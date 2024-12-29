import pyspark
# Note we need pyspark.sql to get SparkSession
from pyspark.sql import SparkSession
from numpy import random

# Here is where we define the new parameters (Application Name and  
# spark.executor.instances Also, getOrCreate will add to the existing
spark = SparkSession.builder \
.appName("Pi Estimate Example") \
.config('spark.executor.instances', '4') \
.getOrCreate()
# Define/update the Spark context.
sc=spark.sparkContext

n=5000000
def sample(p):
    x, y = random.random(), random.random()
    return 1 if x*x + y*y < 1 else 0
# we could substitute "spark.sparkContext" for "sc" and it will work
count = sc.parallelize(range(0,n)).map(sample).reduce(lambda a, b: a + b)
print ("Pi is roughly %f" % (4.0 * count / n))

