# Technical Notes: Running WordCount MapReduce in Apache Hadoop

This document outlines the standard procedure for starting a single-node Hadoop cluster, preparing input files, executing the MapReduce WordCount example, and verifying the output.

## 1. Initializing the Hadoop Cluster

Before running any MapReduce job, the underlying storage (HDFS) and resource management (YARN) daemons must be active.

```bash
# Start the SSH service (required for Hadoop scripts to connect to nodes)
sudo service ssh start

# Start HDFS daemons (NameNode, DataNode)
start-dfs.sh

# Start YARN daemons (ResourceManager, NodeManager)
start-yarn.sh

# Verify all Java processes are running successfully
jps

```

*Expected `jps` output should include: NameNode, DataNode, SecondaryNameNode, ResourceManager, NodeManager, and Jps.*

---

## 2. Preparing Input Data in HDFS

Hadoop MapReduce operates on data stored in the distributed filesystem, not the local Linux directory.

```bash
# Create and edit a local text file with sample words
nano wordcount.txt

# Create a designated input directory structure in HDFS
hdfs dfs -mkdir -p /user/wordcount/

# Upload the local text file into the HDFS directory
hdfs dfs -put wordcount.txt /user/wordcount/

# Verify that the file exists in HDFS
hdfs dfs -ls /user/wordcount/

```

---

## 3. Executing the MapReduce WordCount Job

Navigate to the Hadoop installation directory to run the pre-compiled examples archive.

```bash
# Change directory to your Hadoop installation folder
cd hadoop

# Execute the MapReduce WordCount job
./bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.6.jar wordcount /user/wordcount/wordcount.txt /user/wordcount/output/

```

> ⚠️ **Note on Output Directories:** YARN requires that the output directory (`/user/wordcount/output/`) **does not exist** prior to execution. Hadoop creates this directory automatically to prevent accidental data overwrites.

---

## 4. Verifying and Viewing Output Results

### Method A: Via Command Line Interface (CLI)

Once the MapReduce console logs display a successful 100% completion status, inspect the output path.

```bash
# List the generated files in the output directory
hdfs dfs -ls /user/wordcount/output

# View the final calculated word counts
hdfs dfs -cat /user/wordcount/output/part-r-00000

```

### Method B: Via Web Utilities (HDFS Utilities UI)

Alternatively, you can monitor and track the generated files visually through a web browser.

* **URL:** `http://localhost:9870/explorer.html#/user/wordcount/output`
* The directory will contain two key items:
* `_SUCCESS`: A 0-byte file indicating the MapReduce task completed without errors.
* `part-r-00000`: The actual text file holding the final reduction results sorted alphabetically.
