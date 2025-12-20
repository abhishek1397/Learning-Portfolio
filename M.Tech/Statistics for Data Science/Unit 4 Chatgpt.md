# **Hypothesis Testing – Formal Notes**

---

## **1. Introduction to Hypothesis Testing**

**Hypothesis Testing** is a statistical decision-making procedure used to draw conclusions about a **population parameter** based on **sample data**.

### **Objectives**

* To evaluate whether observed sample results reflect a real population effect.
* To distinguish systematic effects from random sampling variation.
* To support data-driven decisions with quantified risk.

### **Importance**

* Eliminates subjective judgment.
* Provides a standardized research methodology.
* Quantifies uncertainty and error probabilities.

---

## **2. Statistical Hypotheses**

A hypothesis test is based on two mutually exclusive statements:

### **2.1 Null Hypothesis (H0)**

* Represents the **status quo** or **no-effect** assumption.
* Assumed true until sufficient evidence suggests otherwise.
* Always contains equality (=, ≤, ≥).

**Example:**
H0: μ = 5

---

### **2.2 Alternative Hypothesis (H1 or Ha)**

* Represents the **research claim** or expected deviation.
* Accepted only if H0 is rejected.
* Uses inequality (<, >, ≠).

**Example:**
H1: μ < 5

---

## **3. Level of Significance (alpha)**

**Significance level (alpha)** is the maximum probability of rejecting a true null hypothesis.

### **Common Values**

* alpha = 0.05 → Standard level
* alpha = 0.01 → Strict (high-risk decisions)
* alpha = 0.10 → Lenient

**Interpretation:**
A 5% alpha means accepting a 5% risk of making a wrong rejection.

---

## **4. Types of Errors**

### **4.1 Type I Error (alpha error)**

* Rejecting a true H0
* False positive
* Controlled by alpha

### **4.2 Type II Error (beta error)**

* Failing to reject a false H0
* False negative
* Related to **power of test**

**Power of Test = 1 − beta**

---

## **5. Test Statistic**

A **test statistic** measures how far the sample result deviates from the hypothesized value in standardized units.

### **General Form**

(sample estimate − hypothesized value) / standard error

Examples:

* Z-statistic
* t-statistic

---

## **6. Critical Value Method**

The **critical value method** compares the test statistic with a threshold value.

### **6.1 Critical Value**

* A cutoff point determined by:

  * alpha
  * type of test
  * sampling distribution

### **6.2 Rejection Region**

* The region beyond the critical value.
* Total probability of this region equals alpha.

### **6.3 Decision Rule**

* If test statistic lies in rejection region → **Reject H0**
* Otherwise → **Fail to reject H0**

---

## **7. Types of Hypothesis Tests (Based on H1)**

### **7.1 Left-Tailed Test**

* H1: parameter < hypothesized value
* Rejection region in left tail

### **7.2 Right-Tailed Test**

* H1: parameter > hypothesized value
* Rejection region in right tail

### **7.3 Two-Tailed Test**

* H1: parameter ≠ hypothesized value
* Rejection regions split between both tails

---

## **8. Choice of Sampling Distribution**

### **8.1 Z-Test**

Used when:

* Population standard deviation is known, or
* Sample size is large (n ≥ 30)

Distribution: Standard Normal

---

### **8.2 T-Test**

Used when:

* Population standard deviation is unknown
* Sample size is small (n < 30)

Characteristics:

* Wider tails than normal distribution
* More conservative

**Degrees of Freedom (df):**
df = n − 1

---

## **9. Steps in Hypothesis Testing**

1. State H0 and H1 clearly
2. Choose alpha (before analysis)
3. Select appropriate test statistic
4. Determine critical value
5. Compute test statistic
6. Compare statistic with critical value
7. Make decision and conclusion

---

## **10. Interpretation of Results**

* **Reject H0**: Sufficient statistical evidence supports H1
* **Fail to Reject H0**: Insufficient evidence; does not prove H0 true

---

## **11. Statistical vs Practical Significance**

* Statistical significance indicates evidence against H0
* Practical significance considers real-world impact
* Both must be evaluated for sound conclusions

---

## **12. Key Guidelines**

* Hypotheses must be defined before data analysis
* Alpha must not be adjusted post-analysis
* Use one method consistently (critical value or p-value)
* Stronger deviation from H0 implies stronger evidence

---

## **Summary**

Hypothesis testing provides a formal, objective mechanism to validate claims under uncertainty by:

* Defining competing hypotheses
* Quantifying acceptable risk
* Using probability distributions
* Applying clear decision rules

It is a foundational tool in statistical inference, research, and data-driven decision-making.

---

* **Z vs t comparison table**
* **p-value method version**
* **MCQ / viva-oriented notes**

Say which one—no redundancy, no filler.


--- 

---

# **Z-Test and T-Test – Formal Statistical Notes**

