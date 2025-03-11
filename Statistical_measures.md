# Statistical Measures

## 1. **Mean (Average)**
   - **Definition**: The sum of all values divided by the number of values.
   - **Formula**:  
     Mean = (Σ x_i) / n
   - **Use**: Provides the central value of a dataset.

## 2. **Median**
   - **Definition**: The middle value of a dataset when the values are ordered.
   - **Use**: The median is useful when you have skewed data or outliers.

## 3. **Mode**
   - **Definition**: The value that appears most frequently in a dataset.
   - **Use**: The mode is useful for categorical data or identifying the most common value.

## 4. **Range**
   - **Definition**: The difference between the highest and lowest values in a dataset.
   - **Formula**:  
     Range = Maximum value - Minimum value
   - **Use**: Provides a basic measure of how spread out the data is.

## 5. **Variance**
   - **Definition**: The average of the squared differences from the mean.
   - **Formula**:  
     Variance = (Σ (x_i - μ)^2) / n
   - **Use**: Measures how spread out the values are in a dataset.

## 6. **Standard Deviation**
   - **Definition**: The square root of the variance, providing a measure of average distance from the mean.
   - **Formula**:  
     Standard Deviation = √(Variance)
   - **Use**: A measure of how spread out the data is, commonly used in statistics.

## 7. **Interquartile Range (IQR)**
   - **Definition**: The range between the first (Q1) and third (Q3) quartiles.
   - **Formula**:  
     IQR = Q3 - Q1
   - **Use**: Measures the spread of the middle 50% of the data.

## 8. **Percentiles and Quartiles**
   - **Definition**: Percentiles indicate the value below which a given percentage of data falls.
   - **Use**: Quartiles divide the data into four equal parts, with Q1 being the 25th percentile, Q2 being the median (50th percentile), and Q3 being the 75th percentile.

## 9. **Skewness**
   - **Definition**: Measures the asymmetry of the data distribution.
   - **Interpretation**: 
     - **Positive Skew**: Tail is longer on the right side.
     - **Negative Skew**: Tail is longer on the left side.
   - **Formula**:  
     Skewness = (n / ((n - 1)(n - 2))) Σ ((x_i - μ) / σ)^3
   - **Use**: Identifies the direction of skew in a distribution.

## 10. **Kurtosis**
   - **Definition**: Measures the "tailedness" or extremeness of the data distribution.
   - **Interpretation**:
     - **Leptokurtic**: High peak, fat tails.
     - **Platykurtic**: Flat peak, thin tails.
   - **Formula**:  
     Kurtosis = [(n(n + 1)) / ((n - 1)(n - 2)(n - 3))] Σ ((x_i - μ) / σ)^4 - [3(n - 1)^2 / ((n - 2)(n - 3))]
   - **Use**: Describes the shape of the distribution, particularly the presence of outliers.

## 11. **Coefficient of Variation (CV)**
   - **Definition**: The ratio of the standard deviation to the mean, expressed as a percentage.
   - **Formula**:  
     CV = (σ / μ) × 100
   - **Use**: Compares relative variability across datasets with different units or means.

## 12. **Z-Score**
   - **Definition**: Measures how many standard deviations a data point is from the mean.
   - **Formula**:  
     Z = (X - μ) / σ
   - **Use**: Identifies how extreme a data point is relative to the overall distribution.

## 13. **Boxplot and Outliers**
   - **Definition**: A boxplot shows the distribution of data based on the five-number summary.
   - **Use**: Helps visualize the spread, symmetry, and presence of outliers in a dataset.
   - **Outlier Detection**: Outliers are values below (Q1 - 1.5 × IQR) or above (Q3 + 1.5 × IQR).

## 14. **Correlation Coefficient (Pearson's r)**
   - **Definition**: Measures the strength and direction of the linear relationship between two variables.
   - **Formula**:  
     r = [n Σ(xy) - Σx Σy] / √[(n Σx² - (Σx)²)(n Σy² - (Σy)²)]
   - **Use**: Values range from -1 to +1, indicating the degree of linear relationship.

