
### 1. Load the data

```python
import pandas as pd
df = pd.read_csv("data/2015.csv")
```

### 2. Initial Exploration

```python
print(df.head())  # View the first few rows
print(df.columns)  # Get column names
print(df.info())  # Summary of data types and missing values
print(df.describe())  # Summary statistics
```

### 3.  Handle Missing Values

* Identify missing values

```python
print(df.isnull().sum())  # Count missing values per column
```

#### Choose a strategy:

* 1. Drop rows with missing values

```python
df.dropna(inplace=True)
```

* 2. Fill missing values with a constant (e.g., 0)

```python
df.fillna(0, inplace=True)
```

* 3. Fill using a method like 'ffill' (forward fill) or 'bfill' (backward fill)

```python
df.fillna(method='ffill', inplace=True)
```

### 4.  Data Type Conversion

#### Check for columns that need conversion (e.g., 'date' to datetime, 'price' to numeric)

```python
df['date'] = pd.to_datetime(df['date'])
df['price'] = pd.to_numeric(df['price'], errors='coerce')  # Handle non-numeric values
```

### 5.  Duplicate Removal

* Identify duplicate rows 

```python
print(df.duplicated().sum())  # Count duplicate rows
```

* Remove duplicates

```python 
df.drop_duplicates(inplace=True)
```

### 6.  Outlier Handling 
> (I should probably use Jupyter here; I am still experimenting)

* Explore outliers visually (box plots, histograms)
* Apply methods like:
  * Removing outliers directly
  * Capping outliers (setting limits)
  * Using robust statistical methods (e.g., interquartile range)

### 7.  Standardization/Normalization (Optional)

* If required for machine learning or analysis, consider:
  * tandardization (zero mean, unit variance)
  * Normalization (scaling to a range like [0, 1])

### 8.  Encoding Categorical Features (Optional)

* Convert categorical columns into numerical representations using methods like:
  * One-hot encoding (create dummy variables)
  * Label encoding (assign numerical labels)

### 9.  Data Validation (Optional)
* Ensure data integrity using checks:
  * Range checks (e.g., age should be within a reasonable range)
  * Consistency checks (e.g., values in different columns should be logically related)

### 10.  Save the cleaned data

```python
df.to_csv("cleaned_data/2015_cleaned.csv", index=False)
```
