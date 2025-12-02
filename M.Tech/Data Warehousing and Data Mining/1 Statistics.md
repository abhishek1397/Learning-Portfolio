## **I. Data Structure and Types**

**Data Objects**
*   **Definition:** A data object represents an entity (e.g., a customer, patient, or student),.
*   **Synonyms:** Also referred to as samples, examples, instances, data points, objects, or tuples.
*   **Database Structure:** In a database,
    *   rows -> data objects
    *   columns -> attributes.

**Types of Data Sets**
*   **Record Data:**
    *   Structured rows and columns  
    *   Includes Relational records, data matrices (numerical matrix, crosstabs), document data (text), and transaction data.
      
*   **Graph and Network Data:**
    *   Entities connected by relationships  
    *   Includes World Wide Web data, social/information networks, and molecular structures.
      
*   **Ordered Data:**
    *   Data with sequence or time ordering   
    *   Includes video (sequence of images), temporal (time-series), sequential (transaction sequences), and genetic sequences.
      
*   **Spatial/Multimedia:**
    *  Representation using location or media objects   
    *   Includes maps, image data, and video data.

---

### **II. Attributes (Variables)**

An **attribute** (also called a **dimension, feature, or variable**) is a data field representing a characteristic of a data object (e.g., customer_ID, name, address).

**1. Categorical Attributes**
*   **Nominal:**
    *   Represents categories, states, or "names of things" without an inherent order
    *   (e.g., hair color, occupation, zip codes).
      
*   **Binary:**
    *   A special nominal attribute with only two states (0 or 1).
      *   **Symmetric:** Both outcomes are equally important (e.g., gender).
      *   **Asymmetric:** Outcomes are not equally important (e.g., a medical test where "positive" is rare and critical). Convention assigns 1 to the most important outcome.
        
*   **Ordinal:**
    *   Values have a meaningful order or ranking, but the magnitude of difference between them is unknown
    *   (e.g., drink sizes like small/medium/large, army rankings, grades).

**2. Numeric Attributes**
*   **Interval-Scaled:**
    *   measured on a scale of equal-sized units where values have order.
    *   **Key Feature:** No true zero-point. A value of "0" does not mean "none" (e.g., 0°C is the freezing point of water, not the absence of temperature; Year 0 is a point in time, not no time).

*   **Ratio-Scaled:**
    *   Possesses an **inherent zero-point** where 0 means "none" (e.g., 0 length, 0 money).
    *   Allows for comparison of magnitude (e.g., 10K is twice as hot as 5K).

**3. Discrete vs. Continuous**
*   **Discrete:**
    *   Finite or countably infinite set of values
    *   (e.g., zip codes, word counts). Often integers. Binary attributes are a special type of discrete attribute.

*   **Continuous:**
    *   Real numbers represented (practically) by floating-point variables
    *   (e.g., temperature, height, weight),.

---

### **III. Statistical Descriptions of Data**

The goal of basic statistics is to understand **central tendency**, **variation**, and **spread**.

**Measuring Central Tendency**
*   **Mean:** The algebraic average.
    *   **Weighted Arithmetic Mean:** Assigns weights to values.
    *   **Trimmed Mean:** Calculates the average after chopping off extreme values to avoid distortion.

*   **Median:** The middle value of a dataset.
    *   If the number of values ($n$) is odd, it is the middle value.
    *   If $n$ is even, it is the average of the two middle values,.

*   **Mode:**
    *   The value that occurs most frequently.
    *   Data can be unimodal, bimodal, or trimodal.

