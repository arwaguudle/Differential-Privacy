# Differential Privacy

This repository contains code and experiments exploring **Differential Privacy** mechanisms, developed as part of a **group project** which is to understand how differential privacy techniques protect sensitive data while maintaining useful statistical insights.

---

## Overview

Differential Privacy is a framework that provides formal privacy guarantees when analyzing sensitive datasets.  
In this project, we implement and compare several common differential privacy mechanisms using practical examples and real datasets.

---

## Contents

The repository includes Python files and Jupyter notebooks covering the following:

- **Laplace Mechanism**
  - Adding Laplace noise
  - Privacy guarantees with different epsilon values

- **Gaussian Mechanism**
  - Noise calibration
  - Effect of epsilon on privacy and accuracy

- **Exponential Mechanism**
  - Selection under privacy constraints

- **Randomized Response**
  - Protecting individual responses in surveys

- **Mechanism Comparison**
  - Comparing outputs and privacy trade-offs

- **Mathematical Foundations**
  - Differential privacy formulas and concepts

---

## Datasets

The project uses both synthetic and real datasets, including:
- Survey response datasets
- Banking dataset (`bank_add_full.csv`)
- Generated CSV files for sensitive attributes

---

## Tools & Technologies

- Python
- Jupyter Notebook
- NumPy
- Pandas
- Matplotlib

---

## Contributors

- **Arwa Ibrahim Guudle**
- **Bezadsj**

---

## Notes

This repository was created for a final project and is intended for **educational and research purposes**, focusing on understanding and experimenting with differential privacy concepts.
