import pyspark
# Note we need pyspark.sql to get SparkSession
from pyspark.sql import SparkSession
from pyspark.context import SparkContext

sc = SparkContext('local')
spark = SparkSession(sc)


# spark= SparkSession.builder.appName("Hive-test").enableHiveSupport().getOrCreate()
# spark= SparkSession.builder.appName("Hive-test").getOrCreate()
sqlContext = spark.builder.enableHiveSupport().getOrCreate()
for x in spark.sparkContext.getConf().getAll(): print (x)

df_csv = spark.read.options(header='True').csv("hdfs://localhost:9000/user/hands-on/CSV-Files/names.csv")

df_csv.show(5)

df_csv.write.mode("overwrite").saveAsTable("names")

