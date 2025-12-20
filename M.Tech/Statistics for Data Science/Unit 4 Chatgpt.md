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
