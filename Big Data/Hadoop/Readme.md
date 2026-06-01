Based on the provided resources, here are the comprehensive study notes on Big Data, Apache Hadoop, and Apache Spark.

---

## 1. Understanding Big Data

### What is Big Data?

* **Definition**: Big Data refers to extremely large, fast-growing, and complex datasets that cannot be efficiently stored or managed by traditional data management systems (like standard RDBMS).


* **Business Value**: When evaluated using modern tools, it provides organizations with actionable insights to improve business decision-making. For instance, Facebook collects vast volumes of user data to analyze and deliver a personalized News Feed.


* **Growth Scale**: Data volume is exploding, driven by social media, e-commerce, and tech giants. It is estimated that the global volume of digital data will reach 163 zettabytes by 2025.



### Types of Data

1. **Structured Data**: Follows a predefined schema or tabular format (e.g., Relational databases, Excel spreadsheets). Fields are discrete and easily sorted, searched, and joint-accessed.


2. **Semi-Structured Data**: A hybrid format that inherits some organizational properties but does not conform to a strict relational structure (e.g., XML, JSON, and Emails).


3. **Unstructured Data**: Information with no predefined conceptual format or schema, making it difficult for standard databases to analyze. It accounts for the majority of big data and includes video/audio files, mobile activity, log files, and satellite imagery.



### The 5 Vs of Big Data

* **Volume**: The massive size of data, typically reaching petabytes and exabytes, requiring advanced processing power beyond standard desktop CPUs.


* **Variety**: The varying formats and structural types of data collected from diverse sources (e.g., social logs, media files, databases).


* **Velocity**: The rapid speed at which new data is generated, accumulated, and needs to be processed or analyzed in real-time.


* **Value**: The reliability and usefulness of the data, focusing on turning raw data into meaningful business insights.


* **Veracity**: The trustworthiness, quality, and accuracy of the data, which requires checks and balances to handle messy data (like typos or abbreviations in tweets).



### Historical Architecture Shift

* **Legacy Bottleneck**: Early architecture relied on a single processor and a single storage unit. As data volume and variety grew, a single processor became too slow, and a single central storage unit created severe network overhead bottlenecks.


* **The Solution**: Distributed storage combined with parallel processing. Moving the computation algorithm close to where the data is physically stored minimizes network congestion and maximizes system throughput (**Data Locality**).



---

## 2. Apache Hadoop

### Framework Overview

* **Definition**: Apache Hadoop is an open-source software framework designed for distributed storage and large-scale parallel processing of datasets across clusters of commodity hardware.


* **Origin**: Created by Doug Cutting and Mike Cafarella in 2005. It was named after Doug's son's toy elephant.


* **Evolution**: Inspired by the Google File System (GFS) paper, which addressed Google's infrastructure challenge of handling billions of concurrent search queries and scaling out via cheap hardware.



### Core Modules & Components

Hadoop's architecture is divided into specialized storage, resource management, and processing layers:

| Component | Type | Module | Primary Role |
| --- | --- | --- | --- |
| **NameNode** | Master | HDFS | Manages file system metadata, directory structures, block maps, and replication factors. *Does not store actual user data*.
| **DataNode** | Slave | HDFS | Stores actual data blocks, handles read/write operations, and sends periodic heartbeats to the NameNode.|
| **JobTracker** | Master | MapReduce (v1) | Receives client jobs, splits work into tasks, schedules them on worker nodes, and tracks completion or failures.|
| **TaskTracker** | Slave | MapReduce (v1) | Accepts specific map/reduce tasks from the JobTracker and executes them locally on worker nodes. |
| **ResourceManager** | Master | YARN (v2) | Acts as the operating system for Hadoop 2.0; manages cluster resources and schedules jobs globally.|
| **NodeManager** | Slave | YARN (v2) | Monitors resource containers (RAM, CPU) on individual slave nodes and reports to the ResourceManager. |

### Hadoop Distributed File System (HDFS) Features

* **Block Allocation**: Files are broken down into logical, fixed-sized blocks (defaulting to 128 MB or similar chunks) and spread across multiple DataNodes.


* **Fault Tolerance**: Blocks are automatically replicated across different machines (default replication factor is 3) and distributed across server racks. If a chunk server or node crashes, the data remains accessible elsewhere.


* **Hardware Economy**: It is explicitly designed to run reliably on inexpensive, fault-prone commodity hardware.



---

## 3. MapReduce Programming Model

### Core Abstraction

MapReduce is the foundational parallel processing layer of Hadoop. It splits a large problem into a series of independent, isolated tasks that run concurrently across slaves.

1. **Map Phase**:
* Takes incoming data and automatically converts it into Key/Value $(k, v)$ pairs.


* Applies custom, user-defined business logic to every record.


* Outputs **intermediate outputs** stored on the local disk of the worker machine (not directly to HDFS).




2. **Shuffle and Sort Phase**:
* Triggered automatically after mappers finish.


* It physically moves data over the network (**Shuffle**), grouping and sorting all intermediate values associated with the exact same key (**Sort**) before handing them to the reducer.




3. **Reduce Phase**:
* Accepts the aggregated intermediate keys and value iterators.


* Executes custom aggregation, summation, or evaluation logic.


* Writes the **final output** pairs back to HDFS, triggering standard replication.





### Detailed Architectural Data Flow

