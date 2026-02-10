from flask import Flask, render_template, request
import os
import re
import smtplib
from email.message import EmailMessage
from topsis import topsis

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

EMAIL_REGEX = r'^[\w\.-]+@[\w\.-]+\.\w+$'


def send_email(receiver_email, attachment_path):
    sender_email = "YOUR_EMAIL"
    sender_password = "YOUR_APP_PASSWORD"   # Gmail App Password

    msg = EmailMessage()
    msg["Subject"] = "TOPSIS Result"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content("Please find the attached TOPSIS result file.")

    with open(attachment_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="octet-stream",
            filename="topsis_output.csv"
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        weights = request.form["weights"]
        impacts = request.form["impacts"]
        email = request.form["email"]

        # Email validation
        if not re.match(EMAIL_REGEX, email):
            return "Invalid email address"

        input_path = os.path.join(UPLOAD_FOLDER, file.filename)
        output_path = os.path.join(OUTPUT_FOLDER, "topsis_output.csv")

        file.save(input_path)

        weights = list(map(float, weights.split(",")))
        impacts = impacts.split(",")

        topsis(input_path, weights, impacts, output_path)

        send_email(email, output_path)

        return "TOPSIS completed successfully. Result emailed."

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
