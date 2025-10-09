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

