### Part 1: Introduction to Apache Spark

1. Start a Spark Session

`pyspark.sql` is a PySpark module that provides tools for working with structured data using DataFrames and SQL-like queries.

Start a Spark Session

```python
#  This initializes Spark and creates a session for DataFrame operations.
from pyspark.sql import SparkSession

# Start Spark
#  This initializes Spark and creates a session for DataFrame operations.
spark = SparkSession.builder.appName("Biostats Analysis").getOrCreate()

# Load CSV file
#  Reads a CSV file into a Spark DataFrame with inferred schema.
df = spark.read.csv("Biostats.csv", header=True, inferSchema=True)

# View first rows
#  Displays the top rows of the DataFrame.
df.show(5)
```

2. Explore schema

```python
#  Shows the structure of the DataFrame including column types.
df.printSchema()
```

3. Select Columns

```python
#  Displays the top rows of the DataFrame.
df.select("Name", "Age", "Sex").show()
```

4. Filter: People older than 40

```python
#  Displays the top rows of the DataFrame.
df.filter(df["Age"] > 40).show()
```

5. Sort by Weight descending order.

```python
#  Displays the top rows of the DataFrame.
df.orderBy(df["Weight(lbs)"].desc()).show()
```

6. Group by Sex and Count

```python
#  Displays the top rows of the DataFrame.
df.groupBy("Sex").count().show()
```

7. Average Weight by Sex

```python
#  Displays the top rows of the DataFrame.
df.groupBy("Sex").avg("Weight(lbs)").show()

```

8. Before running SQL queries, register the DataFrame as a temporary view. Now you can query it like a regular SQL table.

```python
#  Registers the DataFrame as a temporary SQL view.
df.createOrReplaceTempView("biostats")
```

9.  Select Name, Age, Sex

```python
#  Displays the top rows of the DataFrame.
spark.sql("SELECT Name, Age, Sex FROM biostats").show()
```

10. Filter: People older than 40

```python
#  Displays the top rows of the DataFrame.
spark.sql("SELECT * FROM biostats WHERE Age > 40").show()
```

---

### Part 2: Data cleaning with Spark

1. Load the CSV

```python
#  This initializes Spark and creates a session for DataFrame operations.
from pyspark.sql import SparkSession

#  This initializes Spark and creates a session for DataFrame operations.
spark = SparkSession.builder.appName("DataFrameMapReduce").getOrCreate()
#  Reads a CSV file into a Spark DataFrame with inferred schema.
df = spark.read.csv("Movies.csv", header=True, inferSchema=True)
```

2. Clean the data

```python
#  Executes a SQL query on the registered temporary view.
from pyspark.sql.functions import lower, trim

df = df.withColumn("Genre_clean", trim(lower(df["Genre"])))

#  Executes a SQL query on the registered temporary view.
from pyspark.sql.functions import when

df = df.withColumn(
    "Genre_fixed",
    when(df["Genre_clean"] == "comdy", "comedy")
    .when(df["Genre_clean"] == "romence", "romance")
    .when(df["Genre_clean"] == "romance", "romance")
    .when(df["Genre_clean"] == "comedy", "comedy")
    .when(df["Genre_clean"] == "action", "action")
    .when(df["Genre_clean"] == "drama", "drama")
    .when(df["Genre_clean"] == "animation", "animation")
    .when(df["Genre_clean"] == "fantasy", "fantasy")
    .otherwise(df["Genre_clean"])
)
```

3. Run the map reduce process

```python
#  Displays the top rows of the DataFrame.
df.groupBy("Genre_clean").count().show()
```

4. Group in ascending order

```python
#  Displays the top rows of the DataFrame.
df.groupBy("Genre_fixed").count().orderBy("count", ascending=False).show()
```

5. Save as CSV

```python
#  Sorts the DataFrame by specified column(s).
genre_counts = df.groupBy("Genre_fixed").count().orderBy("count", ascending=False)
genre_counts.write.csv("output", header=True, mode="overwrite")
```

6. Load the movies file

```python
#  This initializes Spark and creates a session for DataFrame operations.
from pyspark.sql import SparkSession

#  This initializes Spark and creates a session for DataFrame operations.
spark = SparkSession.builder.appName("MoviesCleaning").getOrCreate()
#  Reads a CSV file into a Spark DataFrame with inferred schema.
df = spark.read.csv("Movies.csv", header=True, inferSchema=True)
#  Shows the structure of the DataFrame including column types.
df.printSchema()

```

7. Drop rows with missing key fields

```python
df = df.dropna(subset=["Film", "Genre", "Audience score %", "Profitability"])
```

8. Clean and standardize names

