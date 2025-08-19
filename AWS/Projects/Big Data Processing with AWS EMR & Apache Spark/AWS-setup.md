# 🚀 Big Data Processing with AWS EMR & PySpark

## 📌 Project Overview

This project demonstrates how to process and analyze large datasets using **Apache Spark (PySpark)** on **Amazon EMR**, AWS’s managed big data platform. The input data is stored in **Amazon S3**, processed on a distributed Spark cluster, and key business insights are derived using PySpark transformations and aggregations.

---

## 🧰 Tools & Technologies

| Tool / Service        | Purpose                                                |
|-----------------------|--------------------------------------------------------|
| **Amazon S3**         | Store input dataset and Spark output                   |
| **Amazon EMR**        | Scalable cluster for running PySpark jobs              |
| **PySpark**           | Data processing engine for large-scale analytics       |
| **AWS CLI**           | Command-line interaction with AWS services             |
| **EC2 Key Pair**      | SSH into EMR master node for job execution             |

---

## 🎯 Use Case

Analyze retail transaction data to:
- Identify best-selling products
- Calculate revenue per country
- Detect high-value transactions

---

## 📁 Dataset Used

**Dataset:** [UCI Online Retail Dataset](https://archive.ics.uci.edu/ml/datasets/Online+Retail)  
**Converted to CSV** and uploaded to S3.  
> 💡 _Lightweight (~500KB), real-world e-commerce transactions dataset. Minimal AWS cost._

---

## 🪜 Step-by-Step Guide

### ✅ 1. Set Up AWS CLI and S3

```bash
# Configure AWS CLI
aws configure

# Create an S3 bucket to store the dataset and output
aws s3 mb s3://your-emr-bucket

# Upload dataset (after converting to CSV from Excel)
aws s3 cp online_retail.csv s3://your-emr-bucket/
````

---

### ✅ 2. Launch an EMR Cluster (PySpark Enabled)

#### Option A: Using AWS CLI

```bash
aws emr create-cluster \
--name "PySparkCluster" \
--release-label emr-6.7.0 \
--applications Name=Spark \
--instance-type m5.xlarge \
--instance-count 3 \
--use-default-roles \
--ec2-attributes KeyName=your-key
```

#### Option B: Using AWS Console

* Go to **EMR > Create cluster**
* Choose **Spark** as application
* Select **m5.xlarge** as instance type
* Use 3 instances (1 master, 2 core)
* Attach your EC2 **key pair**
* Launch the cluster

---

### ✅ 3. Connect to EMR Master Node

Once the cluster is running:

```bash
ssh -i your-key.pem hadoop@<master-node-public-dns>
```

---

### ✅ 4. Run PySpark Job

Launch PySpark:

```bash
pyspark
```

Paste and run pyspark code:
[Pyspark code](https://github.com/abhishek1397/AWS/blob/main/Big%20Data%20Processing%20with%20AWS%20EMR%20%26%20Apache%20Spark/spark_analysis.py)


### ✅ 5. Terminate the EMR Cluster (Cost-Saving)

Once done, terminate the cluster:

```bash
aws emr terminate-clusters --cluster-ids j-XXXXXXXXXXXXX
```

---

## 📈 Outcomes

* ✅ Processed large data on a distributed cluster with PySpark
* ✅ Derived top-selling products and revenue insights by region
* ✅ Identified high-value transactions
* ✅ Saved output back to S3 for future use or BI visualization

---

## 💰 Cost Optimization Tips

| Strategy                          | Description                     |
| --------------------------------- | ------------------------------- |
| Use `m5.xlarge` or `t2.medium`    | Lower-cost EC2 instances        |
| Use **Spot Instances** (optional) | Cheaper than on-demand          |
| Terminate EMR ASAP                | Avoid idle charges              |
| Use small dataset (\~500KB)       | Lower storage and compute costs |

---

## 🧠 Learnings

* How to create and manage EMR clusters
* Executing PySpark jobs on AWS infrastructure
* Reading and writing data from Amazon S3
* Aggregation and filtering using PySpark DataFrames

## 🔗 Resources

* [Amazon EMR Docs](https://docs.aws.amazon.com/emr/)
* [PySpark API Docs](https://spark.apache.org/docs/latest/api/python/)
* [UCI Online Retail Dataset](https://archive.ics.uci.edu/ml/datasets/Online+Retail)
* [AWS CLI Reference](https://docs.aws.amazon.com/cli/latest/index.html)

---

