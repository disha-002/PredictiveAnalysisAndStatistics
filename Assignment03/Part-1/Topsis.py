import sys
import pandas as pd
import numpy as np


def topsis(input_file, weights, impacts, output_file):

    # ---------- Read input file ----------
    try:
        data = pd.read_csv(input_file)
    except:
        raise Exception("Error: Unable to read input file")

    if data.shape[1] < 3:
        raise Exception("Error: Input file must have at least 3 columns")

    alternatives = data.iloc[:, 0]
    matrix = data.iloc[:, 1:].values

    # ---------- Validate numeric data ----------
    if not np.issubdtype(matrix.dtype, np.number):
        raise Exception("Error: All criteria values must be numeric")

    # ---------- Parse weights and impacts ----------
    weights = list(map(float, weights.split(',')))
    impacts = impacts.split(',')

    if len(weights) != matrix.shape[1]:
        raise Exception("Error: Number of weights must match number of criteria")

    if len(impacts) != matrix.shape[1]:
        raise Exception("Error: Number of impacts must match number of criteria")

    for impact in impacts:
        if impact not in ['+', '-']:
            raise Exception("Error: Impacts must be + or -")

    weights = np.array(weights)

    # ---------- Step 1: Normalize ----------
    norm_matrix = matrix / np.sqrt((matrix ** 2).sum(axis=0))

    # ---------- Step 2: Apply weights ----------
    weighted_matrix = norm_matrix * weights

    # ---------- Step 3: Ideal best and worst ----------
    ideal_best = np.zeros(weighted_matrix.shape[1])
    ideal_worst = np.zeros(weighted_matrix.shape[1])

    for j in range(weighted_matrix.shape[1]):
        if impacts[j] == '+':
            ideal_best[j] = weighted_matrix[:, j].max()
            ideal_worst[j] = weighted_matrix[:, j].min()
        else:
            ideal_best[j] = weighted_matrix[:, j].min()
            ideal_worst[j] = weighted_matrix[:, j].max()

    # ---------- Step 4: Distances ----------
    distance_best = np.sqrt(((weighted_matrix - ideal_best) ** 2).sum(axis=1))
    distance_worst = np.sqrt(((weighted_matrix - ideal_worst) ** 2).sum(axis=1))

    # ---------- Step 5: TOPSIS score ----------
    score = distance_worst / (distance_best + distance_worst)

    # ---------- Step 6: Ranking ----------
    rank = pd.Series(score).rank(ascending=False)
    rank = rank.astype(int).values


    # ---------- Output ----------
    data['Topsis Score'] = score
    data['Rank'] = rank.astype(int)

    data.to_csv(output_file, index=False)


# ---------- Command line execution ----------
if __name__ == "__main__":

    if len(sys.argv) != 5:
        print("Usage: python topsis.py <input_file> <weights> <impacts> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    output_file = sys.argv[4]

    try:
        topsis(input_file, weights, impacts, output_file)
        print("TOPSIS calculation completed successfully.")
    except Exception as e:
        print(e)
