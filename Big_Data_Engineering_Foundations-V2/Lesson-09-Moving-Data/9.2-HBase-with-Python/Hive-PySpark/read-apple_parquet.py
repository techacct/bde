import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder \
.appName("Read Apple Parquet") \
.getOrCreate()

# Read parquet table into spark data frame (df_apple) from Hive warehouse in HDFS
df_apple=spark.read.parquet("hdfs://localhost:9000//user/hive/warehouse/apple_parquet")
df_apple.show(5)

