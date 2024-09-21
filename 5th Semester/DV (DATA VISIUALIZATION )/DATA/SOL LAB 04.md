# Data Science
# Assignment '#2 -  Exploratory Data Analysis




```python
%matplotlib inline

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#display wide tables
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 100)
```

We have a list of 10,000 movies with IMDB user rating as imdb.txt. We want to perform a exploratory data analysis of this data in Python by using its Pandas library.  We will perform the cleaning, transformation and then visualization on the raw data. This will help us to understand the data for further processing.


```python
!head imdb.txt

```

    tt0111161	The Shawshank Redemption (1994)	1994	 9.2	619479	142 mins.	Crime|Drama
    tt0110912	Pulp Fiction (1994)	1994	 9.0	490065	154 mins.	Crime|Thriller
    tt0137523	Fight Club (1999)	1999	 8.8	458173	139 mins.	Drama|Mystery|Thriller
    tt0133093	The Matrix (1999)	1999	 8.7	448114	136 mins.	Action|Adventure|Sci-Fi
    tt1375666	Inception (2010)	2010	 8.9	385149	148 mins.	Action|Adventure|Sci-Fi|Thriller
    tt0109830	Forrest Gump (1994)	1994	 8.7	368994	142 mins.	Comedy|Drama|Romance
    tt0169547	American Beauty (1999)	1999	 8.6	338332	122 mins.	Drama
    tt0499549	Avatar (2009)	2009	 8.1	336855	162 mins.	Action|Adventure|Fantasy|Sci-Fi
    tt0108052	Schindler's List (1993)	1993	 8.9	325888	195 mins.	Biography|Drama|History|War
    tt0080684	Star Wars: Episode V - The Empire Strikes Back (1980)	1980	 8.8	320105	124 mins.	Action|Adventure|Family|Sci-Fi


## 1. Loading data

Read the imdb.txt into dataframe named data. The data is tab delimited. The columns names are 'imdbID', 'title', 'year', 'score', 'votes', 'runtime', 'genres'


```python
# Your code here
cols = ['imdbID', 'title', 'year', 'score', 'votes', 'runtime', 'genres']

data = pd.read_csv('imdb.txt', names = cols, delimiter = '\t')

data.head()
```





  <div id="df-fafa7d6a-85ae-4e01-9399-961408b30244">
    <div class="colab-df-container">
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
      <th>imdbID</th>
      <th>title</th>
      <th>year</th>
      <th>score</th>
      <th>votes</th>
      <th>runtime</th>
      <th>genres</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>tt0111161</td>
      <td>The Shawshank Redemption (1994)</td>
      <td>1994</td>
      <td>9.2</td>
      <td>619479</td>
      <td>142 mins.</td>
      <td>Crime|Drama</td>
    </tr>
    <tr>
      <th>1</th>
      <td>tt0110912</td>
      <td>Pulp Fiction (1994)</td>
      <td>1994</td>
      <td>9.0</td>
      <td>490065</td>
      <td>154 mins.</td>
      <td>Crime|Thriller</td>
    </tr>
    <tr>
      <th>2</th>
      <td>tt0137523</td>
      <td>Fight Club (1999)</td>
      <td>1999</td>
      <td>8.8</td>
      <td>458173</td>
      <td>139 mins.</td>
      <td>Drama|Mystery|Thriller</td>
    </tr>
    <tr>
      <th>3</th>
      <td>tt0133093</td>
      <td>The Matrix (1999)</td>
      <td>1999</td>
      <td>8.7</td>
      <td>448114</td>
      <td>136 mins.</td>
      <td>Action|Adventure|Sci-Fi</td>
    </tr>
    <tr>
      <th>4</th>
      <td>tt1375666</td>
      <td>Inception (2010)</td>
      <td>2010</td>
      <td>8.9</td>
      <td>385149</td>
      <td>148 mins.</td>
      <td>Action|Adventure|Sci-Fi|Thriller</td>
    </tr>
  </tbody>
