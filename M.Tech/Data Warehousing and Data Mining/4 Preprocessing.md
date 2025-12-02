# **I. Why Preprocess Data?**

**The Problem: "Dirty" Data**
Real-world data is often imperfect and unsuitable for immediate mining due to three main issues:
*   **Incomplete:** Lacking attribute values or attributes of interest, or containing only aggregate data (e.g., missing customer income),.
*   **Noisy:** Containing errors, outliers, or random variance (e.g., a salary of 1,000,000 in a dataset of average earners),.
*   **Inconsistent:** Containing discrepancies in codes or names (e.g., "New York" vs. "NY", or "Male/Female" vs. "M/F"),.

**The Goal**
*   **Data Quality:** High-quality mining results rely on high-quality data.
*   **Warehousing:** Data warehouses require the consistent integration of clean data.

---

### **II. Task 1: Data Cleaning**

**1. Handling Missing Data**
When data is not available due to equipment failure, inconsistency, or misunderstanding, several strategies can be used:
*   **Ignore the Tuple (Row):** Delete the row. This is commonly done if the **class label** is missing in classification tasks. However, it is **ineffective** if the dataset is small or if missing values affect many different attributes, as it discards too much useful data,,.
*   **Fill in Manually:** Accurate but tedious and impractical for large datasets.
*   **Global Constant:** Replace with a value like "Unknown" (may create a fake "new" class).
*   **Attribute Mean:** Replace with the average value of that attribute across the whole dataset.
*   **Class-Specific Mean:** The smartest statistical approach. Replace with the mean of the attribute *belonging to the same class* (e.g., if a customer bought a product, replace their missing age with the average age of other buyers, not non-buyers),.

**2. Handling Noisy Data (Smoothing)**
Noise is random error or variance (e.g., faulty sensors, typos). Techniques to smooth data include,:
*   **Binning:** A local smoothing method.
    *   **Step 1:** Sort data and partition into bins (buckets).
    *   **Step 2:** Smooth values using:
        *   *Bin Means:* Replace values with the average of the bin,.
        *   *Bin Medians:* Replace values with the median of the bin,.
        *   *Bin Boundaries:* Replace values with the closest boundary (min or max) of the bin,.
*   **Clustering:** Grouping similar points to detect and remove outliers (points that fall outside clusters),.
*   **Regression:** Fitting data to a function (linear or multiple regression) to smooth values toward the trend line,.
*   **Inspection:** A mix of automated detection and human verification.

**3. Commercial Cleaning Tools**
*   **Data Scrubbing:** Uses domain knowledge (e.g., spell-checking, address formatting). Tools: *OpenRefine*, *Trifacta*,.
*   **Data Auditing:** Analyzes data to find rule violations (e.g., Age < 0). Tools: *Informatica Data Quality*, *Talend*.

---

### **III. Task 2: Data Integration**

This involves combining data from multiple sources (databases, files, cubes) into a coherent store.

**Key Challenges**
*   **Entity Identification Problem:** Matching equivalent entities across sources (e.g., is `cust_id` in Database A the same as `cust_#` in Database B?).
*   **Data Value Conflicts:** Attributes may differ due to representation (e.g., date formats) or scaling (e.g., metric vs. British units).
*   **Redundancy:**
    *   Attributes may be derived from others (e.g., "Annual Revenue" might be redundant if "Monthly Revenue" exists).
    *   **Correlation Analysis** can detect these redundancies to improve mining speed.

---

### **IV. Task 3: Data Transformation**

Converting data into forms appropriate for mining.

**Normalization**
Scaling data to fall within a specific small range (e.g., 0.0 to 1.0).
*   **Min-Max Normalization:** Linearly transforms data to a new range.
*   **Z-Score Normalization:** Uses mean and standard deviation (useful when min/max are unknown or outliers exist).
*   **Decimal Scaling:** Moves the decimal point based on the maximum absolute value.

---

### **V. Task 4: Data Reduction**

Reducing data volume while maintaining analytical quality.

**Strategies**
*   **Data Cube Aggregation:** Summarizing data at higher conceptual levels (e.g., aggregating daily sales into monthly sales). The lowest level is the "base cuboid"; the highest is the "apex".
*   **Dimensionality Reduction:** Removing irrelevant attributes.
    *   **Decision Trees:** A supervised method that identifies the most valuable attributes for classification (nodes) and discards the rest,.
*   **Data Compression:**
    *   **Lossless:** Original data can be reconstructed perfectly (e.g., Huffman coding).
    *   **Lossy:** Some detail is discarded for higher compression (e.g., JPEG, Wavelet transforms),.
*   **Numerosity Reduction:** Replacing data with a model.
    *   **Regression:** Modeling a variable ($Y$) as a linear function of another ($X$) or multiple variables ($X_1, X_2...$),.
    *   **Log-Linear Models:** Approximating multidimensional probability distributions,.
    *   **Histograms:** Dividing data into buckets and storing the sum/average.

| Type                             | Examples / Notes                                       |
| -------------------------------- | ------------------------------------------------------ |
| **Data Cube Aggregation**        | Summarization across hierarchical levels (base → apex) |
| **Dimensionality Reduction**     | PCA, SVD                                               |
| **Numerosity Reduction**         | Sampling, regression, clustering                       |
| **Discretization**               | Convert numeric → categorical                          |
| **Concept Hierarchy Generation** | Convert low-level details → higher-level concepts      |
|                                  |                                                        |


---

### **VI. Discretization and Concept Hierarchies**

**Discretization**
Converting continuous attributes (real numbers) into intervals (categorical labels). This is a form of data reduction useful because some algorithms only accept categorical data.

**Concept Hierarchy**
Organizing data from low-level concepts to high-level concepts to summarize data.
*   **Example:** Age (25) $\rightarrow$ Range (20-30) $\rightarrow$ Concept (Young Adult).
*   **Automatic Generation:** Hierarchies can be generated based on the count of distinct values. The attribute with the **most distinct values** (e.g., street name) is placed at the lowest level, while attributes with fewer values (e.g., country) are at the top.

---

### **Analogy: Data Preprocessing as Cooking**

To understand the workflow, imagine you are **preparing a gourmet meal**:

*   **Data Cleaning (Washing/Trimming):** You don't cook vegetables with dirt on them. You wash them (clean noise), cut off the rotten parts (outliers), or if a recipe calls for 3 eggs and you only have 2, you might borrow one or adjust the recipe (handling missing values).
*   **Data Integration (Mixing Ingredients):** You take onions from the pantry and carrots from the fridge (different sources). You have to ensure you aren't using "cups" of sugar in one bowl and "grams" in another (resolving unit conflicts).
*   **Data Transformation (Marinating/Slicing):** You might chop everything into uniform sizes (normalization) so they cook evenly.
*   **Data Reduction (Reducing a Sauce):** You simmer a large pot of liquid until it becomes a concentrated, flavorful sauce. It’s smaller in volume but keeps the essential flavor (analytical value).
*   **Discretization (Categorizing):** Instead of serving "43 peas," you just serve a "scoop." You group specific numbers into a general serving size.
