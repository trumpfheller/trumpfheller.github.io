
## Data cleaning on the gas records of my BB.

I am driving a 2003 4cyl. 1.8 liter C230 coupe. 
It is a German thing: 
* small car to find always parking space.
* small engine to make sure I don't have to worry about prizes.
* and enough HP since it has a compressor (German word for turbo): I shift into the third and emmidiatly get proper acceleration. 

When I bought the car in 2010 (I guess) it had 87K on it and now (2024) the odometer is showing 165K. BB (name of my car; BB = BabyBenz since it is the smallest of all Mercs).

Since 2019 I am recording the gas consumption of my car to get an idea what age does to the gas consumption. Well, in part. I also was hoping to predict any probable issues based on higher or lower consumption as usual.

### 1.Initial Exploration

```python
import pandas as pd
import numpy as np
df = pd.read_csv("data/bb.csv")
np.random.seed(0) 
print(df.head())  # View the first few rows
```

```sql
         Date  Odometer  miles driven  Gallons  Price/Gal  Total   MPG  \
0  05/23/2024  160439.0         259.0    12.66       5.10  64.57  20.5   
1  04/14/2024  160180.0         306.0    13.26       6.20  82.23  23.1   
2  03/28/2024  159874.0         215.0     9.64       4.80  46.24  22.3   
3  02/09/2024  159659.0         342.0    13.50       5.18  69.89  25.3   
4  12/26/2023  159371.0         317.0    13.00       4.24  55.20  24.4   

   l/100km  
0      NaN  
1     10.2  
2     10.5  
3      9.3  
4      9.6  
```

### delete a column

* at this point I had already tried to delete the 'Comment' column which didn't work. 

```python
df = df.drop(columns=['Random notes', 'Comment\ncapacity: 16.2Gal GOAL:26MPG (8,8 l/km)'])

# Print the updated DataFrame (optional)
print(df)

# Get the index of the row where the second column contains word 'Average'
index_to_drop = df[df.iloc[:, 1] == 'Average'].index

# Drop the row using the index
df = df.drop(index=index_to_drop)

# Print the updated DataFrame (optional)
print(df)
```

* For the sake of time and since these are only two columns I removed them by hand.

### 2.Columns and details

* after I had deleted the columns, I need to know what I would be working with. So I print out the columns and then check the datatype (consistency, validity).

```python
print(df.columns)  # Get column names
```

```sql
# result
Index(['Date', 'Odometer', 'miles driven', 'Gallons', 'Price/Gal', 'Total',
       'MPG', 'l/100km'],
      dtype='object')
```

```python
print(df.info())
```

```sql
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 99 entries, 0 to 98
Data columns (total 8 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   Date          99 non-null     object 
 1   Odometer      98 non-null     float64
 2   miles driven  96 non-null     float64
 3   Gallons       96 non-null     float64
 4   Price/Gal     94 non-null     float64
 5   Total         94 non-null     float64
 6   MPG           94 non-null     float64
 7   l/100km       93 non-null     float64
dtypes: float64(7), object(1)
memory usage: 6.3+ KB
None
```

## 3.Handle Missing Values

* I knew I had left some cells empty in the past. Before choosing a strategy, 
I had to get a clear picture.
* the most common way to get an idea is using `isnull().sum()`

```python
print(df.isnull().sum()) 
```

```sql
Date            0
Odometer        1
miles driven    3
Gallons         3
Price/Gal       5
Total           5
MPG             5
l/100km         6
dtype: int64
```

* Maybe I can get that in percentage?

```python
missing_values_count = df.isnull().sum()
total_cells = np.prod(df.shape)
total_missing = missing_values_count.sum()

# percent of data that is missing
percent_missing = (total_missing/total_cells) * 100
print(percent_missing)
```

result: 3.53%

> to be continued






