# Lab: Introduction to Data Visualization

## Objective:
- Learn the basics of data types, formats, and data visualization using Python.

### Part 1: Data Types and Formats

1.1 Import necessary libraries:


```python
import pandas as pd
import numpy as np
```

1.2 Create a simple dataset:


```python
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 22],
        'Salary': [50000, 60000, 75000, 45000]}
df = pd.DataFrame(data)
```

1.3 Display the dataset:



```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Age</th>
      <th>Salary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alice</td>
      <td>25</td>
      <td>50000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bob</td>
      <td>30</td>
      <td>60000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Charlie</td>
      <td>35</td>
      <td>75000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>David</td>
      <td>22</td>
      <td>45000</td>
    </tr>
  </tbody>
</table>
</div>



1.4 Check data types of columns:



```python
df.dtypes
```




    Name      object
    Age        int64
    Salary     int64
    dtype: object



1.5 Convert 'Age' to float:


```python
df['Age'] = df['Age'].astype(float)
df.dtypes
```




    Name       object
    Age       float64
    Salary      int64
    dtype: object



1.6 Save the dataset to CSV:



```python
df.to_csv('sample_data.csv', index=True)

```

## Part 2: Data Visualization
2.1 Import Matplotlib library:


```python
import matplotlib.pyplot as plt
%matplotlib inline
```

2.2 Plot a simple line chart:



```python
plt.plot(df['Name'], df['Age'], marker='o')
plt.title('Age Distribution')
plt.xlabel('Name')
plt.ylabel('Age')
plt.show()
```


    
![png](Lab2%20Solution_files/Lab2%20Solution_16_0.png)
    


2.3 Create a bar chart for Salary:



```python
plt.bar(df['Name'], df['Salary'], color='green')
plt.title('Salary Distribution')
plt.xlabel('Name')
plt.ylabel('Salary')
plt.show()
```


    
![png](Lab2%20Solution_files/Lab2%20Solution_18_0.png)
    


2.4 Scatter plot for Age and Salary:



```python
plt.scatter(df['Age'], df['Salary'], color='red')
plt.title('Scatter Plot: Age vs. Salary')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.show()
```


    
![png](Lab2%20Solution_files/Lab2%20Solution_20_0.png)
    


2.5 Save the visualizations:



```python
plt.savefig('line_chart.png')
plt.savefig('bar_chart.png')
plt.savefig('scatter_plot.png')
```


    <Figure size 640x480 with 0 Axes>



```python

```
