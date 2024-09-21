# Lab 03 - Data Visualization

# Introduction

This notebook provides a brief introduction to data visualization tools and principles. We will explore basic concepts using the Matplotlib library in Python and practice fundamental design principles.

## Note:
#### - Each task will be graded separately
#### - Every Plot should have proper Axis and Title text
#### - Set proper X and Y limits for plots
#### - Marks will be deducted for incomplete results

# 1. Import libraries: (2)
- Numpy
- Pandas
- Matplotlib - pyplot


```python
import matplotlib.pyplot as plt
```

# 2. Generate and plot data: (2)
- x = [1, 2, 3, 4, 5]
- y = [3, 5, 7, 2, 1]

### Plot the data as a scatter plot


```python
# Create sample data
x = [1, 2, 3, 4, 5]
y = [3, 5, 7, 2, 1]

# Plot the data as a scatter plot
plt.scatter(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Sample Scatter Plot")
plt.show()

```


    
![png](LAB%2003%20Sol_files/LAB%2003%20Sol_7_0.png)
    


# 3. Customize plot elements: (4)

- Change the plot market and color
- Add grid lines 
- Add proper Labels and Title


```python

# Change plot marker and color
plt.scatter(x, y, marker='o', color='red')
plt.grid(True)  # Add gridlines

# Set axis limits
plt.xlim(0, 6)
plt.ylim(0, 8)

# Add labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Customized Scatter Plot")
plt.show()

```


    
![png](LAB%2003%20Sol_files/LAB%2003%20Sol_10_0.png)
    


# 4. Create different chart types: (4)
- Line Plot
- Bar Plot
- Histogram


```python
# Line plot
plt.plot(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Plot")
plt.show()

# Bar plot
plt.bar(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Bar Plot")
plt.show()

# Histogram
plt.hist(y)
plt.xlabel("Y-axis values")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()
```


    
![png](LAB%2003%20Sol_files/LAB%2003%20Sol_12_0.png)
    



    
![png](LAB%2003%20Sol_files/LAB%2003%20Sol_12_1.png)
    



    
![png](LAB%2003%20Sol_files/LAB%2003%20Sol_12_2.png)
    


# 5. Enhance plot with annotations: (4)
- Add an annotation on a random point in plot


```python
# Add text annotation
plt.scatter(x, y)
plt.annotate("Point (2, 5)", (2, 5), textcoords="offset points", xytext=(0, 10), arrowprops=dict(facecolor='black'))
plt.show()

```


    
![png](LAB%2003%20Sol_files/LAB%2003%20Sol_14_0.png)
    


# 6. Subplots and multiple plots: (4)
Create 2 Subplots
+ Bar Plot
+ Scatter Plot


```python
# Create two subplots
plt.subplot(1, 2, 1)
plt.scatter(x, y)
plt.title("Scatter Plot")

plt.subplot(1, 2, 2)
plt.bar(x, y)
plt.title("Bar Plot")

plt.show()
```


    
![png](LAB%2003%20Sol_files/LAB%2003%20Sol_16_0.png)
    


# 7. Saving plots: (4)
Save the most recent plot as PNG


```python
plt.plot(x, y)
plt.title("Line Plot")
plt.savefig("line_plot.png")  # Save as image file
plt.show()
```


    
![png](LAB%2003%20Sol_files/LAB%2003%20Sol_18_0.png)
    


# 8. Color theory and application: (4)

##### Explore Color Palattes
Assign new variables
- b = range(100)
- a = [i**2 for i in x]

Create a Scatter Plot with Viridis Colormap


```python
import matplotlib.pyplot as plt

# Example using viridis colormap
x = range(100)
y = [i**2 for i in x]

plt.scatter(x, y, cmap='viridis')
plt.colorbar(label='Color values')
plt.title("Scatter plot with viridis colormap")
plt.show()
```

    /var/folders/ln/3h7vxn1x297c87rv0v1zvhyc0000gn/T/ipykernel_19838/3260286117.py:7: UserWarning: No data for colormapping provided via 'c'. Parameters 'cmap' will be ignored
      plt.scatter(x, y, cmap='viridis')



    
![png](LAB%2003%20Sol_files/LAB%2003%20Sol_21_1.png)
    


#### Apply Color Maps to Data
Generate a 10x10 heatmap of random data using the 'coolwarm' colormap and display the color bar with labeled data values.



