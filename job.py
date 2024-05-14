from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder \
    .appName("PySparkShell") \
    .getOrCreate()

# Create a list of tuples
data = [("John", 25), ("Alice", 30), ("Bob", 35)]

# Create a DataFrame from the list of tuples
df = spark.createDataFrame(data, ["Name", "Age"])

# Show the DataFrame
df.show()