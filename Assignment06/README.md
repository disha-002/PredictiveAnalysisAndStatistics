# Assignment – Sampling Techniques on Imbalanced Dataset

This repository contains the solution for the Sampling Assignment. The objective of this assignment is to analyze the impact of different sampling techniques on machine learning models using a highly imbalanced credit card dataset.

---

## Objective

The objectives of this assignment are:

- To understand the importance of sampling techniques in handling imbalanced datasets  
- To convert an imbalanced dataset into a balanced dataset  
- To apply different sampling strategies  
- To evaluate how sampling affects the accuracy of multiple machine learning models  

---

## Dataset

The dataset used is the **Credit Card Fraud Detection Dataset**, downloaded from:

https://github.com/AnjulaMehto/Sampling_Assignment/blob/main/Creditcard_data.csv

The dataset is highly imbalanced, with significantly fewer fraud cases compared to non-fraud cases.

---

## Step 1 – Balancing the Dataset

The dataset was balanced using **undersampling**.  
The majority class was reduced to match the number of samples in the minority class, creating a balanced dataset for further experimentation.

---

## Step 2 – Creating Five Samples

Five different sampling techniques were applied:

- **Sampling1 – Simple Random Sampling**
- **Sampling2 – Systematic Sampling**
- **Sampling3 – Stratified Sampling**
- **Sampling4 – Cluster Sampling**
- **Sampling5 – Bootstrap Sampling**

Each sampling method generated a separate dataset.

---

## Step 3 – Machine Learning Models

Five machine learning models were used:

- **M1 – Logistic Regression**
- **M2 – Decision Tree**
- **M3 – Random Forest**
- **M4 – Support Vector Classifier**
- **M5 – Gaussian Naive Bayes**

Each model was trained and evaluated on all five sampled datasets.

---

## Step 4 – Accuracy Comparison

Accuracy (in percentage) was calculated for each combination of sampling technique and model.
The dataset was split into training and testing sets before model evaluation.


The best sampling technique for each model is:

- **M1 → Sampling5**
- **M2 → Sampling1**
- **M3 → Sampling5**
- **M4 → Sampling1**
- **M5 → Sampling5**

This shows that different models respond differently to various sampling strategies.

---

## Observations

- Sampling techniques significantly influence model performance.
- No single sampling method performs best for all models.
- Undersampling successfully handled class imbalance in this implementation.
- Model behavior varies depending on the sampling strategy used.

---

## Repository Contents

- `Sampling.ipynb` – Jupyter notebook containing complete implementation  
- `Creditcard_data.csv` – Dataset used  
- `README.md` – Description of methodology and results  

---

## Conclusion

This assignment demonstrates how different sampling techniques impact the performance of machine learning models on imbalanced datasets. By balancing the dataset and applying multiple sampling strategies, we compared their effects across different models and identified the most effective sampling method for each case.