```
[Input Data in HDFS]
       │
       ▼
  InputFormat  ──► Defines how files are split logically[cite: 3].
       │
       ▼
   InputSplits ──► Logical pointers to data; 1 InputSplit = 1 Map Task[cite: 3].
       │
       ▼
  RecordReader ──► Transforms physical splits into discrete (key, value) pairs[cite: 3].
       │
       ▼
     Mapper    ──► Processes user logic; creates intermediate data[cite: 3].
       │
       ▼
    Combiner   ──► Optional "Mini-Reducer" performing local in-node aggregation[cite: 3].
       │
       ▼
  Partitioner  ──► Routes keys to specific reducers if using >1 reducer[cite: 3].
       │
       ▼
 Shuffle & Sort──► Networks intermediate pairs across nodes; groups by key[cite: 3].
       │
       ▼
    Reducer    ──► Aggregates and yields final processed outputs[cite: 3].
       │
       ▼
  RecordWriter ──► Formats and writes data back to physical HDFS storage via OutputFormat[cite: 3].
       │
       ▼
[Final HDFS Output File]

```

### Critical MapReduce Operational Facts

* **Mappers vs. Reducers**: Clusters typically spawn significantly more mappers than reducers. Heavy, complex business logic is executed in parallel at the mapper level, leaving light aggregation work for the reducers.


* **Split vs. Block**: An HDFS block is a physical piece of data written to a disk. A MapReduce split is a logical view or pointer to data utilized by the processing framework. Developers cannot manually alter the number of mappers since it is directly dictated by the number of logical input splits.


* **Disabling Reducers**: Developers can completely disable the reduce phase by configuring the number of reducers to zero, turning it into a map-only job.


* **Language Support**: While the MapReduce framework itself is implemented natively in **Java**, any programming language (Python, R, Perl, Ruby) can be used via the **Hadoop Streaming API**.



---

## 4. Apache Spark vs. Apache Hadoop

### Spark Overview

* **Origin**: Started as a research project at the UC Berkeley AMPLab in 2009 and was open-sourced in early 2010.


* **Core Architecture**: Powered by **Spark Core**, which manages the base memory engine, and interfaces with various cluster schedulers like its Standalone Scheduler, YARN, or Mesos.



### Functional Feature Comparison

| Capability / Feature | Apache Hadoop  | Apache Spark |
| --- | --- | --- |
| **Primary Processing Style** | Batch Processing | Batch & Real-Time Processing |
| **Iterative Processing** | No (Inefficient disk writes)| Yes (In-Memory execution) |
| **Stream Processing** | ✘ Not Supported nativel| | ✔ Supported (Spark Streaming) |
| **Graph Processing** | ✘ Not Supported natively| ✔ Supported (GraphX module)|
| **Multi-Language Support** | Limited natively (uses Streaming API) | ✔ Native API support|
| **Machine Learning Layer** | ✘ None native | ✔ Integrated (MLlib module) |

### Ecosystem Modules in Spark

* **Spark SQL**: For managing structured data processing.


* **Spark Streaming**: For processing real-time streaming feeds.


* **MLlib**: A native, built-in machine learning library.


* **GraphX**: Optimized library for graph processing computation.



### Performance Insights

* **Running Time**: In iterative computing workflows (e.g., machine learning algorithms repeating over a dataset), Spark’s in-memory computing keeps running times flat and minimal as iterations increase, whereas Hadoop's overhead scales up exponentially due to constant disk write-backs.



---

## 5. Practical Implementation Examples (Scala / Spark API)

The provided source snippets highlight three common programmatic patterns used in Apache Spark:

### GraphX API (Vertex & Edge Relationships)

```scala
import org.apache.spark.graphx._

// Setting up patient nodes
val data1 = Seq((1L, "Patient_A"), (2L, "Patient_B"), (3L, "Patient_C"), (4L, "Patient_D"), (5L, "Patient_E"))
val vertex = sc.parallelize(data1)

// Mapping directed referral relationships
val data2 = Seq(Edge(1L, 2L, "Referral"), Edge(2L, 3L, "Referral"), Edge(3L, 4L, "Referral"), Edge(4L, 5L, "Referral"))
val egde = sc.parallelize(data2)

// Initializing the graph layout
val graph = Graph(vertex, egde, "nowhere")

```

### Spark SQL (DataFrames & SQL Queries)

```scala
import org.apache.spark.implicits._

val data = Seq(
  (1, "Laptop", "Electronics", "North", 85000),
  (2, "Mobile", "Electronics", "South", 45000),
  (3, "Chair", "Furniture", "East", 12000)
)
val salesDF = sc.parallelize(data).toDF("ProductID", "ProductName", "Category", "Region", "SalesAmount")
salesDF.createOrReplaceTempView("sales")

// Running relational aggregation queries directly on memory tables
val avgSales = spark.sql("SELECT Category, avg(SalesAmount) FROM sales GROUP BY Category")

```

### RDD Transformations & Partitioning Control

```scala
val data = Seq(("Aman", "Delhi", 32), ("Riya", "Mumbai", 28), ("Karan", "Delhi", 41))
val deliveryRDD = sc.parallelize(data, 4) // Initializes across 4 distinct partitions

// Transformation 1: Filter rows by conditional predicates
val filter1 = deliveryRDD.filter(x => x._3 >= 30)

// Transformation 2: Map structural schema changes 
val filter2 = deliveryRDD.map(x => (x._1, x._3))

// Partition Management
deliveryRDD.coalesce(2) // Decreases cluster partition footprint down to 2 for efficiency

```
