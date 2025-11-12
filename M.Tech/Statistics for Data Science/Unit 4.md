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

Would you like me to draw a simple diagram showing how the **right-tail rejection region** looks for this example? It really helps make the concept of “t in the right tail → reject H₀” crystal clear.
