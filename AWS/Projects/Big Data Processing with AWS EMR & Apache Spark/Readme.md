# 🚀 Big Data Processing with AWS EMR & PySpark

## 📌 Project Overview

This project demonstrates how to analyze a real-world retail dataset using **Apache Spark (PySpark)** on **Amazon EMR**. It uses Amazon S3 as data storage, EMR as the compute engine, and PySpark for distributed data transformation.

---

## 🛠️ Tools & Services Used

| Tool/Service     | Purpose                                  |
|------------------|-------------------------------------------|
| Amazon S3        | Store raw input and processed output data |
| Amazon EMR       | Run Spark job in a managed cluster        |
| Apache Spark     | Perform distributed data processing       |
| PySpark          | Spark programming in Python               |
| AWS CLI          | Manage resources via command line         |

---

## 📦 Dataset

**Online Retail Dataset**  
- Source: UCI Machine Learning Repository  
- Link: [UCI Retail Dataset](https://archive.ics.uci.edu/ml/datasets/Online+Retail)  
- Size: ~500 KB  
- Description: Invoices from a UK-based online retailer  
- Upload to S3:
  ```bash
  aws s3 cp online_retail.csv s3://your-emr-bucket/