## 15. **Covariance**
   - **Definition**: Measures how two variables change together.
   - **Formula**:  
     Cov(X, Y) = (1 / n) Σ (x_i - μ_X)(y_i - μ_Y)
   - **Use**: Identifies directional relationships between two variables.

## 16. **Entropy (in Information Theory)**
   - **Definition**: Measures the uncertainty or randomness in a system.
   - **Formula**:  
     H(X) = - Σ p(x) log p(x)
   - **Use**: Quantifies the unpredictability of a system or dataset.

## 17. **Moment of Distribution (Higher-order moments)**
   - **Definition**: Moments provide detailed information about the shape of a distribution.
   - **Use**: Skewness and kurtosis are the third and fourth moments of a distribution.

## 18. **Cross-Validation**
   - **Definition**: A technique for evaluating the performance of a model by partitioning the data into training and test sets.
   - **Methods**:
     - **K-Fold Cross-Validation**: Data is divided into k subsets, and the model is trained and tested k times.
     - **Leave-One-Out Cross-Validation (LOOCV)**: Every data point is used once as a test set.
   - **Use**: Helps assess model generalization and prevent overfitting.

## 19. **Bayesian Statistics**
   - **Definition**: A statistical approach that uses Bayes' Theorem to update the probability of a hypothesis based on new evidence.
   - **Formula**:  
     P(θ | X) = [P(X | θ) P(θ)] / P(X)
   - **Use**: Incorporates prior knowledge and updates the beliefs based on data.

## 20. **Principal Component Analysis (PCA)**
   - **Definition**: A dimensionality reduction technique that projects data into new coordinate axes to capture the most variance.
   - **Use**: Reduces the number of variables while retaining as much information as possible.

## 21. **Factor Analysis**
   - **Definition**: Identifies latent variables that explain correlations between observed variables.
   - **Use**: Simplifies data and reveals hidden patterns or factors.

## 22. **Survival Analysis**
   - **Definition**: Analyzes time-to-event data, predicting the time until a specific event happens.
   - **Methods**: 
     - **Kaplan-Meier Estimator**: Estimates the survival function.
     - **Cox Proportional-Hazards Model**: Analyzes the relationship between survival time and predictor variables.

## 23. **Markov Chains and Monte Carlo Methods (MCMC)**
   - **Markov Chains**: Models the probability of moving from one state to another in a sequence of random events.
   - **Monte Carlo Simulation**: Uses random sampling to solve complex problems.
   - **Use**: Widely used in time series, forecasting, and simulations.

## 24. **Time Series Analysis**
   - **Definition**: Analyzes data collected over time, identifying trends, seasonality, and patterns.
   - **Methods**:
     - **ARIMA (AutoRegressive Integrated Moving Average)**: Forecasts time series data.
     - **Seasonal Decomposition of Time Series (STL)**: Decomposes time series into seasonal, trend, and residual components.

## 25. **Non-Parametric Tests**
   - **Definition**: Statistical tests that do not assume a specific distribution.
   - **Tests**:
     - **Mann-Whitney U Test**: Compares two independent samples.
     - **Kruskal-Wallis Test**: Non-parametric version of ANOVA.
     - **Wilcoxon Signed-Rank Test**: Compares two related samples.

## 26. **Entropy and Information Gain**
   - **Definition**: Entropy measures randomness, and information gain quantifies the reduction of entropy after a split.
   - **Use**: Used in decision trees and clustering algorithms.

## 27. **Hotelling’s T-squared Statistic**
   - **Definition**: A multivariate test used to compare the means of multiple variables.
   - **Use**: Tests hypotheses about multivariate data.

## 28. **Generalized Linear Models (GLMs)**
   - **Definition**: Extensions of linear regression models to handle different types of data distributions (e.g., binomial, Poisson).
   - **Use**: Used when the dependent variable does not follow a normal distribution.
