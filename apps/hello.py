from pyspark.sql import SparkSession
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# spark = SparkSession.builder \
#     .appName("HelloWorld") \
#     .getOrCreate()
    
logging.info("Starting Spark session...")
# spark = SparkSession.builder.remote("sc://spark-connect:15002").appName("HelloWorld").getOrCreate()
spark = SparkSession.builder.remote("sc://localhost:15002").appName("HelloWorld").getOrCreate()

logging.info("Spark session started.")

spark.stop()