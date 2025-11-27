# A Neural Network–Based Framework for Identifying Hazardous Road Segments Using Geometrical Road Attributes

This folder contains the raw data used for training and evaluating the neural network model.

## Data Files

### `sequences_labels.npz`
- **Format:** NumPy `.npz` archive  
- **Library version:** `numpy 2.3.2`  
- **Contents:**  
  - **X** — input sequences (geometrical road attributes)  
  - **y** — corresponding labels (hazardous vs non-hazardous segments)

## Purpose
These data files were used in the experiments described in the paper:

**A Neural Network–Based Framework for Identifying Hazardous Road Segments Using Geometrical Road Attributes**

The dataset supports the full reproducibility of the model architecture, preprocessing steps, and evaluation procedures.

## Notes
- The `.npz` file was generated in Python using `numpy.savez`.  
- Shapes of arrays can be inspected in Python:

```python
import numpy as np
data = np.load("sequences_labels.npz")
data["X"].shape, data["y"].shape