from pyspark.sql import SparkSession

table_name = 'DelayedFlights4'
spark = SparkSession.builder.appName("Spark Assignment").getOrCreate()
df = spark.read.format("csv").option("header", "true").load("s3://mapreduce-assignment/input/DelayedFlights-updated.csv")
df.write.mode("overwrite").saveAsTable(table_name)

for i in range(0, 5):
    result = spark.sql(f"SELECT Year, avg((CarrierDelay /ArrDelay)*100) from {table_name} GROUP BY Year").show()
    result = spark.sql(f"SELECT Year, avg((NASDelay /ArrDelay)*100) from {table_name} GROUP BY Year").show()
    result = spark.sql(f"SELECT Year, avg((WeatherDelay /ArrDelay)*100) from {table_name} GROUP BY Year").show()
    result = spark.sql(f"SELECT Year, avg((LateAircraftDelay /ArrDelay)*100) from {table_name} GROUP BY Year").show()
    result = spark.sql(f"SELECT Year, avg((SecurityDelay /ArrDelay)*100) from {table_name} GROUP BY Year").show()