Here are comprehensive notes on Ordinary Least Squares (OLS) regression, correlation, and performance metrics based on the provided text.

### **1. Core Concept: Ordinary Least Squares (OLS)**
*   **Definition:** OLS is a foundational linear regression methodology used to find the best-fitting line or hyperplane through a set of data points.
*   **Objective:** The primary goal of OLS is to minimize the sum of squared residuals (the differences between observed values and predicted values).
*   **Output:** It produces a statistically interpretable slope and intercept, allowing analysts to explain how predictors influence the response variable.

#### Ordinary Least Squares (OLS) vs Model Evaluation Metrics
Ordinary Least Squares (OLS) is a method used to build a regression model, while performance metrics such as R-squared, Adjusted R-squared, MSE, and RMSE are used to evaluate how well that model performs.

#### **What it OLS**
Ordinary Least Squares is a procedure for estimating the unknown parameters (coefficients) in a linear regression model.


### **2. Correlation Analysis**
Before applying regression, correlation is used to understand relationships within the data.
*   **Measurement:** Correlation measures the strength of linear relationships between variables.
*   **Range and Direction:**
    *   Values range from **-1 to +1**.
    *   **Positive correlation:** Variables increase together.
    *   **Negative correlation:** Variables move in opposite directions (one increases while the other decreases).
    *   **Zero correlation:** There is no linear association.
*   **Application:** It is a key tool in exploratory data analysis (EDA) and helps detect multicollinearity in regression models. Scatterplots and correlation matrices are used to visualize these relationships.

### **3. The Mathematics of OLS (Calculating the Best Fit)**
To determine the line of best fit ($y = mx + c$), OLS follows a specific calculation process using the means of $x$ and $y$.

*   **Slope ($m$):**
    *   Represents the rate of change of $y$ with respect to $x$.
    *   **Interpretation:** If $m = 1.5$, it means that for every 1-unit increase in $x$, $y$ is expected to increase by 1.5. Conversely, if $x$ decreases by 1, $y$ decreases by 1.5.
*   **Intercept ($c$):**
    *   Represents the value of $y$ when $x = 0$.
    *   It serves as a baseline or starting point where the regression line crosses the y-axis.
*   **Residual Calculation:**
    *   Residuals are calculated as the actual value minus the predicted value ($y - \hat{y}$).
    *   The best-fit line passes as close as possible to all data points by minimizing the sum of these squared residuals.

### **4. Model Performance Metrics**
Evaluating how well a regression model performs requires specific error metrics.

#### **Mean Absolute Error (MAE)**
*   **Formula:** $MAE = (Σ|y_i - ŷ_i|)/n$.
*   **Definition:** MAE measures the average absolute difference between predicted and actual values.
*   **Characteristics:**
    *   It captures the magnitude of error without considering direction.
    *   It is expressed in the same units as the response variable.
    *   **Robustness:** Unlike MSE, MAE is robust to extreme outliers because it does not square the errors.

#### **Mean Squared Error (MSE)**
*   **Formula:** $MSE = Σ(y_i - ŷ_i)² / n$.
*   **Definition:** MSE averages the squared prediction errors.
*   **Characteristics:**
    *   It penalizes larger deviations more significantly due to the quadratic weighting.
    *   It is derived directly from the least squares principle and serves as a basis for maximum likelihood estimation.
    *   It is highly sensitive to outliers.

#### **Root Mean Squared Error (RMSE)**
*   **Formula:** $RMSE = √(Σ(y_i - ŷ_i)² / n)$.
*   **Definition:** RMSE is the square root of the MSE value.
*   **Characteristics:**
    *   Like MAE, it retains unit consistency with the response variable, making it interpretable.
    *   It remains sensitive to large error deviations (like MSE) but provides an error magnitude that is easier to communicate in practical terms.
    *   Lower RMSE values imply higher model precision and reliability.

#### **R-squared ($R^2$)**
*   **Formula:** $R^2 = 1 - (SSR/SST)$.
*   **Definition:** $R^2$ explains the proportion of variance captured by the regression model regarding the total variation (SST).
*   **Characteristics:**
    *   Values typically range between 0 and 1, where higher scores imply stronger explanatory power.
    *   A negative $R^2$ indicates the model is performing worse than a naive baseline.
    *   It is an important complement to error metrics like MSE and MAE.

### **5. Practical Application: Interpreting Error Rates**
To determine if a model is "good," error metrics must be compared against the scale of the target variable.

*   **Example Case:** Predicting house prices with a mean value of \$200,000.
    *   **Excellent Model:** An RMSE of \$15,000 represents a 7.5% error rate relative to the mean.
    *   **Good Model:** An MAE of \$25,000 represents a 12.5% error rate.
    *   **Poor Model:** An RMSE of \$80,000 represents a 40% error rate.

***

### 🔍 Common Metrics

| Metric                             | Category                    | Purpose                                                                                                                                           |
| ---------------------------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **MSE (Mean Squared Error)**       | Error                       | Measures the average squared difference between actual and predicted values. Lower is better.                                                     |
| **RMSE (Root Mean Squared Error)** | Error                       | Square root of MSE; easier to interpret since it's in the same units as the target variable. Lower is better.                                     |
| **MAE (Mean Absolute Error)**      | Error                       | Measures average absolute difference between predictions and actual values. Less sensitive to outliers.                                           |
| **R-squared (R²)**                 | Goodness-of-fit             | Represents how much variance in the dependent variable the model explains. Higher is better.                                                      |
| **Adjusted R-squared**             | Goodness-of-fit (penalized) | Modified R² that penalizes adding unnecessary predictors; prevents overfitting. Higher indicates a better model only if new predictors add value. |


**Analogy for Understanding Metrics:**
Think of fitting a regression line like trying to throw a dart at the bullseye of a target.
*   **OLS** is the technique you use to adjust your stance to get your average throw as close to the center as possible.
*   **MAE** calculates the average distance of all your throws from the center, treating a miss to the left equally to a miss to the right.
*   **MSE** is a strict coach who yells louder the further you miss; if you miss by 2 inches, they are 4 times as angry as if you missed by 1 inch, forcing you to eliminate those wild, off-target throws (outliers).
