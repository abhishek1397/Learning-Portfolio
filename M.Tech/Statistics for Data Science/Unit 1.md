# **Measures of Central Tendency**

### **Definition**
Measures of central tendency are statistical tools used to identify the **central or typical value** around which other data points cluster in a dataset.
The three most commonly used measures are **Mean**, **Median**, and **Mode**.

They help summarize large data sets with a **single representative value**.

## **1. Mean (Arithmetic Average)**

### **Definition**
The **mean** is the arithmetic average of all values in a dataset.
It is calculated by **adding all the observations** and **dividing by the total number of observations**.

![equation](https://latex.codecogs.com/svg.image?\bg_black&fg_white&dpi=110&space;\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i)


* ( \sum X ) = Sum of all data values
* ( N ) = Number of observations

### **Example**

Dataset: 10, 20, 30, 40, 50

[
\text{Mean} = \frac{10 + 20 + 30 + 40 + 50}{5} = \frac{150}{5} = 30
]

**Interpretation:**
The average (mean) value of this dataset is **30**.

### **When to Use the Mean**

* When data is **continuous** and **normally distributed** (no extreme outliers).
* When **all values** contribute equally to the average.
* Best for **quantitative** data such as test scores, height, weight, or temperature.

### **When Not to Use**

* When there are **outliers** (extremely high or low values), as they can **distort** the mean.
  Example: Mean income can be misleading if a few very rich individuals are included.


## **2. Median (Middle Value)**

### **Definition**
The **median** is the **middle value** of an ordered dataset.
If the number of observations is:

* **Odd**, the median is the middle value.
* **Even**, the median is the average of the two middle values.

### **Example**

Dataset: 5, 10, 15, 20, 100
Ordered data → 5, 10, 15, 20, 100
The middle (3rd) value is **15**, so the **median = 15**.

If dataset: 5, 10, 15, 20, 25, 100
[
\text{Median} = \frac{15 + 20}{2} = 17.5
]

### **When to Use the Median**

* When data contains **outliers or skewed distributions**.
* When analyzing **income, property prices, or survival times**, where extreme values exist.
* For **ordinal data** (ranked data like satisfaction ratings: poor, fair, good, excellent).

### **When Not to Use**

* When data is **symmetrical** and has **no outliers** — mean would be better.
* When data is **nominal** (no natural order).


## **3. Mode (Most Frequent Value)**

### **Definition**
The **mode** is the value that occurs **most frequently** in a dataset.
A dataset can be:

* **Unimodal** – one mode
* **Bimodal** – two modes
* **Multimodal** – more than two modes

### **Example**

Dataset: 3, 7, 7, 8, 10, 10, 10, 12
The number **10** appears most often → **Mode = 10**

### **When to Use the Mode**

* When data is **categorical or nominal** (e.g., color, brand, gender).
  Example: Most preferred brand = Mode.
* When you want to know the **most common** or **frequent** response.

### **When Not to Use**

* When all values occur with equal frequency (no mode).
* When data is **continuous and spread out** with few repeating values.


## **Comparison and Appropriate Usage**

| **Measure** | **Definition**        | **Example (Data: 10, 20, 30, 40, 100)**              | **When to Use**                                  | **When Not to Use**                        |
| ----------- | --------------------- | ---------------------------------------------------- | ------------------------------------------------ | ------------------------------------------ |
| **Mean**    | Average of all values | (10 + 20 + 30 + 40 + 100)/5 = **40**                 | For **symmetric** distributions without outliers | When data has **extreme values**           |
| **Median**  | Middle value          | Ordered data → 10, 20, 30, 40, 100 → **Median = 30** | For **skewed** or **ordinal** data               | When data is symmetric and mean works fine |
| **Mode**    | Most frequent value   | If data = 10, 10, 20, 30, 40 → **Mode = 10**         | For **categorical** or **nominal** data          | When all values are unique                 |


## **Illustrative Summary**

| **Type of Data**                         | **Best Measure** | **Reason**                              |
| ---------------------------------------- | ---------------- | --------------------------------------- |
| Salary data with a few very high earners | Median           | Less affected by extreme values         |
| Exam scores of a balanced class          | Mean             | Represents overall performance          |
| Favorite food of students                | Mode             | Categorical data — most common response |


### **In Summary**

* **Mean** → Mathematical average → Best for **normal data**
* **Median** → Middle value → Best for **skewed data or outliers**
* **Mode** → Most frequent → Best for **categorical data**

> Together, these measures provide a **comprehensive understanding of data’s central tendency** and are often used jointly to detect **data skewness** and **distribution shape**.

***

# **Kurtosis and Its Types**

**Kurtosis** is a statistical measure that describes the *tailedness* or *sharpness* of the peak of a data distribution. It helps us understand the frequency of extreme values (outliers) compared to a normal distribution.

* **Unlike skewness** (which measures the asymmetry of a distribution), **kurtosis** focuses on the extremity of data points in the tails and the height of the peak.

### Types of Kurtosis:

![Types of Kurtosis](https://github.com/user-attachments/assets/1ae90b4b-8e20-4ced-b285-c3231a55d1d0)
---
![Kurtosis](https://github.com/user-attachments/assets/845a5977-79e1-49ad-a754-6db592a57fb4)


1. **Mesokurtic (Normal Distribution)**:

   * **Kurtosis Value**: 3 (same as the normal distribution).
   * **Characteristics**:

     * Features a *moderate peak* and *moderate tails*.
     * Extreme values (outliers) are neither too frequent nor too rare.
   * **Example**: Normal distribution (Bell curve).

2. **Leptokurtic (High Kurtosis)**:

   * **Kurtosis Value**: Greater than 3.
   * **Characteristics**:

     * Has a *higher peak* and *heavier tails*.
     * Indicates more frequent extreme values or outliers.
   * **Example**: Stock market returns (where extreme events like market crashes are more common).

3. **Platykurtic (Low Kurtosis)**:

   * **Kurtosis Value**: Less than 3.
   * **Characteristics**:

     * Has a *flatter peak* and *lighter tails*.
     * Extreme values are rare, and the data is more evenly distributed around the mean.
   * **Example**: Uniform distribution or certain discrete distributions.

### Key Takeaways:

* **Kurtosis** helps determine how concentrated the data is around the mean and how much is spread out in the tails.
* It is used to assess the likelihood of extreme events in the data.


# **Measure of Kurtosis**:

A **measure of kurtosis** refers to a specific way of calculating kurtosis based on data, often the **excess kurtosis**. In practice, when you calculate kurtosis, you are finding how much the data deviates from a normal distribution.

* **Excess Kurtosis**: This is the more commonly used version of kurtosis. It is calculated as the kurtosis of the data minus 3 (the kurtosis of a normal distribution). So:

  * **Excess Kurtosis = Kurtosis - 3**.
  * This adjustment allows a normal distribution to have a value of 0 for excess kurtosis.

### In summary:

* **Kurtosis** is the concept or property related to the tails of a distribution.
* **Measure of Kurtosis** is the statistical calculation (like **excess kurtosis**) used to quantify that property.

So, while **kurtosis** describes the tail behavior, **measure of kurtosis** is the actual metric that quantifies it!