```python
#  Executes a SQL query on the registered temporary view.
from pyspark.sql.functions import trim, lower, when, col

# Create cleaned genre
df = df.withColumn("Genre_clean", trim(lower(col("Genre"))))

# Fix typos
df = df.withColumn("Genre_fixed",
    when(col("Genre_clean") == "comdy", "comedy")
    .when(col("Genre_clean") == "romence", "romance")
    .otherwise(col("Genre_clean"))
)
```

9. Clean and convert Worldwide Gross to numeric

```python
#  Executes a SQL query on the registered temporary view.
from pyspark.sql.functions import regexp_replace

df = df.withColumn("Worldwide_Gross_Clean",
    regexp_replace("Worldwide Gross", "[$,]", "").cast("float")
)
```

10. Convert to data types

```python
df = df.withColumn("Profitability", col("Profitability").cast("float"))
df = df.withColumn("Audience_Score", col("Audience score %").cast("float"))
```

11. Drop duplicated

```python
df = df.dropDuplicates(["Film", "Year"])
```

12. Check final schema

```python
#  Shows the structure of the DataFrame including column types.
df.printSchema()
#  Displays the top rows of the DataFrame.
df.select("Film", "Genre_fixed", "Audience_Score", "Profitability", "Worldwide_Gross_Clean").show(5)

```

13. Save to a new directory with a single CSV file

```python
df.coalesce(1).write.csv("cleaned_movies_output", header=True, mode="overwrite")
```

---

### Part 3: Exercises

1. Show the first 5 records

* Question: Display the first five rows of the dataset.

💡  Hint: Use .show(5) after reading the CSV with spark.read.csv().

2. Display the schema of the dataset

* Question: What are the data types of each column?

💡   Hint: Use .printSchema() to inspect structure and types.

3. Count how many startups are from each country

* Question: Find the number of unicorns per country.

💡   Hint: Use groupBy("Country").count() and sort with .orderBy(...).

4. What are the top 10 most valuable startups?

* Question: List the 10 companies with the highest valuation.

💡   Hint: Make sure Valuation is numeric → use .cast("float"), then .orderBy(...).

5. Filter all startups in the Fintech industry

* Question: Find all rows where the industry is “Fintech”.

💡   Hint: Use .filter(col("Industry") == "Fintech").

6. Count how many unicorns each city has

* Question: Group by City and count the number of entries.

💡   Hint: groupBy("City").count() — sort to see top cities.

7. Count how many unicorns were founded each year

* Question: Count unicorns per year from the Date column.

💡  Hint: Use to_date("Date", "M/d/yyyy"), Extract year() to a new column, Group and count by Year

8. What’s the average valuation per industry?

* Question: Calculate and rank average startup valuation by industry.

💡 Hint: Cast Valuation to float, Use groupBy("Industry").avg(...), Order by the result

9. Create a new column to flag U.S. startups

* Question: Add a column Is_USA to mark startups from the U.S.

💡   Hint: Use withColumn("Is_USA", col("Country") == "United States")

10. Save the cleaned DataFrame to a CSV file
* Question: Write the cleaned and transformed DataFrame to disk.

💡   Hint: Use coalesce(1).write.csv(..., header=True, mode="overwrite")

----

### Part 3: Exercises solutions (`Python`)

Download the following data: https://www.kaggle.com/datasets/uzairrehman/world-wide-unicorn-startups

1. Load the dataset

```python
#  This initializes Spark and creates a session for DataFrame operations.
from pyspark.sql import SparkSession
#  This initializes Spark and creates a session for DataFrame operations.
spark = SparkSession.builder.appName("Unicorns").getOrCreate()

#  Reads a CSV file into a Spark DataFrame with inferred schema.
df = spark.read.csv("World_Wide_Unicorn_Startups.csv", header=True, inferSchema=True)
```

2. Show the first 5 records

```python
#  Displays the top rows of the DataFrame.
df.show(5)
```

3. Show the schema of the DataFrame

```python
#  Shows the structure of the DataFrame including column types.
df.printSchema()
```

4. Count how many startups are from each country

```python
#  Displays the top rows of the DataFrame.
df.groupBy("Country").count().orderBy("count", ascending=False).show()
```

5. Find the top 10 most valuable startups

```python
#  Displays the top rows of the DataFrame.
df.orderBy(df["Valuation"].desc()).select("Company", "Valuation").show(10)
```

6. Filter all startups in the Fintech industry

```python
#  Displays the top rows of the DataFrame.
df.filter(df["Industry"] == "Fintech").show()
```

7. Count how many unicorns each city has

```python
import time

s = time.time()

#  Sorts the DataFrame by specified column(s).
df.groupBy("City").count().orderBy("count", ascending=False)

print(time.time()-s)

s = time.time()

#  Displays the top rows of the DataFrame.
df.groupBy("City").count().orderBy("count", ascending=False).show(10)

print(time.time()-s)

```