| Measure            | Definition                                    | Notes                                      |
| ------------------ | --------------------------------------------- | ------------------------------------------ |
| **Mean (Average)** |  ![mean](https://github.com/user-attachments/assets/fd0e504f-f7d6-4eae-98ac-c41b1b076f24)   | Sensitive to outliers                      |
| **Weighted Mean**  |  ![weighted mean](https://github.com/user-attachments/assets/002bf2f5-242f-4193-9b7f-36f3ea711d73)   | Used when values have different importance |
| **Trimmed Mean**   | Mean after removing extreme values            | Reduces outlier influence                  |
| **Median**         | Middle value when sorted                      | Best for skewed data/outliers              |
| **Mode**           | Most frequently occurring value               | Used for categorical data                  |


**Symmetric vs. Skewed Data**
The relationship between mean, median, and mode determines skewness,:
*   **Symmetric:** Mean = Median = Mode.
    *  <img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/a79fcb05-bf7b-4252-880d-32f28bf9abe9" />

*   **Positively Skewed:** Mode < Median < Mean (Tail extends to the right).
    * <img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/dbaefd2a-f4c7-461c-9c86-c51f0e5616a0" />
      
*   **Negatively Skewed:** Mean < Median < Mode (Tail extends to the left).
    * <img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/a1294e7c-7889-487a-bdc7-2abe17b2523b" />


---

### **IV. Measuring Dispersion (Spread)**

**Key Measures**
*   **Variance:**
    *   Average squared deviation from mean.  

*   **Standard Deviation:**
    *   Algebraic measures of spread.
    *   SD ($\sigma$ or $s$) is the square root of variance.
    *   Same unit as data

*   **Quartiles:**
    *   **Q1 (Lower Quartile):** The 25th percentile.
    *   **Median (Q2): The 50th percentile.
    *   **Q3 (Upper Quartile):** The 75th percentile.

*   **Inter-quartile Range (IQR):**
    *   Calculated as $Q3 - Q1$.
    *   It measures the spread of the middle 50% of the data.

*   **Outliers:**
    *   Typically defined as values:
      *   < ( Q1 - 1.5 . IQR ) or
      *   > ( Q3 + 1.5 . IQR )
---

### **V. Data Visualization: The Boxplot**

<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/2d1181b9-68f0-4886-9d58-f5a99635ddf1" />


A boxplot visually displays data distribution using:

* Box = IQR range (Q1 → Q3)
* Line inside box = Median
* Whiskers = min and max non-outlier values
* Points outside whiskers = Outliers


**Construction Steps**
1.  **Order** the numbers from least to greatest.
2.  Find the **Median** (the middle number). If two numbers share the middle, average them,.
3.  Split the list into a lower half and an upper half.
4.  Find the median of the lower half (**Lower Quartile / Q1**).
5.  Find the median of the upper half (**Upper Quartile / Q3**).
6.  Draw a **Box** connecting Q1 and Q3 on a number line.
7.  Mark the **Median** inside the box.
8.  Draw **Whiskers** connecting the box to the lowest and highest non-outlier points,.

<img width="300" height="80" alt="image" src="https://github.com/user-attachments/assets/8b421da0-bd8f-44d6-af3f-e585c6c30cb5" />
<img width="700" height="350" alt="image" src="https://github.com/user-attachments/assets/7e0111b3-9a28-4437-822f-2e690579fd4e" />

What can you say about the ages of the shoppers and what kind of shop they are:
*   Dressnice has a much lower median age, so the shoppers are younger
*   Clotheswell has broader appeal because the IQR is bigger
*   Dressnice is a shop for younger people, perhaps more fashionable

**Interpretation Example**
*   **Median Position:** Indicates the "average" characteristic (e.g., a lower median age means younger shoppers).
*   **Box Length (IQR):** Indicates the breadth of appeal or consistency. A larger IQR suggests broader appeal or more variation; a smaller IQR suggests a more focused or consistent group.

***

## **Summary Checklist**

| Concept          | Purpose                       |
| ---------------- | ----------------------------- |
| Central tendency | Understand average behavior   |
| Dispersion       | Understand variability        |
| Attribute types  | Correct encoding and analysis |
| Boxplots         | Detect spread and outliers    |

***

### **Analogy for Attribute Types**
*To better remember the difference between **Interval** and **Ratio** data:*
Think of a **ruler** vs. a **calendar**.
*   **Ratio (Ruler):** If you break a ruler in half, you have 0 length left. This is a true zero. You can also say 12 inches is twice as long as 6 inches.
*   **Interval (Calendar):** If you look at the year 0, time didn't stop or not exist; it was just a marker on the line. Furthermore, the year 2000 isn't "twice as much time" as the year 1000 in a physical sense, just a later position on the scale.
