# Assignment 03 – TOPSIS Implementation

This repository contains the complete solution for Assignment 03, which focuses on implementing the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) method in multiple forms. The assignment is divided into three parts, each demonstrating a different way of using the same algorithm.

---

## Part 1: Command-Line Implementation

In this part, the TOPSIS algorithm is implemented as a Python script that can be executed from the command line. The program takes an input CSV file along with weights and impacts, computes TOPSIS scores, and generates an output CSV file with ranks.

Folder: `Part-1`

---

## Part 2: Python Package

In this part, the TOPSIS logic is converted into a Python package and published on PyPI. The package can be installed using pip and executed using a command-line command. A user manual explaining installation and usage is provided in the Part-2 README.

Folder: `Part-2`  
PyPI Package: `topsis-disha-102303705`

---

## Part 3: Web Application with Email Support

In this part, a Flask-based web application is developed. Users can upload a CSV file, enter weights and impacts, and provide an email address. The application runs TOPSIS on the server and emails the result CSV file to the user. Email credentials are intentionally excluded for security reasons.

Folder: `Part-3`

---

## Summary

- Part 1 demonstrates the core TOPSIS logic using a command-line program.
- Part 2 packages the logic into a reusable Python module.
- Part 3 extends the solution into a web application with email functionality.

Together, these parts show different practical ways to implement and deploy the TOPSIS method.
