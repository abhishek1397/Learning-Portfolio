
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as spark_sum, round as spark_round

# Create Spark session
spark = SparkSession.builder \
    .appName("OnlineRetailAnalysis") \
    .getOrCreate()

# Read data from S3
s3_path = "s3://your-emr-bucket/online_retail.csv"
df = spark.read.option("header", "true").option("inferSchema", "true").csv(s3_path)

# Drop rows with missing key values
df_clean = df.dropna(subset=["InvoiceNo", "StockCode", "Description", "Quantity", "InvoiceDate", "UnitPrice", "Country"])

# Add TotalPrice column
df_enriched = df_clean.withColumn("TotalPrice", col("Quantity") * col("UnitPrice"))

# 1. Top 10 best-selling products
top_products = df_enriched.groupBy("Description") \
    .agg(spark_sum("Quantity").alias("TotalQuantity")) \
    .orderBy(col("TotalQuantity").desc())

top_products.show(10, truncate=False)

# 2. Total revenue per country
revenue_by_country = df_enriched.groupBy("Country") \
    .agg(spark_round(spark_sum("TotalPrice"), 2).alias("TotalRevenue")) \
    .orderBy(col("TotalRevenue").desc())

revenue_by_country.show(truncate=False)

# 3. High value transactions
high_value_txns = df_enriched.filter(col("TotalPrice") > 1000)
high_value_txns.select("InvoiceNo", "Quantity", "UnitPrice", "TotalPrice").show(5, truncate=False)

# Optionally write output back to S3
top_products.write.option("header", "true").csv("s3://your-emr-bucket/output/top-products/")
revenue_by_country.write.option("header", "true").csv("s3://your-emr-bucket/output/revenue-country/")
