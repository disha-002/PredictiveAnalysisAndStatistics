import pandas as pd
import numpy as np

def topsis(input_file, weights, impacts, output_file):

    data = pd.read_csv(input_file)
    matrix = data.iloc[:, 1:].values

    weights = np.array(list(map(float, weights.split(','))))
    impacts = impacts.split(',')

    norm_matrix = matrix / np.sqrt((matrix ** 2).sum(axis=0))
    weighted_matrix = norm_matrix * weights

    ideal_best = []
    ideal_worst = []

    for j in range(matrix.shape[1]):
        if impacts[j] == '+':
            ideal_best.append(weighted_matrix[:, j].max())
            ideal_worst.append(weighted_matrix[:, j].min())
        else:
            ideal_best.append(weighted_matrix[:, j].min())
            ideal_worst.append(weighted_matrix[:, j].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    dist_best = np.sqrt(((weighted_matrix - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted_matrix - ideal_worst) ** 2).sum(axis=1))

    score = dist_worst / (dist_best + dist_worst)
    rank = np.argsort(-score) + 1

    data["Topsis Score"] = score
    data["Rank"] = rank

    data.to_csv(output_file, index=False)