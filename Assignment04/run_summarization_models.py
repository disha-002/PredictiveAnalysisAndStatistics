import time
import csv
import psutil
from transformers import pipeline
from rouge_score import rouge_scorer

# -----------------------------
# Input text to summarize
# -----------------------------
input_text = (
    "Artificial intelligence has seen rapid growth in recent years. "
    "It is being applied in healthcare, finance, education, and many other fields. "
    "Despite its benefits, ethical concerns and data privacy remain major challenges. "
    "Governments and organizations are working to create regulations to ensure responsible use."
)

# -----------------------------
# Reference summary (for ROUGE)
# -----------------------------
reference_summary = (
    "Artificial intelligence is rapidly growing and is used in areas such as "
    "healthcare, finance, and education, but ethical concerns and data privacy remain challenges."
)

# -----------------------------
# Models to evaluate
# -----------------------------
models = {
    "BART": "facebook/bart-large-cnn",
    "DistilBART": "sshleifer/distilbart-cnn-12-6",
    "T5-small": "t5-small",
    "BART-base": "facebook/bart-base",
    "FLAN-T5-small": "google/flan-t5-small"
}

# -----------------------------
# ROUGE scorer
# -----------------------------
scorer = rouge_scorer.RougeScorer(["rouge1"], use_stemmer=True)

results = []

# -----------------------------
# Run models
# -----------------------------
for model_name, model_id in models.items():
    print(f"\nRunning model: {model_name}")

    summarizer = pipeline(
        "summarization",
        model=model_id,
        device=0  # uses MPS on Mac if available
    )

    # Measure inference time
    start_time = time.time()
    summary = summarizer(
        input_text,
        max_length=60,
        min_length=30,
        do_sample=False
    )
    end_time = time.time()

    inference_time = (end_time - start_time) * 1000  # ms

    # Measure memory usage
    memory_used = psutil.Process().memory_info().rss / (1024 ** 2)  # MB

    summary_text = summary[0]["summary_text"]

    # Compute ROUGE score
    rouge_score = scorer.score(reference_summary, summary_text)
    rouge_f1 = rouge_score["rouge1"].fmeasure

    # Print results
    print("Summary:")
    print(summary_text)
    print("ROUGE-1 F1 Score:", round(rouge_f1, 4))
    print("Inference Time (ms):", round(inference_time, 2))
    print("Memory Usage (MB):", round(memory_used, 2))

    # Store results
    results.append({
        "Model": model_name,
        "ROUGE": round(rouge_f1, 4),
        "InferenceTime": round(inference_time, 2),
        "MemoryUsage": round(memory_used, 2)
    })

# -----------------------------
# Final output
# -----------------------------
print("\nFinal Results:")
for r in results:
    print(r)

# -----------------------------
# Save results to CSV
# -----------------------------
csv_file = "summarization_results.csv"

with open(csv_file, mode="w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["Model", "ROUGE", "InferenceTime", "MemoryUsage"]
    )
    writer.writeheader()
    writer.writerows(results)

print(f"\nResults saved to {csv_file}")
