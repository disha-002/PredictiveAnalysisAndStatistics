## User Manual

This package provides a command-line implementation of the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) method for multi-criteria decision making.

## Installation

Install the package using pip:

```bash
pip install topsis-disha-102303705
```

## Usage

After installation, the package can be executed using the topsis command:

```bash
topsis <input_file> <weights> <impacts> <output_file>
```

## Command Line Arguments

**input_file**
Path to the input CSV file. The first column should contain the names of the alternatives, and the remaining columns should contain numerical values for each criterion.

**weights**
Comma-separated numerical values representing the importance of each criterion.
Example: 1,1,1,1,1

**impacts**
Comma-separated symbols indicating whether a criterion is beneficial or non-beneficial.
Use + for benefit criteria and - for cost criteria.
Example: +,+,-,+,+

**output_file**
Path where the output CSV file will be saved.

## Example
```bash
topsis Topsis_data.csv "1,1,1,1,1" "+,+,+,+,+" output.csv
```

## Output

The output CSV file contains two additional columns:

Topsis Score – indicates the relative closeness of each alternative to the ideal solution

Rank – rank of each alternative based on the TOPSIS score

A higher TOPSIS score indicates a better alternative.