8. Count unicorns per year

```python
#  Executes a SQL query on the registered temporary view.
from pyspark.sql.functions import to_date

df = df.withColumn("ParsedDate", to_date("Date", "M/d/yyyy"))

#  Executes a SQL query on the registered temporary view.
from pyspark.sql.functions import year

df = df.withColumn("Year", year("ParsedDate"))

#  Displays the top rows of the DataFrame.
df.groupBy("Year").count().orderBy("Year").show()
```

9. Average valuation per industry

```python
df = df.withColumn("Valuation_numeric", col("Valuation").cast("float"))

df.groupBy("Industry") \
  .avg("Valuation_numeric") \
#  Sorts the DataFrame by specified column(s).
  .orderBy("avg(Valuation_numeric)", ascending=False) \
#  Displays the top rows of the DataFrame.
  .show()
```

10.  Create a new column Is_USA to check if company is from United States

```python
#  Executes a SQL query on the registered temporary view.
from pyspark.sql.functions import col

df = df.withColumn("Is_USA", col("Country") == "United States")
#  Displays the top rows of the DataFrame.
df.select("Company", "Country", "Is_USA").show(5)

```

11. Save the cleaned and enriched dataset to CSV

```python
df.coalesce(1).write.csv("unicorns_cleaned.csv", header=True, mode="overwrite")
```

---

### Part 3: Solutions in Spark (`SQL`)

1. Setup

```python
#  This initializes Spark and creates a session for DataFrame operations.
from pyspark.sql import SparkSession
#  Executes a SQL query on the registered temporary view.
from pyspark.sql.functions import to_date, year, col

#  This initializes Spark and creates a session for DataFrame operations.
spark = SparkSession.builder.appName("Unicorns").getOrCreate()

# Load and prepare
#  Reads a CSV file into a Spark DataFrame with inferred schema.
df = spark.read.csv("World_Wide_Unicorn_Startups.csv", header=True, inferSchema=True)

# Parse date and cast valuation
df = df.withColumn("ParsedDate", to_date("Date", "M/d/yyyy"))
df = df.withColumn("Year", year("ParsedDate"))
df = df.withColumn("Valuation_numeric", col("Valuation").cast("float"))

# Register SQL view
#  Registers the DataFrame as a temporary SQL view.
df.createOrReplaceTempView("unicorns")

```

2. Show the first 5 records

```python
#  Displays the top rows of the DataFrame.
spark.sql("SELECT * FROM unicorns LIMIT 5").show()
```

3. Show the schema

```python
#  Shows the structure of the DataFrame including column types.
df.printSchema()

```

4. Count startups per country

```python
#  Executes a SQL query on the registered temporary view.
spark.sql("""
SELECT Country, COUNT(*) AS num_startups
FROM unicorns
GROUP BY Country
ORDER BY num_startups DESC
#  Displays the top rows of the DataFrame.
""").show()

```

5. Top 10 most valuable startups

```python
#  Executes a SQL query on the registered temporary view.
spark.sql("""
SELECT Company, Valuation_numeric
FROM unicorns
ORDER BY Valuation_numeric DESC
LIMIT 10
#  Displays the top rows of the DataFrame.
""").show()

```

6. Filter startups in Fintech industry

```python
#  Executes a SQL query on the registered temporary view.
spark.sql("""
SELECT *
FROM unicorns
WHERE Industry = 'Fintech'
#  Displays the top rows of the DataFrame.
""").show()

```

7. Count startups per city

```python
#  Executes a SQL query on the registered temporary view.
spark.sql("""
SELECT City, COUNT(*) AS count
FROM unicorns
GROUP BY City
ORDER BY count DESC
LIMIT 10
#  Displays the top rows of the DataFrame.
""").show()

```

8. Count unicorns per year

```python
#  Executes a SQL query on the registered temporary view.
spark.sql("""
SELECT Year, COUNT(*) AS count
FROM unicorns
GROUP BY Year
ORDER BY Year
#  Displays the top rows of the DataFrame.
""").show()

```

9. Average valuation per industry

```python
#  Executes a SQL query on the registered temporary view.
spark.sql("""
SELECT Industry, AVG(Valuation_numeric) AS avg_valuation
FROM unicorns
GROUP BY Industry
ORDER BY avg_valuation DESC
#  Displays the top rows of the DataFrame.
""").show()
```

10. Create Is_USA flag

```python
#  Executes a SQL query on the registered temporary view.
spark.sql("""
SELECT Company, Country,
       CASE WHEN Country = 'United States' THEN TRUE ELSE FALSE END AS Is_USA
FROM unicorns
#  Displays the top rows of the DataFrame.
""").show(5)
```