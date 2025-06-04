# Statistical Test Guider (Python + Win EXE)

Designed to assist researchers, data scientists, and students, this Python-based interactive command-line tool provides guidance in selecting appropriate statistical tests from a list of 50 of the most frequently employed statistical techniques, according to their study's purpose, research design, and data characteristics.

This tool was developed with the assistance of Google's Gemini 2.5 Pro Preview model.

**Status:** Actively being tested and refined. Expect improvements and expanded test coverage over time. Contributions and feedback are welcome!

## Table of Contents

- [Functionality](#functionality)
- [How It Works](#how-it-works)
- [Available Statistical Tests](#available-statistical-tests)
  - [I. Tests for Comparing Means/Medians (Location)](#i-tests-for-comparing-meansmedians-location)
  - [II. Tests for Proportions/Categorical Data](#ii-tests-for-proportionscategorical-data)
  - [III. Tests for Relationships & Regression Models](#iii-tests-for-relationships--regression-models)
  - [IV. Tests for Variances](#iv-tests-for-variances)
  - [V. Tests for Distributional Assumptions & Goodness-of-Fit (General)](#v-tests-for-distributional-assumptions--goodness-of-fit-general)
  - [VI. Time Series Specific Tests](#vi-time-series-specific-tests)
  - [VII. Survival Analysis Tests](#vii-survival-analysis-tests)
  - [VIII. Other Important/General Purpose Tests & Concepts](#viii-other-importantgeneral-purpose-tests--concepts)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Running the Guide](#running-the-guide)
- [Important Considerations](#important-considerations)
- [Contributing](#contributing)
- [License](#license)

## Functionality

The primary goal of this program is to simplify the often complex process of choosing the right statistical test. It achieves this by:

1.  **Interactive Questioning:** The program asks a series of targeted questions about your research goals, the number of groups or variables, the type of data (nominal, ordinal, interval, ratio), whether samples are paired or independent, and other relevant factors.
2.  **Decision Tree Logic:** Based on your answers, it navigates a built-in decision tree that maps specific research scenarios to appropriate statistical tests.
3.  **Test Recommendations:** Once a suitable path is identified, the program recommends one or more statistical tests.
4.  **Test Summaries:** For each recommended test, it provides:
    *   A concise **purpose** statement (what the test is used for).
    *   A list of key **assumptions** that need to be met for the test results to be valid.
5.  **Educational Tool:** Serves as a learning aid by exposing users to various tests and their underlying requirements.

## How It Works

The script uses a series of nested conditional statements (`if/elif/else`) to mimic a decision tree. User input is gathered via the `input()` function, and helper functions manage different branches of the decision tree.

A core component is a comprehensive Python dictionary (`TEST_SUMMARIES`) that stores the purpose and assumptions for each statistical test covered. When a test is recommended, its details are retrieved from this dictionary and displayed to the user.

## Available Statistical Tests

The guide currently includes information on the following statistical tests, grouped by their general purpose:

*(P) = Parametric, (NP) = Non-Parametric*

### I. Tests for Comparing Means/Medians (Location)

| Test Name                                              | Description                                                                                             |
| :----------------------------------------------------- | :------------------------------------------------------------------------------------------------------ |
| **1. One-Sample t-test (P)**                           | Tests if a sample mean is significantly different from a known or hypothesized population mean.           |
| **2. Two-Sample (Independent) t-test (P)**             | Compares the means of two independent groups.                                                           |
| **3. Welch's t-test (P)**                              | An adaptation of the two-sample t-test for when the two groups have unequal variances.                    |
| **4. Paired t-test (P)**                               | Compares the means of the same group/item at two different time points or conditions.                   |
| **5. One-Way ANOVA (P)**                               | Compares the means of three or more independent groups.                                                 |
| **6. Two-Way ANOVA (P)**                               | Examines the effect of two independent categorical variables (factors) on a continuous dependent variable. |
| **7. Repeated Measures ANOVA (P)**                     | Compares means across three or more time points or conditions for the same subjects.                    |
| **8. ANCOVA (P)**                                      | ANOVA that includes a continuous covariate to control for its effect.                                   |
| **9. Z-test (for means) (P)**                          | Tests a sample mean against a population mean when population variance is known (less common).            |
| **10. Mann-Whitney U Test (Wilcoxon Rank-Sum) (NP)**   | Non-parametric alternative to the independent two-sample t-test; compares medians.                        |
| **11. Wilcoxon Signed-Rank Test (NP)**                 | Non-parametric alternative to the paired t-test or one-sample t-test; compares medians.                   |
| **12. Kruskal-Wallis H Test (NP)**                     | Non-parametric alternative to one-way ANOVA; compares medians of three or more groups.                  |
| **13. Friedman Test (NP)**                             | Non-parametric alternative to repeated measures ANOVA.                                                  |
| **14. Sign Test (NP)**                                 | Simple non-parametric test for consistent differences between pairs or one sample median.                 |
| **15. Jonckheere-Terpstra Test (NP)**                  | Tests for an ordered difference (trend) among medians of three or more ordered groups.                  |
| **16. Mood's Median Test (NP)**                        | Tests if medians of two or more groups are equal.                                                       |

### II. Tests for Proportions/Categorical Data

| Test Name                                                         | Description                                                                                             |
| :---------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------ |
| **17. Chi-squared (χ²) Goodness-of-Fit Test**                     | Tests if observed frequencies of a single categorical variable match expected frequencies.                |
| **18. Chi-squared (χ²) Test of Independence/Association**         | Tests if two categorical variables are associated.                                                      |
| **19. Fisher's Exact Test**                                       | Used for 2x2 contingency tables, especially with small sample sizes, to test for independence.          |
| **20. McNemar's Test**                                            | Tests for changes in proportions for paired categorical data (e.g., before/after).                      |
| **21. Cochran's Q Test**                                          | Extension of McNemar's test for three or more related categorical variables (binary).                   |
| **22. Binomial Test**                                             | Tests if the proportion of successes in Bernoulli trials matches a hypothesized value.                  |
| **23. Z-test for Proportions (One-sample & Two-sample)**          | Tests for differences in proportions (large sample approximation).                                      |
| **24. Cochran-Armitage Test for Trend**                           | Tests for a trend in proportions across ordered categories.                                             |

### III. Tests for Relationships & Regression Models

| Test Name                                                         | Description                                                                                             |
| :---------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------ |
| **25. Pearson Correlation Coefficient (test of significance) (P)**| Measures linear association between two continuous variables.                                             |
| **26. Spearman Rank Correlation (test of significance) (NP)**     | Measures monotonic association between two ranked variables.                                              |
| **27. Kendall's Tau (test of significance) (NP)**                 | Another non-parametric measure of rank correlation.                                                     |
| **28. Simple Linear Regression (P)**                              | Models linear relationship between one independent and one dependent continuous variable.                 |
| **29. Multiple Linear Regression (P)**                              | Models linear relationship between multiple independent variables and one dependent continuous variable.  |
| **30. Logistic Regression**                                       | Models the probability of a binary outcome based on predictor variables.                                  |
| **31. Poisson Regression**                                        | Models count data.                                                                                      |
| **32. Negative Binomial Regression**                              | Models count data with overdispersion.                                                                  |
| **33. Ordinal Logistic Regression**                               | Models an ordinal dependent variable.                                                                   |

### IV. Tests for Variances

| Test Name                                | Description                                                                                   |
| :--------------------------------------- | :-------------------------------------------------------------------------------------------- |
| **34. F-test for Equality of Variances (P)** | Compares variances of two populations (sensitive to non-normality).                             |
| **35. Levene's Test**                    | Tests for equality of variances between groups (more robust to non-normality than Bartlett's). |
| **36. Bartlett's Test (P)**              | Tests for equality of variances between groups (assumes normality).                           |
| **37. Brown-Forsythe Test**              | A modification of Levene's test, often more robust, especially with skewed distributions.     |

### V. Tests for Distributional Assumptions & Goodness-of-Fit (General)

| Test Name                                             | Description                                                                                             |
| :---------------------------------------------------- | :------------------------------------------------------------------------------------------------------ |
| **38. Shapiro-Wilk Test**                             | Tests if a sample comes from a normally distributed population.                                         |
| **39. Kolmogorov-Smirnov (K-S) Test (One & Two-sample)** | One-sample tests if data follows a specified distribution; Two-sample tests if two samples come from the same distribution. |
| **40. Anderson-Darling Test**                         | Tests if data comes from a specific distribution (e.g., normal), good for tail deviations.            |
| **41. Lilliefors Test**                               | K-S modification for normality when mean/variance are unknown.                                          |

### VI. Time Series Specific Tests

| Test Name                                | Description                                                                |
| :--------------------------------------- | :------------------------------------------------------------------------- |
| **42. Durbin-Watson Test**               | Tests for first-order autocorrelation in regression residuals.             |
| **43. Ljung-Box Test (or Box-Pierce)**   | Tests for overall autocorrelation in a time series.                        |
| **44. Augmented Dickey-Fuller (ADF) Test** | Tests for a unit root (non-stationarity) in a time series.                 |
| **45. Kwiatkowski-Phillips-Schmidt-Shin (KPSS) Test** | Tests for stationarity (null is stationarity).                             |

### VII. Survival Analysis Tests

| Test Name                                                         | Description                                                                   |
| :---------------------------------------------------------------- | :---------------------------------------------------------------------------- |
| **46. Log-Rank Test**                                             | Compares survival distributions of two or more groups.                        |
| **47. Cox Proportional Hazards Model**                              | Regression model for survival data examining predictor effects on hazard rates. |

### VIII. Other Important/General Purpose Tests & Concepts

| Test Name                               | Description                                                                 |
| :-------------------------------------- | :-------------------------------------------------------------------------- |
| **48. Likelihood Ratio Test (LRT)**       | Compares the fit of two nested statistical models.                          |
| **49. Wald Test**                       | Assesses significance of parameters in a statistical model.                 |
| **50. Score Test (Lagrange Multiplier)**  | Another general test for model parameters, useful when models are hard to fit. |

## Getting Started

### Prerequisites

*   Python 3.x

### Running the Guide

1.  Clone this repository or download the `statistical_test_guide.py`.
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved the file.
4.  Run the script using the command:
    ```bash
    python statistical_test_guide.py
    ```
5.  Follow the on-screen prompts, answering questions about your research to receive test recommendations.

For **Windows users**, there is a compile version available in the repo (StatGuide.exe), so you can run it without the need of using Python. 

## Important Considerations

While this tool aims to be helpful, it is **not a substitute for a thorough understanding of statistical principles or consultation with a qualified statistician.**

*   **Assumptions are Key:** Always verify the assumptions of any recommended test using your specific data. Violating assumptions can lead to incorrect conclusions.
*   **Sample Size:** Consider the impact of your sample size on test choice and power.
*   **Post-Hoc Tests:** For tests like ANOVA or Kruskal-Wallis that compare 3+ groups, a significant result indicates *a* difference exists. You'll need appropriate post-hoc tests (e.g., Tukey's HSD, Dunn's test) to determine *which specific groups* differ.
*   **Multiple Comparisons:** Performing many statistical tests increases the chance of false positives (Type I errors). Consider adjustments like Bonferroni correction or False Discovery Rate (FDR) control if applicable.
*   **Effect Size:** Statistical significance (p-value) doesn't indicate the practical importance or magnitude of an effect. Always report and interpret effect sizes.
*   **Data Exploration:** Before running any inferential test, thoroughly explore your data with descriptive statistics and visualizations.

## Contributing

This project is currently in its early stages. Contributions, bug reports, and suggestions for improvement are highly welcome! Please feel free to:

*   Open an issue to report bugs or suggest features.
*   Fork the repository and submit a pull request with your enhancements.
    *   When adding new tests, please ensure to update the `TEST_SUMMARIES` dictionary with a clear purpose and key assumptions.
    *   Maintain consistency in the decision tree logic and user prompts.

## License

This project is licensed under the **MIT License**.
