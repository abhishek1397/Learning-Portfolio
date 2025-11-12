### 🧠 Step-by-step reasoning

1. **Tail direction comes from the alternative hypothesis (H₁):**

   * If **H₁: μ > μ₀**, → **Right-tailed test**
   * If **H₁: μ < μ₀**, → **Left-tailed test**
   * If **H₁: μ ≠ μ₀**, → **Two-tailed test**

   So yes — the **alternative hypothesis determines the tail** of the test.

---

2. **Example:**

   > You are testing whether the mean is greater than 100 g.

   * H₁: μ > 100 → **Right-tailed test**
   * We calculate **t(calculated)** from the sample.
   * If **t(calculated)** falls in the **right tail** (beyond **t(critical)**), we **reject H₀**.

---

3. **What does rejecting H₀ mean?**

   * It means we have enough evidence (based on our sample) to **support H₁**.
   * But remember — since we’re using a sample, there’s always a chance of being wrong.
   * That’s where **Type I error (α)** comes in.

---

4. **Type I error (α):**

   * Occurs when we **reject H₀ even though it’s actually true**.
   * The **α region** is the tail (or tails) where we decide to reject H₀.
   * Example: For a right-tailed test at α = 0.05, the **rightmost 5%** of the t-distribution is the **rejection region**.

   So yes — in your example:

   * You’re testing if μ > 100 → right-tailed test
   * You’ll reject H₀ if t(calculated) lies in the **right tail**
   * That rejection region corresponds to the **Type I error probability (α)**

---

### ✅ Summary

| Concept           | Explanation                                               |
| ----------------- | --------------------------------------------------------- |
| Tail direction    | Decided by **alternative hypothesis (H₁)**                |
| Right-tailed test | H₁: μ > μ₀                                                |
| Left-tailed test  | H₁: μ < μ₀                                                |
| Two-tailed test   | H₁: μ ≠ μ₀                                                |
| Reject H₀ when    | t(calculated) lies in the rejection region (tail(s))      |
| Type I error (α)  | Probability of rejecting a true H₀ (the shaded tail area) |

---

Excellent — here’s a **complete summary of the formulas** for all **three main types of *t*-tests**, with clear explanations and symbols. 👇

---

## 🔹 **1️⃣ One-Sample *t*-Test**

### 🎯 Purpose:

To test whether the **mean of a single sample** differs from a **known or hypothesized population mean (μ₀)**.

### 🧮 Formula:

[
t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}
]

### 📘 Where:

* ( \bar{x} ) = sample mean
* ( \mu_0 ) = hypothesized (population) mean
* ( s ) = sample standard deviation
* ( n ) = sample size

### 📈 Degrees of Freedom:

[
df = n - 1
]

---

## 🔹 **2️⃣ Independent Samples *t*-Test**

### 🎯 Purpose:

To test whether the **means of two independent groups** are significantly different.

---

### Case A: **Equal variances assumed (pooled t-test)**

[
t = \frac{\bar{x}_1 - \bar{x}_2}{s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}
]
where
[
s_p = \sqrt{\frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}}
]

**df:**
[
df = n_1 + n_2 - 2
]

---

### Case B: **Unequal variances (Welch’s t-test)**

[
t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}
]

**df (approximate):**
[
df = \frac{\left(\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}\right)^2}{\frac{(s_1^2 / n_1)^2}{n_1 - 1} + \frac{(s_2^2 / n_2)^2}{n_2 - 1}}
]

---

## 🔹 **3️⃣ Paired Samples *t*-Test (Dependent t-test)**

### 🎯 Purpose:

To test whether the **mean difference** between *paired observations* (e.g., before–after) is significantly different from zero.

### 🧮 Formula:

[
t = \frac{\bar{d}}{s_d / \sqrt{n}}
]

### 📘 Where:

* ( \bar{d} ) = mean of the differences (after − before)
* ( s_d ) = standard deviation of the differences
* ( n ) = number of pairs

### 📈 Degrees of Freedom:

[
df = n - 1
]

---

## 🔹 **Summary Table**

| Type of t-Test                        | Formula                                                                            | df                | When to Use                                       |
| ------------------------------------- | ---------------------------------------------------------------------------------- | ----------------- | ------------------------------------------------- |
| **One-sample**                        | ( t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}} )                                       | ( n - 1 )         | Compare sample mean to a known mean               |
| **Independent (equal var)**           | ( t = \frac{\bar{x}_1 - \bar{x}_2}{s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} )     | ( n_1 + n_2 - 2 ) | Compare two independent groups (equal variance)   |
| **Independent (unequal var / Welch)** | ( t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}} ) | Formula above     | Compare two independent groups (unequal variance) |
| **Paired (dependent)**                | ( t = \frac{\bar{d}}{s_d / \sqrt{n}} )                                             | ( n - 1 )         | Compare before–after or matched pairs             |

---

Would you like me to show how to **calculate one of them step-by-step with an example dataset** (e.g., independent or paired)?

Would you like me to draw a simple diagram showing how the **right-tail rejection region** looks for this example? It really helps make the concept of “t in the right tail → reject H₀” crystal clear.