</table>
</div>
      <button class="colab-df-convert" onclick="convertToInteractive('df-fafa7d6a-85ae-4e01-9399-961408b30244')"
              title="Convert this dataframe to an interactive table."
              style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
       width="24px">
    <path d="M0 0h24v24H0V0z" fill="none"/>
    <path d="M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z"/><path d="M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z"/>
  </svg>
      </button>

  <style>
    .colab-df-container {
      display:flex;
      flex-wrap:wrap;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

      <script>
        const buttonEl =
          document.querySelector('#df-fafa7d6a-85ae-4e01-9399-961408b30244 button.colab-df-convert');
        buttonEl.style.display =
          google.colab.kernel.accessAllowed ? 'block' : 'none';

        async function convertToInteractive(key) {
          const element = document.querySelector('#df-fafa7d6a-85ae-4e01-9399-961408b30244');
          const dataTable =
            await google.colab.kernel.invokeFunction('convertToInteractive',
                                                     [key], {});
          if (!dataTable) return;

          const docLinkHtml = 'Like what you see? Visit the ' +
            '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
            + ' to learn more about interactive tables.';
          element.innerHTML = '';
          dataTable['output_type'] = 'display_data';
          await google.colab.output.renderOutput(dataTable, element);
          const docLink = document.createElement('div');
          docLink.innerHTML = docLinkHtml;
          element.appendChild(docLink);
        }
      </script>
    </div>
  </div>




__Marks = 2__

Check the data types of each column


```python
# Your code here
data.dtypes
```




    imdbID      object
    title       object
    year         int64
    score      float64
    votes        int64
    runtime     object
    genres      object
    dtype: object



__Marks = 1__

## 2. Clean the DataFrame

The data frame has several problems

1. The runtime column is stored as a string
2. The genres column has several genres together. This way, it is hard to check which movies are Action movies and so on.
3. The movie year is also present in the title


### Fix the runtime column
Convert the string '142 mins' to number 142.


```python
# Your code here
#run1 = data.iloc[0, 5]
#min, unit = run1.split(' ')
#data.iloc[0, 5] = int(min)
#data.head()


# above method will display an error in the next block so instead of changing it in data we'll change the value '142 mins' explicitly
int(data.iloc[0,5].split(' ')[0])
```




    142



__Marks = 3__

Perform this conversion on every element in the dataframe `data`


```python
# Your code here
data_rt = data['runtime'].str.split(' ', expand = True)

data['runtime'] = data_rt[0].astype(int)

data.head()
```





  <div id="df-8671132b-3320-425f-9de8-6eac3cda99f4">
    <div class="colab-df-container">
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
      <th>imdbID</th>
      <th>title</th>
      <th>year</th>
      <th>score</th>
      <th>votes</th>
      <th>runtime</th>
      <th>genres</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>tt0111161</td>
      <td>The Shawshank Redemption (1994)</td>
      <td>1994</td>
      <td>9.2</td>
      <td>619479</td>
      <td>142</td>
      <td>Crime|Drama</td>
    </tr>
    <tr>
      <th>1</th>
      <td>tt0110912</td>
      <td>Pulp Fiction (1994)</td>
      <td>1994</td>
      <td>9.0</td>
      <td>490065</td>
      <td>154</td>
      <td>Crime|Thriller</td>
    </tr>
    <tr>
      <th>2</th>
      <td>tt0137523</td>
      <td>Fight Club (1999)</td>
      <td>1999</td>
      <td>8.8</td>
      <td>458173</td>
      <td>139</td>
      <td>Drama|Mystery|Thriller</td>
    </tr>
    <tr>
      <th>3</th>
      <td>tt0133093</td>
      <td>The Matrix (1999)</td>
      <td>1999</td>
      <td>8.7</td>
      <td>448114</td>
      <td>136</td>
      <td>Action|Adventure|Sci-Fi</td>
    </tr>
    <tr>
      <th>4</th>
      <td>tt1375666</td>
      <td>Inception (2010)</td>
      <td>2010</td>
      <td>8.9</td>
      <td>385149</td>
      <td>148</td>
      <td>Action|Adventure|Sci-Fi|Thriller</td>
    </tr>
  </tbody>
</table>
</div>
      <button class="colab-df-convert" onclick="convertToInteractive('df-8671132b-3320-425f-9de8-6eac3cda99f4')"
              title="Convert this dataframe to an interactive table."
              style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
       width="24px">
    <path d="M0 0h24v24H0V0z" fill="none"/>
    <path d="M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z"/><path d="M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z"/>
  </svg>
      </button>

  <style>
    .colab-df-container {
      display:flex;
      flex-wrap:wrap;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

      <script>
        const buttonEl =
          document.querySelector('#df-8671132b-3320-425f-9de8-6eac3cda99f4 button.colab-df-convert');
        buttonEl.style.display =
          google.colab.kernel.accessAllowed ? 'block' : 'none';

        async function convertToInteractive(key) {
          const element = document.querySelector('#df-8671132b-3320-425f-9de8-6eac3cda99f4');
          const dataTable =
            await google.colab.kernel.invokeFunction('convertToInteractive',
                                                     [key], {});
          if (!dataTable) return;

          const docLinkHtml = 'Like what you see? Visit the ' +
            '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
            + ' to learn more about interactive tables.';
          element.innerHTML = '';
          dataTable['output_type'] = 'display_data';
          await google.colab.output.renderOutput(dataTable, element);
          const docLink = document.createElement('div');
          docLink.innerHTML = docLinkHtml;
          element.appendChild(docLink);
        }
      </script>
    </div>
  </div>




__Marks = 2__

### Split the genres

We would like to split the genres column into many columns. Each new column will correspond to a single genre, and each cell will be True or False.

First, we would like to find the all the unique genres present in any record. Its better to sort the genres to locate easily.


```python
#determine the unique genres

gen_cols = data['genres'].str.split('|')
gen_cols = gen_cols.dropna()
gen_cols = gen_cols.explode()
sorted_genres = gen_cols.sort_values()
genres = sorted_genres.unique()

genres

```




    array(['Action', 'Adult', 'Adventure', 'Animation', 'Biography', 'Comedy',
           'Crime', 'Drama', 'Family', 'Fantasy', 'Film-Noir', 'History',
           'Horror', 'Music', 'Musical', 'Mystery', 'News', 'Reality-TV',
           'Romance', 'Sci-Fi', 'Sport', 'Thriller', 'War', 'Western'],
          dtype=object)



__Marks = 4__

Then make a column for each genre


```python
#make a column for each genre
gen_cols = data['genres'].str.get_dummies("|")
gen_cols = gen_cols.replace({1: True, 0: False})
data = pd.concat([data, gen_cols], axis = 1)

data
```





  <div id="df-1f1a0edc-4227-41d7-8e65-0c69e357e9bb">
    <div class="colab-df-container">
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
      <th>imdbID</th>
      <th>title</th>
      <th>year</th>
      <th>score</th>
      <th>votes</th>
      <th>runtime</th>
      <th>genres</th>
      <th>Action</th>
      <th>Adult</th>
      <th>Adventure</th>
      <th>Animation</th>
      <th>Biography</th>
      <th>Comedy</th>
      <th>Crime</th>
      <th>Drama</th>
      <th>Family</th>
      <th>Fantasy</th>
      <th>Film-Noir</th>
      <th>History</th>
      <th>Horror</th>
      <th>Music</th>
      <th>Musical</th>
      <th>Mystery</th>
      <th>News</th>
      <th>Reality-TV</th>
      <th>Romance</th>
      <th>Sci-Fi</th>
      <th>Sport</th>
      <th>Thriller</th>
      <th>War</th>
      <th>Western</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>tt0111161</td>
      <td>The Shawshank Redemption (1994)</td>
      <td>1994</td>
      <td>9.2</td>
      <td>619479</td>
      <td>142</td>
      <td>Crime|Drama</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>tt0110912</td>
      <td>Pulp Fiction (1994)</td>
      <td>1994</td>
      <td>9.0</td>
      <td>490065</td>
      <td>154</td>
      <td>Crime|Thriller</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>tt0137523</td>
      <td>Fight Club (1999)</td>
      <td>1999</td>
      <td>8.8</td>
      <td>458173</td>
      <td>139</td>
      <td>Drama|Mystery|Thriller</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>tt0133093</td>
      <td>The Matrix (1999)</td>
      <td>1999</td>
      <td>8.7</td>
      <td>448114</td>
      <td>136</td>
      <td>Action|Adventure|Sci-Fi</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>tt1375666</td>
      <td>Inception (2010)</td>
      <td>2010</td>
      <td>8.9</td>
      <td>385149</td>
      <td>148</td>
      <td>Action|Adventure|Sci-Fi|Thriller</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>9995</th>
      <td>tt0807721</td>
      <td>Meduzot (2007)</td>
      <td>2007</td>
      <td>7.0</td>
      <td>1357</td>
      <td>78</td>
      <td>Drama</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>9996</th>
      <td>tt0339642</td>
      <td>Daltry Calhoun (2005)</td>
      <td>2005</td>
      <td>5.2</td>
      <td>1357</td>
      <td>100</td>
      <td>Comedy|Drama|Music|Romance</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>9997</th>
      <td>tt0060880</td>
      <td>The Quiller Memorandum (1966)</td>
      <td>1966</td>
      <td>6.5</td>
      <td>1356</td>
      <td>104</td>
      <td>Drama|Mystery|Thriller</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>9998</th>
      <td>tt0152836</td>
      <td>Taal (1999)</td>
      <td>1999</td>
      <td>6.5</td>
      <td>1356</td>
      <td>179</td>
      <td>Musical|Romance</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>9999</th>
      <td>tt0279977</td>
      <td>The Navigators (2001)</td>
      <td>2001</td>
      <td>6.9</td>
      <td>1356</td>
      <td>96</td>
      <td>Comedy|Drama</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
<p>10000 rows × 31 columns</p>
</div>
      <button class="colab-df-convert" onclick="convertToInteractive('df-1f1a0edc-4227-41d7-8e65-0c69e357e9bb')"
              title="Convert this dataframe to an interactive table."
              style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
       width="24px">
    <path d="M0 0h24v24H0V0z" fill="none"/>
    <path d="M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z"/><path d="M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z"/>
  </svg>
      </button>

  <style>
    .colab-df-container {
      display:flex;
      flex-wrap:wrap;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

      <script>
        const buttonEl =
          document.querySelector('#df-1f1a0edc-4227-41d7-8e65-0c69e357e9bb button.colab-df-convert');
        buttonEl.style.display =
          google.colab.kernel.accessAllowed ? 'block' : 'none';

        async function convertToInteractive(key) {
          const element = document.querySelector('#df-1f1a0edc-4227-41d7-8e65-0c69e357e9bb');
          const dataTable =
            await google.colab.kernel.invokeFunction('convertToInteractive',
                                                     [key], {});
          if (!dataTable) return;

          const docLinkHtml = 'Like what you see? Visit the ' +
            '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
            + ' to learn more about interactive tables.';
          element.innerHTML = '';
          dataTable['output_type'] = 'display_data';
          await google.colab.output.renderOutput(dataTable, element);
          const docLink = document.createElement('div');
          docLink.innerHTML = docLinkHtml;
          element.appendChild(docLink);
        }
      </script>
    </div>
  </div>




__Marks = 5__

### Eliminate year from the title
We can fix each element by stripping off the last 7 characters


```python
#Strip off last 7 character from title
data['title'] = data['title'].str[: -7]

data["title"]
```




    0       The Shawshank Redemption
    1                   Pulp Fiction
    2                     Fight Club
    3                     The Matrix
    4                      Inception
                      ...           
    9995                     Meduzot
    9996              Daltry Calhoun
    9997      The Quiller Memorandum
    9998                        Taal
    9999              The Navigators
    Name: title, Length: 10000, dtype: object



__Marks = 1__

## 3. Descriptive Statistics

Next, we would like to discover outliers. One possible way is to describe some basic, global summaries of the DataFrame on `score`, `runtime`, `year`, `votes`.


```python
#Call `describe` on relevant columns
data_Disc = data[['score', 'runtime', 'year', 'votes']].describe()

data_Disc
```





  <div id="df-fb2b2cb6-1e6b-4987-b749-e3686830888f">
    <div class="colab-df-container">
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
      <th>score</th>
      <th>runtime</th>
      <th>year</th>
      <th>votes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>10000.000000</td>
      <td>10000.000000</td>
      <td>10000.000000</td>
      <td>10000.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>6.386070</td>
      <td>103.578400</td>
      <td>1993.472800</td>
      <td>16604.012800</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1.189933</td>
      <td>26.628698</td>
      <td>14.829924</td>
      <td>34563.459698</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.500000</td>
      <td>0.000000</td>
      <td>1950.000000</td>
      <td>1356.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>5.700000</td>
      <td>93.000000</td>
      <td>1986.000000</td>
      <td>2333.750000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>6.600000</td>
      <td>102.000000</td>
      <td>1998.000000</td>
      <td>4980.500000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>7.200000</td>
      <td>115.000000</td>
      <td>2005.000000</td>
      <td>15277.750000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>9.200000</td>
      <td>450.000000</td>
      <td>2011.000000</td>
      <td>619479.000000</td>
    </tr>
  </tbody>
</table>
</div>
      <button class="colab-df-convert" onclick="convertToInteractive('df-fb2b2cb6-1e6b-4987-b749-e3686830888f')"
              title="Convert this dataframe to an interactive table."
              style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
       width="24px">
    <path d="M0 0h24v24H0V0z" fill="none"/>
    <path d="M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z"/><path d="M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z"/>
  </svg>
      </button>

  <style>
    .colab-df-container {
      display:flex;
      flex-wrap:wrap;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

      <script>
        const buttonEl =
          document.querySelector('#df-fb2b2cb6-1e6b-4987-b749-e3686830888f button.colab-df-convert');
        buttonEl.style.display =
          google.colab.kernel.accessAllowed ? 'block' : 'none';

        async function convertToInteractive(key) {
          const element = document.querySelector('#df-fb2b2cb6-1e6b-4987-b749-e3686830888f');
          const dataTable =
            await google.colab.kernel.invokeFunction('convertToInteractive',
                                                     [key], {});
          if (!dataTable) return;

          const docLinkHtml = 'Like what you see? Visit the ' +
            '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
            + ' to learn more about interactive tables.';
          element.innerHTML = '';
          dataTable['output_type'] = 'display_data';
          await google.colab.output.renderOutput(dataTable, element);
          const docLink = document.createElement('div');
          docLink.innerHTML = docLinkHtml;
          element.appendChild(docLink);
        }
      </script>
    </div>
  </div>




__Marks = 1__

Do you see any quantity unusual. Better replace with NAN.


```python
#Your code here
data_Disc.replace({0: "NAN"})
```





  <div id="df-f28e03e8-512b-4f9b-976c-3b6de4e9caf5">
    <div class="colab-df-container">
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
      <th>score</th>
      <th>runtime</th>
      <th>year</th>
      <th>votes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>10000.000000</td>
      <td>10000.0</td>
      <td>10000.000000</td>
      <td>10000.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>6.386070</td>
      <td>103.5784</td>
      <td>1993.472800</td>
      <td>16604.012800</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1.189933</td>
      <td>26.628698</td>
      <td>14.829924</td>
      <td>34563.459698</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.500000</td>
      <td>NAN</td>
      <td>1950.000000</td>
      <td>1356.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>5.700000</td>
      <td>93.0</td>
      <td>1986.000000</td>
      <td>2333.750000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>6.600000</td>
      <td>102.0</td>
      <td>1998.000000</td>
      <td>4980.500000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>7.200000</td>
      <td>115.0</td>
      <td>2005.000000</td>
      <td>15277.750000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>9.200000</td>
      <td>450.0</td>
      <td>2011.000000</td>
      <td>619479.000000</td>
    </tr>
  </tbody>
</table>
</div>
      <button class="colab-df-convert" onclick="convertToInteractive('df-f28e03e8-512b-4f9b-976c-3b6de4e9caf5')"
              title="Convert this dataframe to an interactive table."
              style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
       width="24px">
    <path d="M0 0h24v24H0V0z" fill="none"/>
    <path d="M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z"/><path d="M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z"/>
  </svg>
      </button>

  <style>
    .colab-df-container {
      display:flex;
      flex-wrap:wrap;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

      <script>
        const buttonEl =
          document.querySelector('#df-f28e03e8-512b-4f9b-976c-3b6de4e9caf5 button.colab-df-convert');
        buttonEl.style.display =
          google.colab.kernel.accessAllowed ? 'block' : 'none';

        async function convertToInteractive(key) {
          const element = document.querySelector('#df-f28e03e8-512b-4f9b-976c-3b6de4e9caf5');
          const dataTable =
            await google.colab.kernel.invokeFunction('convertToInteractive',
                                                     [key], {});
          if (!dataTable) return;

          const docLinkHtml = 'Like what you see? Visit the ' +
            '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
            + ' to learn more about interactive tables.';
          element.innerHTML = '';
          dataTable['output_type'] = 'display_data';
          await google.colab.output.renderOutput(dataTable, element);
          const docLink = document.createElement('div');
          docLink.innerHTML = docLinkHtml;
          element.appendChild(docLink);
        }
      </script>
    </div>
  </div>




__Marks = 1__

Lets repeat describe to make sure that it is fine


```python
#Your code here
data_Disc = data[['score', 'runtime', 'year', 'votes']].describe()

data_Disc
```





  <div id="df-3b0459b7-a9b1-4558-828c-e8c58c913d70">
    <div class="colab-df-container">
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
      <th>score</th>
      <th>runtime</th>
      <th>year</th>
      <th>votes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>10000.000000</td>
      <td>10000.000000</td>
      <td>10000.000000</td>
      <td>10000.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>6.386070</td>
      <td>103.578400</td>
      <td>1993.472800</td>
      <td>16604.012800</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1.189933</td>
      <td>26.628698</td>
      <td>14.829924</td>
      <td>34563.459698</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.500000</td>
      <td>0.000000</td>
      <td>1950.000000</td>
      <td>1356.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>5.700000</td>
      <td>93.000000</td>
      <td>1986.000000</td>
      <td>2333.750000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>6.600000</td>
      <td>102.000000</td>
      <td>1998.000000</td>
      <td>4980.500000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>7.200000</td>
      <td>115.000000</td>
      <td>2005.000000</td>
      <td>15277.750000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>9.200000</td>
      <td>450.000000</td>
      <td>2011.000000</td>
      <td>619479.000000</td>
    </tr>
  </tbody>
</table>
</div>
      <button class="colab-df-convert" onclick="convertToInteractive('df-3b0459b7-a9b1-4558-828c-e8c58c913d70')"
              title="Convert this dataframe to an interactive table."
              style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
       width="24px">
    <path d="M0 0h24v24H0V0z" fill="none"/>
    <path d="M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z"/><path d="M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z"/>
  </svg>
      </button>

  <style>
    .colab-df-container {
      display:flex;
      flex-wrap:wrap;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

      <script>
        const buttonEl =
          document.querySelector('#df-3b0459b7-a9b1-4558-828c-e8c58c913d70 button.colab-df-convert');
        buttonEl.style.display =
          google.colab.kernel.accessAllowed ? 'block' : 'none';

        async function convertToInteractive(key) {
          const element = document.querySelector('#df-3b0459b7-a9b1-4558-828c-e8c58c913d70');
          const dataTable =
            await google.colab.kernel.invokeFunction('convertToInteractive',
                                                     [key], {});
          if (!dataTable) return;

          const docLinkHtml = 'Like what you see? Visit the ' +
            '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
            + ' to learn more about interactive tables.';
          element.innerHTML = '';
          dataTable['output_type'] = 'display_data';
          await google.colab.output.renderOutput(dataTable, element);
          const docLink = document.createElement('div');
          docLink.innerHTML = docLinkHtml;
          element.appendChild(docLink);
        }
      </script>
    </div>
  </div>




__Marks = 1__

### Basic plots

Lets draw histograms for release year, IMDB rating, runtime distribution


```python
#Your code here
data[['year']].plot.hist(bins = 20)
```




    <Axes: ylabel='Frequency'>




    
![png](SOL%20LAB%2004_files/SOL%20LAB%2004_37_1.png)
    


__Marks = 1__


```python
#Your code here
data[['score']].plot.hist(bins = 20)
```




    <Axes: ylabel='Frequency'>




    
![png](SOL%20LAB%2004_files/SOL%20LAB%2004_39_1.png)
    


__Marks = 1__


```python
#Your code here
data[['runtime']].plot.hist(bins = 20)
```




    <Axes: ylabel='Frequency'>




    
![png](SOL%20LAB%2004_files/SOL%20LAB%2004_41_1.png)
    


__Marks = 1__

Scatter plot between IMDB rating and years. Does it shows some trend?


```python
#Your code here
data.plot.scatter(x = 'year', y = 'score')

# It is hard to figure out a trend from this graph but we can say that Average Score Decreased over the years.
```




    <Axes: xlabel='year', ylabel='score'>




    
![png](SOL%20LAB%2004_files/SOL%20LAB%2004_44_1.png)
    


__Marks = 2__

Is there any relationship between IMDB rating and number of votes? Describe


```python
#Your code here
data.plot.scatter(x = "score", y = "votes")

# Higher Rated movies received more votes.
# Better the Movie, the More Votes it gets.
```




    <Axes: xlabel='score', ylabel='votes'>




    
![png](SOL%20LAB%2004_files/SOL%20LAB%2004_47_1.png)
    


__Marks = 2__

### Data aggregation/Summarization

*What genres are the most frequent?* Lay down the genres in descending order of count


```python
#Your code here
#sum sums over rows by default

freq_gens = data.iloc[:, 7:].sum(axis = 0).sort_values(ascending = False)

freq_gens

#Drama, Comedy and Triller are most Frequent Genres
```




    Drama         5697
    Comedy        3922
    Thriller      2832
    Romance       2441
    Action        1891
    Crime         1867
    Adventure     1313
    Horror        1215
    Mystery       1009
    Fantasy        916
    Sci-Fi         897
    Family         754
    War            512
    Biography      394
    Music          371
    History        358
    Animation      314
    Sport          288
    Musical        260
    Western        235
    Film-Noir       40
    Adult            9
    News             1
    Reality-TV       1
    dtype: int64



__Marks = 2__

Draw a bar plot to show top ten genres


```python
#Your code here
freq_gens[0:10].plot(kind="bar")
```




    <Axes: >




    
![png](SOL%20LAB%2004_files/SOL%20LAB%2004_54_1.png)
    


__Marks = 2__

*How many genres does a movie have, on average?*


```python
#Your code here
#axis=1 sums over columns instead

data['num_genres'] = data['genres'].astype(str).str.count('\|') + 1

average_num_genres = data['num_genres'].mean()

print("Average number of genres per movie:", average_num_genres)
```

    Average number of genres per movie: 2.7538


__Marks = 2__

## Explore Group Properties

Let's split up movies by decade. Find the decade mean score and draw a plot as follows:

<img src=/content/score-year-plot.png>


```python
#Your code here
data['decade'] = (data['year']//10) * 10
trend = data.groupby(['decade'])['score'].mean()
data.plot.scatter(x = 'year', y = 'score', color = 'k', alpha = 0.03)
plt.ylim(1, 10)
plt.xlim(1940, 2020)
plt.plot(trend, 'r-o' , label = "Decade Average")
plt.legend(loc="upper right")
```




    <matplotlib.legend.Legend at 0x7f6e340f7c40>




    
![png](SOL%20LAB%2004_files/SOL%20LAB%2004_61_1.png)
    


__Marks = 5__

Find the most popular movie each year



```python
#Your code here
sorted_movies = data.sort_values(['year', 'votes'], ascending=[True, False])
popular_movies = sorted_movies.groupby('year').first().reset_index()
plt.plot(popular_movies['year'], popular_movies['votes'], marker='o')
plt.xlabel('Year')
plt.ylabel('Votes')
plt.title('Most Popular Movie Each Year')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Display the names in a table
popular_movie_names = popular_movies[['year', 'title']]
popular_movie_names.columns = ['Year', 'Movie Title']
print(popular_movie_names.to_string(index=False))


```


    
![png](SOL%20LAB%2004_files/SOL%20LAB%2004_64_0.png)
    


     Year                                                          Movie Title
     1950                                                         Sunset Blvd.
     1951                                                 Strangers on a Train
     1952                                                  Singin' in the Rain
     1953                                                        Roman Holiday
     1954                                                          Rear Window
     1955                                                Rebel Without a Cause
     1956                                                        The Searchers
     1957                                                         12 Angry Men
     1958                                                              Vertigo
     1959                                                   North by Northwest
     1960                                                               Psycho
     1961                                               Breakfast at Tiffany's
     1962                                                To Kill a Mockingbird
     1963                                                     The Great Escape
     1964 Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb
     1965                                                   The Sound of Music
     1966                                       The Good, the Bad and the Ugly
     1967                                                         The Graduate
     1968                                                2001: A Space Odyssey
     1969                                   Butch Cassidy and the Sundance Kid
     1970                                                               Patton
     1971                                                   A Clockwork Orange
     1972                                                        The Godfather
     1973                                                         The Exorcist
     1974                                               The Godfather: Part II
     1975                                      One Flew Over the Cuckoo's Nest
     1976                                                          Taxi Driver
     1977                                   Star Wars: Episode IV - A New Hope
     1978                                                      The Deer Hunter
     1979                                                                Alien
     1980                       Star Wars: Episode V - The Empire Strikes Back
     1981                                              Raiders of the Lost Ark
     1982                                                         Blade Runner
     1983                           Star Wars: Episode VI - Return of the Jedi
     1984                                                       The Terminator
     1985                                                   Back to the Future
     1986                                                               Aliens
     1987                                                    Full Metal Jacket
     1988                                                             Die Hard
     1989                                   Indiana Jones and the Last Crusade
     1990                                                           Goodfellas
     1991                                             The Silence of the Lambs
     1992                                                       Reservoir Dogs
     1993                                                     Schindler's List
     1994                                             The Shawshank Redemption
     1995                                                                Se7en
     1996                                                                Fargo
     1997                                                              Titanic
     1998                                                  Saving Private Ryan
     1999                                                           Fight Club
     2000                                                            Gladiator
     2001                    The Lord of the Rings: The Fellowship of the Ring
     2002                                The Lord of the Rings: The Two Towers
     2003                        The Lord of the Rings: The Return of the King
     2004                                Eternal Sunshine of the Spotless Mind
     2005                                                        Batman Begins
     2006                                                         The Departed
     2007                                               No Country for Old Men
     2008                                                      The Dark Knight
     2009                                                               Avatar
     2010                                                            Inception
     2011                                                   X-Men: First Class


__Marks = 2__