```python
# Example using heatmap with coolwarm colormap
import numpy as np

data = np.random.rand(10, 10)
plt.imshow(data, cmap='coolwarm')
plt.colorbar(label='Data values')
plt.title("Heatmap with coolwarm colormap")
plt.show()
```


    
![png](LAB%2003%20Sol_files/LAB%2003%20Sol_23_0.png)
    


# 9. Layout and composition: (4)

Explore the impact of different plot sizes and aspect ratios by creating a small square plot and a larger wide plot using the 'scatter' function.
- Small = 5x5
- Large = 10x5


```python
# Smaller plot with square aspect ratio
plt.figure(figsize=(5, 5))
plt.scatter(x, y)
plt.title("Small square plot")
plt.show()

# Larger plot with wider aspect ratio
plt.figure(figsize=(10, 5))
plt.scatter(x, y)
plt.title("Large wide plot")
plt.show()
```


    
![png](LAB%2003%20Sol_files/LAB%2003%20Sol_26_0.png)
    



    
![png](LAB%2003%20Sol_files/LAB%2003%20Sol_26_1.png)
    


Modify the legend placement to the upper left and adjust the positioning of the annotation for the point (2, 5) in a scatter plot


```python

plt.scatter(x, y)
plt.legend(loc='upper left')  # Change legend location

plt.annotate("Point (2, 5)", (2, 5), xytext=(-20, 10),  # Adjust annotation position
             textcoords="offset points", arrowprops=dict(facecolor='black'))
plt.show()
```

    No artists with labels found to put in legend.  Note that artists whose label start with an underscore are ignored when legend() is called with no argument.



    
![png](LAB%2003%20Sol_files/LAB%2003%20Sol_28_1.png)
    


Enhance the use of whitespace in a plot by adjusting the spacing around the plot area and creating a scatter plot with improved whitespace.


```python
plt.figure(figsize=(8, 5))

# Add more space around the plot
plt.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.15)

plt.scatter(x, y)
plt.title("Plot with improved whitespace")
plt.show()
```


    
![png](LAB%2003%20Sol_files/LAB%2003%20Sol_30_0.png)
    


# 10. Effective chart selection: (4)

Choose appropriate chart type for the following data
- categories = ['A', 'B', 'C']
- values = [10, 20, 30]


```python
# Example: Using bar chart for categorical data

categories = ['A', 'B', 'C']
values = [10, 20, 30]

plt.bar(categories, values)
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar chart for categorical data")
plt.show()

```


    
![png](LAB%2003%20Sol_files/LAB%2003%20Sol_33_0.png)
    


Showcase the use of simpler visuals, such as a scatter plot with adjusted markers and transparency, to cater to a broader audience.
- marker: round
- color: blue
- transparency: 70%


```python
# Example: Using simpler visuals for broader audiences

plt.scatter(x, y, marker='o', color='blue', alpha=0.8)  # Adjust marker and transparency
plt.title("Simple scatter plot for general audience")
plt.show()

```


    
![png](LAB%2003%20Sol_files/LAB%2003%20Sol_35_0.png)
    


# 11. Customize plot styles: (4)

Experiment with line styles, marker shapes, and color gradients:
- Dashed Line
- Triangle Marker (Green)

Utilize color gradients to represent data using a specified colormap, for example, 'YlGnBu', to create a scatter plot with a color bar.


```python
# Different line styles and markers
plt.plot(x, y, linestyle='--', marker='^', color='green')
plt.show()

# Color gradient
cmap = plt.cm.get_cmap('YlGnBu')
colors = cmap(np.linspace(0, 1, len(x)))
plt.scatter(x, y, c=colors)
plt.colorbar(label='Color values')
plt.show()
```


    
![png](LAB%2003%20Sol_files/LAB%2003%20Sol_38_0.png)
    


    C:\Users\Usman\AppData\Local\Temp\ipykernel_15736\1290391746.py:6: MatplotlibDeprecationWarning: The get_cmap function was deprecated in Matplotlib 3.7 and will be removed two minor releases later. Use ``matplotlib.colormaps[name]`` or ``matplotlib.colormaps.get_cmap(obj)`` instead.
      cmap = plt.cm.get_cmap('YlGnBu')



    
![png](LAB%2003%20Sol_files/LAB%2003%20Sol_38_2.png)
    



```python

```