---

## **1. Direction of Hypothesis Tests**

The **alternative hypothesis (H1)** determines the direction and placement of the rejection region.

### **1.1 Two-Tailed Test (Non-Directional)**

* **Purpose:** Detects deviation in either direction.
* **Hypotheses:**

  * H0: mu = mu0
  * H1: mu ≠ mu0
* **Rejection Region:** Split equally between left and right tails.
* **Use Case:** When no prior direction of change is assumed.

---

### **1.2 One-Tailed Test (Directional)**

#### **Left-Tailed Test**

* **Hypotheses:**

  * H0: mu ≥ mu0
  * H1: mu < mu0
* **Rejection Region:** Left tail
* **Keywords:** decrease, less than, reduced, below

#### **Right-Tailed Test**

* **Hypotheses:**

  * H0: mu ≤ mu0
  * H1: mu > mu0
* **Rejection Region:** Right tail
* **Keywords:** increase, greater than, exceeds

---

## **2. Z-Test**

### **2.1 Purpose**

Used to test whether a **sample mean differs from a population mean** when population variability is known or sample size is large.

### **2.2 Conditions for Use**

* Population standard deviation (sigma) is known
  OR
* Sample size n ≥ 30
* Data approximately normally distributed

---

### **2.3 Test Statistic**

Z = (X̄ − mu0) / (sigma / sqrt(n))

Where:

* X̄ = sample mean
* mu0 = hypothesized population mean
* sigma = population standard deviation
* n = sample size

---

### **2.4 Decision Rule**

* Determine critical Z value using alpha and test type
* Reject H0 if calculated Z lies in rejection region
* Otherwise, fail to reject H0

---

### **2.5 Z-Test Interpretation**

* Larger absolute Z values indicate stronger evidence against H0
* Two-tailed tests require stronger evidence than one-tailed tests at the same alpha

---

## **3. T-Test (One-Sample)**

### **3.1 Purpose**

Tests whether a sample mean differs from a hypothesized population mean when population variance is unknown.

---

### **3.2 Conditions for Use**

* Population standard deviation unknown
* Sample size n < 30
* Data approximately normally distributed

---

### **3.3 Test Statistic**

t = (X̄ − mu0) / (s / sqrt(n))

Where:

* s = sample standard deviation

---

### **3.4 Degrees of Freedom**

df = n − 1

Degrees of freedom determine the shape of the t-distribution.

---

### **3.5 Characteristics of t-Distribution**

* Symmetrical around zero
* Wider tails than normal distribution
* Becomes closer to normal distribution as n increases
* More conservative than Z-test

---

### **3.6 Decision Rule**

* Determine critical t value using df, alpha, and test type
* Reject H0 if calculated t lies in rejection region
* Otherwise, fail to reject H0

---

## **4. Independent Two-Sample T-Test**

### **4.1 Purpose**

Compares means of **two independent groups** to determine whether a statistically significant difference exists.

---

### **4.2 Hypotheses**

* H0: mu1 = mu2
* H1: mu1 ≠ mu2 (two-tailed, most common)

---

### **4.3 Assumptions**

* Samples are independent
* Data approximately normal
* Variances equal (pooled t-test)
* If variances unequal → Welch’s t-test

---

### **4.4 Test Statistic (Conceptual Form)**

t = (X̄1 − X̄2) / Standard Error of Difference

Degrees of freedom depend on variance assumption.

---

### **4.5 Decision Rule**

* Use absolute value of t for two-tailed tests
* Reject H0 if |t| exceeds critical t value

---

## **5. Comparison: Z-Test vs T-Test**

| Aspect           | Z-Test      | T-Test         |
| ---------------- | ----------- | -------------- |
| Population SD    | Known       | Unknown        |
| Sample size      | Large (≥30) | Small (<30)    |
| Distribution     | Normal      | t-distribution |
| Tails            | Narrow      | Wider          |
| Conservativeness | Lower       | Higher         |

---

## **6. Interpretation of Results**

* **Reject H0:** Evidence supports a statistically significant difference
* **Fail to Reject H0:** Insufficient evidence; does not prove H0 true
* Statistical significance does not imply practical significance

---

## **7. Summary Decision Framework**

1. Define H0 and H1
2. Identify test direction
3. Choose significance level alpha
4. Select appropriate test (Z or T)
5. Compute test statistic
6. Determine critical value
7. Compare and conclude

---

## **8. Key Examination Notes**

* Direction of H1 determines tails
* Alpha must be fixed before analysis
* Z and T are inference tools, not performance measures
* Always report test statistic, df (if applicable), alpha, and conclusion

---

If you want next:

* **Solved numericals with step-by-step tables**
* **Critical Z and t value cheat sheet**
* **Viva-oriented Q&A**
* **p-value method version (parallel to this)**

Say which one.
