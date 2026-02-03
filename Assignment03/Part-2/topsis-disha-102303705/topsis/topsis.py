import sys
import pandas as pd
import numpy as np


def topsis(input_file, weights, impacts, output_file):

    data = pd.read_csv(input_file)

    if data.shape[1] < 3:
        raise Exception("Input file must contain at least 3 columns")

    matrix = data.iloc[:, 1:].values

    if not np.issubdtype(matrix.dtype, np.number):
        raise Exception("All criteria values must be numeric")

    weights = list(map(float, weights.split(',')))
    impacts = impacts.split(',')

    if len(weights) != matrix.shape[1]:
        raise Exception("Number of weights must match number of criteria")

    if len(impacts) != matrix.shape[1]:
        raise Exception("Number of impacts must match number of criteria")

    for impact in impacts:
        if impact not in ['+', '-']:
            raise Exception("Impacts must be + or -")

    weights = np.array(weights)

    norm_matrix = matrix / np.sqrt((matrix ** 2).sum(axis=0))
    weighted_matrix = norm_matrix * weights

    ideal_best = np.zeros(matrix.shape[1])
    ideal_worst = np.zeros(matrix.shape[1])

    for j in range(matrix.shape[1]):
        if impacts[j] == '+':
            ideal_best[j] = weighted_matrix[:, j].max()
            ideal_worst[j] = weighted_matrix[:, j].min()
        else:
            ideal_best[j] = weighted_matrix[:, j].min()
            ideal_worst[j] = weighted_matrix[:, j].max()

    dist_best = np.sqrt(((weighted_matrix - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted_matrix - ideal_worst) ** 2).sum(axis=1))

    score = dist_worst / (dist_best + dist_worst)
    rank = np.argsort(-score) + 1

    data["Topsis Score"] = score
    data["Rank"] = rank

    data.to_csv(output_file, index=False)


def main():
    if len(sys.argv) != 5:
        print("Usage: topsis <input_file> <weights> <impacts> <output_file>")
        sys.exit(1)

    _, input_file, weights, impacts, output_file = sys.argv

    try:
        topsis(input_file, weights, impacts, output_file)
        print("TOPSIS calculation completed successfully.")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
