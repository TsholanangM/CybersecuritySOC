# Data Processor

This module includes utilities for data preprocessing suitable for machine learning pipelines.

## Functions:

### 1. Load Data
Loads the dataset from a given file path.

```python
import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)
```

### 2. Handle Missing Values
Handles missing values by filling them with a specified strategy.

```python
def handle_missing_values(df, strategy='mean'):
    if strategy == 'mean':
        return df.fillna(df.mean())
    elif strategy == 'drop':
        return df.dropna()
    else:
        raise ValueError("Strategy not recognized!")
```

### 3. Normalize Data
Normalizes the dataset to a given range.

```python
from sklearn.preprocessing import MinMaxScaler

def normalize_data(df):
    scaler = MinMaxScaler()
    return pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
```
