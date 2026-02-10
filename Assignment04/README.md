# Assignment 04 – Model Selection using TOPSIS

This repository contains the solution for Assignment 04. The aim of this assignment is to apply the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) method to select the best **pre-trained text summarization model** based on multiple performance metrics.

---

## Task

As my university roll number ends with **5**, the assigned task is **Text Summarization**.  
Multiple pre-trained summarization models were evaluated and ranked using the TOPSIS method.

---

## Models Used

The following pre-trained models were considered for comparison:

- BART  
- DistilBART  
- T5-small  
- BART-base  
- FLAN-T5-small  

---

## Evaluation Criteria

Each model was evaluated using the following criteria:

- **ROUGE Score** – measures the quality of the generated summary (higher is better)  
- **Inference Time (ms)** – time taken to generate the summary (lower is better)  
- **Memory Usage (MB)** – memory consumed during inference (lower is better)  

These metrics were used to create the decision matrix for TOPSIS.

---

## TOPSIS Methodology

The TOPSIS method was applied by normalizing the decision matrix and assigning equal weights to all criteria. Ideal best and ideal worst solutions were identified, and the distance of each model from these ideal points was calculated. Based on these distances, TOPSIS scores were computed and the models were ranked.

The model with the highest TOPSIS score is considered the best overall performer.

**Note:** Email credentials have been intentionally removed from the code for security reasons.

---

## How to Run

Run the summarization models and collect performance metrics:

```bash
python3 run_summarization_models.py
python3 topsis.py summarization_results.csv "1,1,1" "+,-,-" topsis_output.csv
python3 app.py
```

## Results

The final output CSV file contains the **TOPSIS score** and **rank** for each summarization model.  
A higher **TOPSIS score** indicates better overall performance when all evaluation criteria are considered together.

---

## Conclusion

This assignment demonstrates how TOPSIS can be effectively used for model selection when multiple performance metrics are involved. By combining quality, speed, and resource usage into a single decision-making framework, TOPSIS provides a clear and explainable ranking of pre-trained text summarization models.

