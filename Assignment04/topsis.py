import sys
import pandas as pd
import numpy as np

def topsis(input_file, weights, impacts, output_file):
    # Read input CSV
    data = pd.read_csv(input_file)

    if data.shape[1] < 3:
        raise Exception("Input file must contain at least 3 columns")

    # Extract criteria data (excluding first column)
    criteria_data = data.iloc[:, 1:].values.astype(float)

    # Check weights and impacts length
    if len(weights) != criteria_data.shape[1]:
        raise Exception("Number of weights must match number of criteria")

    if len(impacts) != criteria_data.shape[1]:
        raise Exception("Number of impacts must match number of criteria")

    for i in impacts:
        if i not in ['+', '-']:
            raise Exception("Impacts must be either '+' or '-'")

    # Step 1: Normalize the decision matrix
    norm_matrix = criteria_data / np.sqrt((criteria_data ** 2).sum(axis=0))

    # Step 2: Apply weights
    weighted_matrix = norm_matrix * weights

    # Step 3: Determine ideal best and ideal worst
    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted_matrix[:, i].max())
            ideal_worst.append(weighted_matrix[:, i].min())
        else:
            ideal_best.append(weighted_matrix[:, i].min())
            ideal_worst.append(weighted_matrix[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    # Step 4: Calculate distances
    distance_best = np.sqrt(((weighted_matrix - ideal_best) ** 2).sum(axis=1))
    distance_worst = np.sqrt(((weighted_matrix - ideal_worst) ** 2).sum(axis=1))

    # Step 5: Calculate TOPSIS score
    topsis_score = distance_worst / (distance_best + distance_worst)

    # Step 6: Rank alternatives
    ranks = topsis_score.argsort()[::-1] + 1

    # Add results to dataframe
    data["Topsis Score"] = topsis_score
    data["Rank"] = ranks

    # Save output
    data.to_csv(output_file, index=False)

    print("TOPSIS calculation completed successfully.")


# -----------------------------
# Command line interface
# -----------------------------
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage:")
        print("python topsis.py <input_file> <weights> <impacts> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = list(map(float, sys.argv[2].split(",")))
    impacts = sys.argv[3].split(",")
    output_file = sys.argv[4]

    topsis(input_file, weights, impacts, output_file)
