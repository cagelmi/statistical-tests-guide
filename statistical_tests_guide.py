# statistical_tests_guide.py
# Author: Claudio Gelmi @ https://github.com/cagelmi
# Date: 2025-05-12
# Description: An interactive guide to selecting statistical tests.
# (This program was developed with the assistance of Google's Gemini 2.5 Pro model.)

# --- TEST SUMMARIES DICTIONARY (ASSUMING KEYS ARE CLEAN, e.g., "37. Brown-Forsythe Test") ---
TEST_SUMMARIES = {
    "1. One-Sample t-test (P)": {
        "purpose": "Tests if the mean of a single sample is significantly different from a known or hypothesized population mean.",
        "assumptions": [
            "Dependent variable is continuous (interval/ratio).",
            "Data are a random sample from the population.",
            "Observations are independent.",
            "Data are approximately normally distributed (or sample size is large, e.g., n > 30, by Central Limit Theorem)."
        ]
    },
    "2. Two-Sample (Independent) t-test (P)": {
        "purpose": "Compares the means of two independent groups to determine if there is a statistically significant difference between them.",
        "assumptions": [
            "Dependent variable is continuous (interval/ratio).",
            "Two independent samples/groups.",
            "Observations are independent within and between groups.",
            "Data in each group are approximately normally distributed (or sample sizes are large).",
            "Homogeneity of variances (variances are equal in both groups - if not, Welch's t-test is used)."
        ]
    },
    "3. Welch's t-test (P)": {
        "purpose": "Compares the means of two independent groups when the assumption of equal variances is violated.",
        "assumptions": [
            "Dependent variable is continuous (interval/ratio).",
            "Two independent samples/groups.",
            "Observations are independent within and between groups.",
            "Data in each group are approximately normally distributed (or sample sizes are large).",
            "(Does NOT assume homogeneity of variances)."
        ]
    },
    "4. Paired t-test (P)": {
        "purpose": "Compares the means of the same group or item at two different time points or under two different conditions (paired data).",
        "assumptions": [
            "Dependent variable is continuous (interval/ratio).",
            "Data are paired (e.g., before-after measurements on the same subject).",
            "The differences between the paired observations are approximately normally distributed (or sample size of pairs is large).",
            "Pairs are a random sample from the population of pairs.",
            "Observations within pairs are dependent, but pairs themselves are independent."
        ]
    },
    "5. One-Way ANOVA (P)": {
        "purpose": "Compares the means of three or more independent groups to determine if at least one group mean is different from the others.",
        "assumptions": [
            "Dependent variable is continuous (interval/ratio).",
            "Three or more independent categorical groups.",
            "Observations are independent within and between groups.",
            "Data in each group are approximately normally distributed (or sample sizes in groups are adequate).",
            "Homogeneity of variances (variances are equal across all groups - check with Levene's or Bartlett's test)."
        ]
    },
    "6. Two-Way ANOVA (P) (or higher-way ANOVA)": { # This key has the note, ensure it's intended
        "purpose": "Examines the effect of two (or more) independent categorical variables (factors) on a continuous dependent variable, including their potential interaction effect.",
        "assumptions": [
            "Dependent variable is continuous (interval/ratio).",
            "Two or more independent categorical factors.",
            "Observations are independent.",
            "Data within each cell (combination of factor levels) are approximately normally distributed.",
            "Homogeneity of variances across all cells."
        ]
    },
    "7. Repeated Measures ANOVA (P)": {
        "purpose": "Compares means across three or more time points or conditions for the same subjects (within-subjects design).",
        "assumptions": [
            "Dependent variable is continuous (interval/ratio).",
            "One within-subjects factor with three or more levels (conditions/time points).",
            "Observations are dependent (same subjects).",
            "The differences between levels are multivariate normally distributed.",
            "Sphericity (variances of the differences between all pairs of levels are equal). If violated, corrections like Greenhouse-Geisser or Huynh-Feldt are used."
        ]
    },
    "8. ANCOVA (Analysis of Covariance) (P)": {
        "purpose": "Combines ANOVA and regression to compare means of groups on a dependent variable while statistically controlling for the effect of one or more continuous covariates.",
        "assumptions": [
            "All assumptions of ANOVA (normality, homogeneity of variances, independence of errors for DV within groups).",
            "Linear relationship between the covariate(s) and the dependent variable.",
            "Homogeneity of regression slopes (the relationship between covariate and DV is the same across all groups).",
            "Covariate is measured without error (or with negligible error).",
            "Covariate is independent of the treatment effect (grouping variable)."
        ]
    },
    "9. Z-test (for means) (P)": {
        "purpose": "Tests if a sample mean is significantly different from a known population mean when the population variance is known.",
        "assumptions": [
            "Dependent variable is continuous.",
            "Population variance (σ²) is known.",
            "Data are a random sample.",
            "Observations are independent.",
            "Data are normally distributed or sample size is large (n > 30)."
        ]
    },
    "10. Mann-Whitney U Test (Wilcoxon Rank-Sum Test) (NP)": { # Key has full name
        "purpose": "Non-parametric alternative to the independent two-sample t-test. Compares the medians (or distributions) of two independent groups.",
        "assumptions": [
            "Dependent variable is at least ordinal (or continuous but not normally distributed).",
            "Two independent samples/groups.",
            "Observations are independent.",
            "For testing medians specifically, assumes distributions have similar shapes (otherwise tests for stochastic dominance)."
        ]
    },
    "11. Wilcoxon Signed-Rank Test (NP)": {
        "purpose": "Non-parametric alternative to the paired t-test or one-sample t-test. Compares medians for paired data or a single sample median against a hypothesized value.",
        "assumptions": [
            "Dependent variable is at least ordinal (or continuous but differences not normal).",
            "Data are paired (for paired version) or a single sample.",
            "The distribution of the differences (for paired) or data (for one-sample) is symmetric (for testing median).",
            "Observations are independent (between pairs or for single sample)."
        ]
    },
    "12. Kruskal-Wallis H Test (NP)": {
        "purpose": "Non-parametric alternative to one-way ANOVA. Compares the medians (or distributions) of three or more independent groups.",
        "assumptions": [
            "Dependent variable is at least ordinal (or continuous but assumptions for ANOVA violated).",
            "Three or more independent categorical groups.",
            "Observations are independent.",
            "For testing medians specifically, assumes distributions in all groups have similar shapes."
        ]
    },
    "13. Friedman Test (NP)": {
        "purpose": "Non-parametric alternative to repeated measures ANOVA. Compares medians across three or more related groups or conditions.",
        "assumptions": [
            "Dependent variable is at least ordinal.",
            "Data consist of k >= 3 related groups/conditions (e.g., same subject under different treatments, or multiple raters rating same items).",
            "Observations are ranks within each block (subject/rater).",
            "No interaction between blocks and treatments is assumed."
        ]
    },
    "14. Sign Test (NP)": {
        "purpose": "A simple non-parametric test for consistent differences between pairs of observations (e.g., positive vs. negative change) or if a single sample median is different from a hypothesized value. Only considers the direction of differences, not magnitude.",
        "assumptions": [
            "Data are paired (for paired version) or a single sample.",
            "Variable is at least ordinal, allowing for direction of difference.",
            "Observations are independent (between pairs or in the single sample)."
        ]
    },
    "15. Jonckheere-Terpstra Test (NP)": {
        "purpose": "Tests for an ordered difference (trend) among medians of three or more independent groups when the groups themselves have a natural ordering (e.g., increasing dose levels).",
        "assumptions": [
            "Dependent variable is at least ordinal.",
            "Independent variable defines three or more groups that are ordered a priori.",
            "Independent samples.",
            "Assumes a monotonic trend across group medians."
        ]
    },
    "16. Mood's Median Test (NP)": {
        "purpose": "Tests if the medians of two or more independent groups are equal. It is a specific application of the Chi-squared test on counts above/below the overall median.",
        "assumptions": [
            "Dependent variable is continuous (or ordinal with many levels).",
            "Two or more independent samples/groups.",
            "Observations are independent.",
            "Less powerful than Mann-Whitney U or Kruskal-Wallis for detecting shifts if their assumptions hold."
        ]
    },
    "17. Chi-squared (χ²) Goodness-of-Fit Test": { # Key includes (χ²)
        "purpose": "Tests if the observed frequencies of a single categorical variable match expected frequencies from a hypothesized distribution.",
        "assumptions": [
            "Data are categorical (nominal or ordinal).",
            "Observations are independent.",
            "Sample size is reasonably large (e.g., expected frequency in each category ≥ 5 for reliability of chi-squared approximation)."
        ]
    },
    "18. Chi-squared (χ²) Test of Independence/Association": { # Key includes (χ²)
        "purpose": "Tests if two categorical variables are associated or independent by comparing observed frequencies in a contingency table to expected frequencies under the null hypothesis of independence.",
        "assumptions": [
            "Both variables are categorical (nominal or ordinal).",
            "Observations are independent.",
            "Data are from a random sample.",
            "Sample size is reasonably large (e.g., expected frequency in each cell of the contingency table ≥ 5 for most cells, and no cell < 1)."
        ]
    },
    "19. Fisher's Exact Test": {
        "purpose": "Tests for independence between two categorical variables in a 2x2 contingency table, especially useful when sample sizes are small and expected cell counts are low (violating Chi-squared assumptions).",
        "assumptions": [
            "Both variables are categorical and dichotomous (2x2 table).",
            "Observations are independent.",
            "Row and column totals are considered fixed (conditional test)."
        ]
    },
    "20. McNemar's Test (for 2x2 tables, binary outcome, two related groups/times)": { # Key has full description
        "purpose": "Tests for changes in proportions for paired categorical data (binary outcome measured twice on the same subject, or matched pairs). Focuses on discordant pairs.",
        "assumptions": [
            "Data are paired and categorical (binary).",
            "Sample is random.",
            "Nominal scale of data."
        ]
    },
    "21. Cochran's Q Test": {
        "purpose": "An extension of McNemar's test for three or more related categorical variables (binary responses) from the same subjects or matched sets. Tests if the proportion of 'successes' is equal across conditions.",
        "assumptions": [
            "Dependent variable is binary (0/1).",
            "Three or more related groups/conditions.",
            "Data are arranged in blocks (e.g., subjects).",
            "Random sample of blocks."
        ]
    },
    "22. Binomial Test": {
        "purpose": "Tests if the proportion of successes in a series of independent Bernoulli trials matches a hypothesized population proportion.",
        "assumptions": [
            "Data consist of 'n' independent trials.",
            "Each trial has only two possible outcomes (success/failure).",
            "The probability of success (p) is constant for each trial."
        ]
    },
    "23. Z-test for Proportions (One-sample) (Large N)": { # Key has full description
        "purpose": "Tests if a sample proportion is significantly different from a hypothesized population proportion, using a normal approximation for large samples.",
        "assumptions": [
            "Data are binary.",
            "Random sample.",
            "Observations are independent.",
            "Large sample size (typically np ≥ 10 and n(1-p) ≥ 10 for normal approximation to hold)."
        ]
    },
    "23. Z-test for Proportions (Two-sample) (Large N, often equivalent to Chi-squared for 2x2)": { # Key has full description
        "purpose": "Compares proportions from two independent groups, using a normal approximation for large samples.",
        "assumptions": [
            "Data are binary for both groups.",
            "Two independent random samples.",
            "Observations are independent.",
            "Large sample sizes in both groups (e.g., n1*p1, n1*(1-p1), n2*p2, n2*(1-p2) all ≥ 5 or 10)."
        ]
    },
    "24. Cochran-Armitage Test for Trend (for ordered trend)": { # Key has full description
        "purpose": "Tests for a linear trend in proportions across levels of an ordered categorical variable (e.g., does proportion of 'yes' increase with dose level?).",
        "assumptions": [
            "One variable is binary (outcome).",
            "The other variable is categorical with ordered levels (exposure/group).",
            "Independent observations.",
            "Scores are assigned to the ordered categories to represent the trend."
        ]
    },
    "25. Pearson Correlation Coefficient (test of significance) (P)": { # Key has full name
        "purpose": "Measures the strength and direction of the linear relationship between two continuous variables. The test determines if this correlation is statistically different from zero.",
        "assumptions": [
            "Both variables are continuous (interval/ratio).",
            "Linear relationship between the two variables.",
            "Bivariate normality (observations are sampled from a bivariate normal distribution).",
            "Observations are independent.",
            "Homoscedasticity (variance of one variable is similar across all values of the other - visible in scatterplot)."
        ]
    },
    "26. Spearman Rank Correlation (NP)": {
        "purpose": "Measures the strength and direction of the monotonic (not necessarily linear) association between two ranked variables (or continuous variables converted to ranks).",
        "assumptions": [
            "Variables are at least ordinal (or continuous).",
            "Monotonic relationship.",
            "Observations are independent.",
            "Paired observations."
        ]
    },
    "27. Kendall's Tau (NP)": {
        "purpose": "Another non-parametric measure of rank correlation, assessing the strength of monotonic association. Often preferred for smaller datasets or data with many tied ranks.",
        "assumptions": [
            "Variables are at least ordinal.",
            "Monotonic relationship.",
            "Observations are independent.",
            "Paired observations."
        ]
    },
    "28. Simple Linear Regression (F-test for model, t-tests for coefficients) (P)": { # Key has full description
        "purpose": "Models the linear relationship between one independent variable (predictor) and one continuous dependent variable (outcome). F-test checks overall model fit; t-tests check individual coefficient significance.",
        "assumptions": [
            "Linear relationship between IV and DV.",
            "Independent observations (residuals are independent).",
            "Homoscedasticity (constant variance of residuals across all levels of IV).",
            "Normality of residuals (errors are normally distributed).",
            "IV is measured without error (or error is negligible)."
        ]
    },
    "29. Multiple Linear Regression (F-test for model, t-tests for coefficients) (P)": { # Key has full description
        "purpose": "Models the linear relationship between multiple independent variables (predictors) and one continuous dependent variable (outcome).",
        "assumptions": [
            "Linear relationship between each IV and the DV (after accounting for other IVs).",
            "Independent observations (residuals are independent).",
            "Homoscedasticity (constant variance of residuals).",
            "Normality of residuals.",
            "Absence of perfect multicollinearity among IVs (IVs are not perfectly correlated).",
            "IVs are measured without error (or error is negligible)."
        ]
    },
    "30. Logistic Regression (Likelihood Ratio Test, Wald Test, Score Test for model/coefficients)": { # Key has full description
        "purpose": "Models the probability of a binary outcome (0 or 1) based on one or more predictor variables (continuous or categorical).",
        "assumptions": [
            "Dependent variable is binary (dichotomous).",
            "Independent observations.",
            "Linearity of the logit: The log-odds of the outcome are linearly related to continuous predictors.",
            "Absence of perfect multicollinearity among predictors.",
            "Sufficiently large sample size (e.g., rule of thumb 10-20 events per predictor variable)."
        ]
    },
    "31. Poisson Regression (Likelihood Ratio Test, Wald Test, Score Test)": { # Key has full description
        "purpose": "Models count data (non-negative integers) based on one or more predictor variables. Assumes the mean and variance of the count are equal.",
        "assumptions": [
            "Dependent variable is a count (non-negative integers).",
            "Independent observations.",
            "The logarithm of the mean count is a linear function of the predictors (log-linear model).",
            "Equidispersion: The mean of the distribution is equal to its variance (E[Y] = Var[Y]).",
            "Events occur independently over a fixed period of time/space."
        ]
    },
    "32. Negative Binomial Regression (Likelihood Ratio Test, Wald Test, Score Test) (handles overdispersion)": { # Key has full description
        "purpose": "Models count data, similar to Poisson regression, but is more flexible as it allows for overdispersion (variance greater than the mean).",
        "assumptions": [
            "Dependent variable is a count.",
            "Independent observations.",
            "Logarithm of the mean count is a linear function of predictors.",
            "Allows for overdispersion (variance > mean)."
        ]
    },
    "33. Ordinal Logistic Regression": {
        "purpose": "Models an ordinal dependent variable (categories with a natural order) based on one or more predictor variables.",
        "assumptions": [
            "Dependent variable is ordinal.",
            "Independent observations.",
            "Proportional odds assumption (or parallel lines assumption): The effect of predictors is consistent across the different thresholds of the ordinal categories.",
            "Absence of perfect multicollinearity."
        ]
    },
    "34. F-test for Equality of Variances (P)": {
        "purpose": "Compares the variances of two populations to determine if they are significantly different. Highly sensitive to violations of normality.",
        "assumptions": [
            "Data in both groups are approximately normally distributed.",
            "Independent samples.",
            "Observations are independent."
        ]
    },
    "35. Levene's Test": {
        "purpose": "Tests for equality of variances (homogeneity of variances) between two or more groups. More robust to non-normality than Bartlett's test or the F-test for variances.",
        "assumptions": [
            "Independent samples.",
            "Dependent variable is continuous.",
            "Tests absolute deviations (or squared deviations) from group means/medians using ANOVA."
        ]
    },
    "36. Bartlett's Test (P)": {
        "purpose": "Tests for equality of variances between two or more groups, assuming the data in each group are normally distributed. Sensitive to non-normality.",
        "assumptions": [
            "Data in each group are approximately normally distributed.",
            "Independent samples.",
            "Observations are independent."
        ]
    },
    "37. Brown-Forsythe Test": {
        "purpose": "A modification of Levene's test for equality of variances, often considered more robust, especially when distributions are skewed. Uses ANOVA on absolute deviations from group medians.",
        "assumptions": [
            "Independent samples.",
            "Dependent variable is continuous."
        ]
    },
    "38. Shapiro-Wilk Test": {
        "purpose": "Tests the null hypothesis that a sample of data came from a normally distributed population.",
        "assumptions": [
            "Data are a random sample.",
            "Observations are independent.",
            "Specifically designed for testing normality; often more powerful than other general goodness-of-fit tests for normality."
        ]
    },
    "39. Kolmogorov-Smirnov (K-S) Test (One-sample)": { # Key includes (One-sample)
        "purpose": "Tests if a sample of data comes from a specific, fully specified continuous distribution (e.g., normal with given mean/SD, exponential, uniform).",
        "assumptions": [
            "Data are a random sample from a continuous distribution.",
            "The hypothesized distribution must be fully specified (parameters known, not estimated from data, for the standard K-S test). Lilliefors test is a modification for normality when mean/SD are estimated."
        ]
    },
    "39. Kolmogorov-Smirnov (K-S) Test (Two-sample) (NP)": { # Key includes (Two-sample) (NP)
        "purpose": "Tests if two independent samples come from the same underlying continuous distribution, without specifying what that distribution is. Sensitive to differences in location, scale, and shape.",
        "assumptions": [
            "Two independent random samples.",
            "Data are from continuous distributions (though can be used for discrete if care is taken with ties)."
        ]
    },
    "40. Anderson-Darling Test": {
        "purpose": "Tests if a sample of data comes from a specific distribution (e.g., normal, exponential, Weibull). Often considered more powerful than K-S for detecting deviations in the tails of the distribution.",
        "assumptions": [
            "Data are a random sample.",
            "The specific distribution being tested against needs to be chosen."
        ]
    },
    "41. Lilliefors Test": {
        "purpose": "A modification of the Kolmogorov-Smirnov test specifically for testing normality when the mean and variance of the population are unknown and are estimated from the sample data.",
        "assumptions": [
            "Data are a random sample.",
            "Testing for normality."
        ]
    },
    "42. Durbin-Watson Test": {
        "purpose": "Tests for first-order autocorrelation (serial correlation) in the residuals from a regression analysis.",
        "assumptions": [
            "Regression model has been fitted.",
            "Errors are normally distributed.",
            "Regressors are non-stochastic (fixed).",
            "The test is for first-order autocorrelation (AR(1) process)."
        ]
    },
    "43. Ljung-Box Test (or Box-Pierce Test)": { # Key includes alternative name
        "purpose": "Tests for overall autocorrelation (up to a specified number of lags) in a time series or in the residuals of a time series model. Tests if a group of autocorrelations are different from zero.",
        "assumptions": [
            "Time series data.",
            "Null hypothesis is that the data are independently distributed (no serial correlation)."
        ]
    },
    "44. Augmented Dickey-Fuller (ADF) Test": {
        "purpose": "Tests for a unit root in a time series sample, which is a common way to test for stationarity. The null hypothesis is that a unit root is present (the series is non-stationary).",
        "assumptions": [
            "Time series data.",
            "The underlying model can be an AR(p) process. The 'augmented' part adds lagged difference terms to handle more complex dynamics."
        ]
    },
    "45. Kwiatkowski-Phillips-Schmidt-Shin (KPSS) Test": {
        "purpose": "Another test for stationarity in a time series. Unlike ADF, the null hypothesis of the KPSS test is that the series is stationary (around a deterministic trend or level).",
        "assumptions": [
            "Time series data.",
            "Null hypothesis can be level stationarity or trend stationarity."
        ]
    },
    "46. Log-Rank Test": {
        "purpose": "Compares the survival distributions of two or more independent groups (e.g., treatment vs. control). Tests the null hypothesis that there is no difference in survival between the groups over time.",
        "assumptions": [
            "Two or more independent groups.",
            "Survival times are accurately measured and censoring is non-informative (censoring reasons are unrelated to survival probability).",
            "Proportional hazards: The hazard ratio between groups is assumed to be constant over time (though log-rank is somewhat robust to violations, especially if hazards don't cross)."
        ]
    },
    "47. Cox Proportional Hazards Model (Wald/Likelihood Ratio tests for coefficients)": { # Key has full description
        "purpose": "A semi-parametric regression model for survival data that examines the effect of predictor variables (covariates) on the hazard rate, without assuming a specific baseline hazard function.",
        "assumptions": [
            "Proportional hazards: The effect of covariates on the hazard is multiplicative and constant over time (hazard ratio is constant).",
            "Independent observations (or use robust standard errors for clustered data).",
            "Linearity of continuous covariates on the log-hazard scale.",
            "Non-informative censoring."
        ]
    },
    "48. Likelihood Ratio Test (LRT)": {
        "purpose": "A general statistical test used for comparing the fit of two nested statistical models (one model is a simpler, restricted version of the other). Tests if the more complex model provides a significantly better fit.",
        "assumptions": [
            "Models are estimated using maximum likelihood.",
            "The simpler model is nested within the more complex model.",
            "Certain regularity conditions hold for the likelihood functions."
        ]
    },
    "49. Wald Test": {
        "purpose": "A general statistical test used for assessing the significance of parameters in a statistical model (e.g., regression coefficients). Tests if a parameter is significantly different from a hypothesized value (often zero).",
        "assumptions": [
            "Parameter estimates are approximately normally distributed (often relies on large sample theory and maximum likelihood estimation).",
            "The variance-covariance matrix of the parameter estimates is known or can be consistently estimated."
        ]
    },
    "50. Score Test (Lagrange Multiplier Test)": { # Key includes alternative name
        "purpose": "Another general test for model parameters or model specification. Often used when models are harder to fit under the alternative hypothesis, as it only requires estimation under the null hypothesis.",
        "assumptions": [
            "Relies on properties of the score function (gradient of the log-likelihood).",
            "Often used for testing omitted variables or other restrictions in a model."
        ]
    }
}

def ask_question(prompt, options):
    """
    Helper function to ask a question and get a validated choice.
    Args:
        prompt (str): The question to ask the user.
        options (dict): A dictionary where keys are valid choices (e.g., 'a', '1')
                        and values are descriptions of the choices.
    Returns:
        str: The user's validated choice (key from options).
    """
    print(f"\n{prompt}")
    for key, value in options.items():
        print(f"  {key}) {value}")

    while True:
        choice = input("Your choice: ").strip().lower()
        if choice in options:
            return choice
        else:
            print(f"Invalid input. Please choose from: {', '.join(options.keys())}")

def print_recommendation(tests, notes=None):
    """Prints the recommended test(s) and their summaries."""
    if isinstance(tests, str):
        tests = [tests]
    print("\n--- Recommendation ---")
    if tests:
        print("Based on your answers, suitable test(s) might be:")
        for test_name in tests:
            print(f"\n  >>> {test_name} <<<")
            summary = TEST_SUMMARIES.get(test_name)
            if summary:
                print(f"    Purpose: {summary.get('purpose', 'N/A')}")
                if 'assumptions' in summary and summary['assumptions']:
                    print("    Key Assumptions:")
                    for assumption in summary['assumptions']:
                        print(f"      - {assumption}")
                else:
                    print("    (Key assumptions not detailed for this entry yet).")
            else:
                print(f"    (Summary for '{test_name}' is not yet available in the guide.)") # More specific error

        if any("ANOVA" in test or "Kruskal-Wallis" in test for test in tests if isinstance(test, str)):
             print("\n  NOTE: If this test is significant for 3+ groups, follow up with appropriate post-hoc tests (e.g., Tukey's HSD, Dunn's test) to identify which specific groups differ.")
    else:
        print("Could not determine a specific test with the provided path. Please review your choices or consult a statistician.")
    if notes:
        print(f"\nAdditional Notes from guide: {notes}")
    print("----------------------")
    return True

# --- Section Handlers (with corrected print_recommendation calls) ---

def handle_section_a():
    """Section A: Comparing Groups"""
    q_a1 = "A1. What is the scale of your dependent variable (the outcome you are measuring)?"
    opts_a1 = {
        '1': "Continuous (Interval/Ratio Data - e.g., blood pressure, test score)",
        '2': "Categorical (Nominal/Ordinal Data - e.g., yes/no, low/medium/high)"
    }
    choice_a1 = ask_question(q_a1, opts_a1)

    if choice_a1 == '1': # Continuous DV
        q_a1_1_1 = "A1.1.1. How many groups are you comparing?"
        opts_a1_1_1 = {
            '1': "One Group (comparing sample to a known/hypothesized population value)",
            '2': "Two Groups",
            '3': "Three or More Groups"
        }
        choice_a1_1_1 = ask_question(q_a1_1_1, opts_a1_1_1)

        if choice_a1_1_1 == '1': # One Group
            q_parametric = "Are parametric assumptions met (e.g., normality of data or differences)?"
            opts_parametric = {'y': "Yes", 'n': "No / Small sample / Ordinal-like continuous data"}
            choice_parametric = ask_question(q_parametric, opts_parametric)
            if choice_parametric == 'y':
                q_pop_var_known = "Is the population variance known?"
                opts_pop_var_known = {'y': "Yes", 'n': "No (more common)"}
                if ask_question(q_pop_var_known, opts_pop_var_known) == 'y':
                    return print_recommendation("9. Z-test (for means) (P)")
                else:
                    return print_recommendation("1. One-Sample t-test (P)")
            else:
                return print_recommendation(["11. Wilcoxon Signed-Rank Test (NP)", "14. Sign Test (NP)"])

        elif choice_a1_1_1 == '2': # Two Groups
            q_paired = "Are the samples independent or paired/related (e.g., same subject measured twice)?"
            opts_paired = {'i': "Independent Samples", 'p': "Paired/Related Samples"}
            choice_paired = ask_question(q_paired, opts_paired)

            if choice_paired == 'i': # Independent Samples
                q_parametric = "Are parametric assumptions met (normality, homogeneity of variances)?"
                opts_parametric = {'y': "Yes", 'n': "No / Ordinal data / Small samples"}
                choice_parametric = ask_question(q_parametric, opts_parametric)
                if choice_parametric == 'y':
                    q_variances = "Do you assume equal variances between the two groups (or test confirmed equality)?"
                    opts_variances = {'y': "Yes", 'n': "No (or test confirmed inequality, or unsure - prefer Welch's)"}
                    choice_variances = ask_question(q_variances, opts_variances)
                    if choice_variances == 'y':
                        return print_recommendation("2. Two-Sample (Independent) t-test (P)")
                    else:
                        return print_recommendation("3. Welch's t-test (P)")
                else:
                    return print_recommendation("10. Mann-Whitney U Test (Wilcoxon Rank-Sum Test) (NP)")
            else: # Paired Samples
                q_parametric = "Are parametric assumptions met (normality of differences)?"
                opts_parametric = {'y': "Yes", 'n': "No / Ordinal data / Small samples"}
                choice_parametric = ask_question(q_parametric, opts_parametric)
                if choice_parametric == 'y':
                    return print_recommendation("4. Paired t-test (P)")
                else:
                    return print_recommendation(["11. Wilcoxon Signed-Rank Test (NP)", "14. Sign Test (NP)"])

        elif choice_a1_1_1 == '3': # Three or More Groups
            q_related = "Are the samples independent or related (e.g., repeated measures on the same subject)?"
            opts_related = {'i': "Independent Samples", 'r': "Related Samples (Repeated Measures)"}
            choice_related = ask_question(q_related, opts_related)

            if choice_related == 'i': # Independent Samples
                q_parametric = "Are parametric assumptions met (normality within groups, homogeneity of variances)?"
                opts_parametric = {'y': "Yes", 'n': "No / Ordinal data / Small samples"}
                choice_parametric = ask_question(q_parametric, opts_parametric)

                if choice_parametric == 'y':
                    q_factors = "Are you considering just one grouping factor, or more (e.g., drug type AND gender) or a covariate?"
                    opts_factors = {
                        '1': "One grouping factor (e.g., drug type)",
                        '2': "Two (or more) grouping factors (e.g., drug type AND gender)",
                        'c': "One grouping factor AND a continuous covariate to control for"
                    }
                    choice_factors = ask_question(q_factors, opts_factors)
                    if choice_factors == '1':
                        return print_recommendation("5. One-Way ANOVA (P)")
                    elif choice_factors == '2':
                        return print_recommendation("6. Two-Way ANOVA (P) (or higher-way ANOVA)")
                    else: # 'c'
                        return print_recommendation("8. ANCOVA (Analysis of Covariance) (P)")
                else: # Non-parametric for 3+ independent groups
                    q_ordered_diff = "Do the groups have a natural ordering, and you expect a trend in medians (e.g., dose-response)?"
                    opts_ordered_diff = {'y': "Yes", 'n': "No"}
                    choice_ordered_diff = ask_question(q_ordered_diff, opts_ordered_diff)
                    if choice_ordered_diff == 'y':
                         return print_recommendation(["12. Kruskal-Wallis H Test (NP)", "15. Jonckheere-Terpstra Test (NP)"])
                    else:
                         return print_recommendation("12. Kruskal-Wallis H Test (NP)")

            else: # Related Samples (Repeated Measures) for 3+ groups
                q_parametric = "Are parametric assumptions met (sphericity for ANOVA)?"
                opts_parametric = {'y': "Yes", 'n': "No / Ordinal data"}
                choice_parametric = ask_question(q_parametric, opts_parametric)
                if choice_parametric == 'y':
                    return print_recommendation("7. Repeated Measures ANOVA (P)")
                else:
                    return print_recommendation("13. Friedman Test (NP)")

    elif choice_a1 == '2': # Categorical DV
        q_a1_2_1 = "A1.2.1. How many categorical variables/groups are involved and what's the structure?"
        opts_a1_2_1 = {
            '1': "One categorical variable (comparing observed to expected frequencies)",
            '2': "Two categorical variables (testing for association/independence)",
            '3': "More than two related categorical variables (e.g., same subject, multiple binary items)",
            'p': "Comparing proportions between two independent groups (binary outcome)"
        }
        choice_a1_2_1 = ask_question(q_a1_2_1, opts_a1_2_1)

        if choice_a1_2_1 == '1':
            q_binary = "Is the outcome binary (e.g., success/failure) and are you comparing to a known proportion?"
            opts_binary = {'y': "Yes", 'n': "No (general frequency comparison)"}
            choice_binary = ask_question(q_binary, opts_binary)
            if choice_binary == 'y':
                return print_recommendation(["22. Binomial Test", "23. Z-test for Proportions (One-sample) (Large N)"])
            else:
                return print_recommendation("17. Chi-squared (χ²) Goodness-of-Fit Test")
        elif choice_a1_2_1 == '2':
            q_paired_cat = "Are the samples for the two categorical variables independent or paired/related?"
            opts_paired_cat = {'i': "Independent", 'p': "Paired/Related"}
            choice_paired_cat = ask_question(q_paired_cat, opts_paired_cat)
            if choice_paired_cat == 'i':
                q_small_sample = "Are expected cell counts small (e.g., any cell < 5 for a 2x2 table)?"
                opts_small_sample = {'y': "Yes (consider Fisher's)", 'n': "No (Chi-squared likely appropriate)"}
                choice_small_sample = ask_question(q_small_sample, opts_small_sample)
                if choice_small_sample == 'y':
                    return print_recommendation("19. Fisher's Exact Test")
                else:
                    q_trend = "Is one variable a grouping variable and the other an ordered categorical outcome, testing for trend in proportions?"
                    opts_trend = {'y': "Yes", 'n': "No (general association)"}
                    choice_trend = ask_question(q_trend, opts_trend)
                    if choice_trend == 'y':
                        return print_recommendation(["18. Chi-squared (χ²) Test of Independence/Association", "24. Cochran-Armitage Test for Trend (for ordered trend)"])
                    else:
                        return print_recommendation("18. Chi-squared (χ²) Test of Independence/Association")
            else: # Paired
                return print_recommendation("20. McNemar's Test (for 2x2 tables, binary outcome, two related groups/times)")
        elif choice_a1_2_1 == '3':
            return print_recommendation("21. Cochran's Q Test")
        elif choice_a1_2_1 == 'p':
            return print_recommendation("23. Z-test for Proportions (Two-sample) (Large N, often equivalent to Chi-squared for 2x2)")
    return False


def handle_section_b():
    """Section B: Examining Relationships or Associations"""
    q_b1 = "B1. What are the scales of the TWO variables you are correlating/associating?"
    opts_b1 = {
        'cc': "Both Continuous (Interval/Ratio)",
        'oo': "Both Ordinal (or one/both Ordinal and assumptions for Pearson not met)",
        'nn': "Both Nominal (Categorical)",
        'cn': "One Continuous, One Nominal (Categorical with 2 levels - often like comparing means)",
        'c_cat_multi': "One Continuous, One Nominal (Categorical with 3+ levels - often like comparing means)",
    }
    choice_b1 = ask_question(q_b1, opts_b1)

    if choice_b1 == 'cc':
        q_linear = "Do you expect a linear relationship and are parametric assumptions (e.g., bivariate normality) met?"
        opts_linear = {'y': "Yes", 'n': "No (or monotonic relationship expected, or assumptions violated)"}
        choice_linear = ask_question(q_linear, opts_linear)
        if choice_linear == 'y':
            return print_recommendation("25. Pearson Correlation Coefficient (test of significance) (P)")
        else:
            return print_recommendation(["26. Spearman Rank Correlation (NP)", "27. Kendall's Tau (NP)"])
    elif choice_b1 == 'oo':
        return print_recommendation(["26. Spearman Rank Correlation (NP)", "27. Kendall's Tau (NP)"])
    elif choice_b1 == 'nn':
        q_small_sample = "Are expected cell counts small (e.g., any cell < 5 for a 2x2 table)?"
        opts_small_sample = {'y': "Yes (consider Fisher's)", 'n': "No (Chi-squared likely appropriate)"}
        choice_small_sample = ask_question(q_small_sample, opts_small_sample)
        if choice_small_sample == 'y':
            return print_recommendation("19. Fisher's Exact Test")
        else:
            return print_recommendation("18. Chi-squared (χ²) Test of Independence/Association")
    elif choice_b1 == 'cn':
        print_recommendation(
            ["2. Two-Sample (Independent) t-test (P)",
             "10. Mann-Whitney U Test (Wilcoxon Rank-Sum Test) (NP)"],
            notes="This is framed as comparing means of the continuous variable across the 2 levels of the nominal variable. Point-biserial correlation is related. Parametric assumptions apply to the t-test."
        )
        return True
    elif choice_b1 == 'c_cat_multi':
        print_recommendation(
            ["5. One-Way ANOVA (P)",
             "12. Kruskal-Wallis H Test (NP)"],
            notes="This is framed as comparing means of the continuous variable across the 3+ levels of the nominal variable. Eta-squared from ANOVA indicates association strength. Parametric assumptions apply to ANOVA."
        )
        return True
    return False

def handle_section_c():
    """Section C: Predicting an Outcome (Regression)"""
    q_c1 = "C1. What is the scale of your dependent variable (DV - the outcome you are predicting)?"
    opts_c1 = {
        '1': "Continuous (Interval/Ratio)",
        '2': "Binary (e.g., yes/no, success/failure)",
        '3': "Ordinal (e.g., low/medium/high, Likert scale)",
        '4': "Count (e.g., number of events, items)"
    }
    choice_c1 = ask_question(q_c1, opts_c1)

    if choice_c1 == '1': # Continuous DV
        q_ivs = "How many independent variables (IVs) are you using for prediction?"
        opts_ivs = {'1': "One IV", 'm': "Multiple IVs (two or more)"}
        choice_ivs = ask_question(q_ivs, opts_ivs)
        if choice_ivs == '1':
            return print_recommendation("28. Simple Linear Regression (F-test for model, t-tests for coefficients) (P)")
        else:
            return print_recommendation("29. Multiple Linear Regression (F-test for model, t-tests for coefficients) (P)")
    elif choice_c1 == '2': # Binary DV
        return print_recommendation("30. Logistic Regression (Likelihood Ratio Test, Wald Test, Score Test for model/coefficients)")
    elif choice_c1 == '3': # Ordinal DV
        return print_recommendation("33. Ordinal Logistic Regression")
    elif choice_c1 == '4': # Count DV
        q_overdispersion = "Do you suspect overdispersion (variance of counts much larger than the mean)?"
        opts_overdispersion = {'y': "Yes / Unsure (consider Negative Binomial)", 'n': "No (Poisson might be appropriate)"}
        choice_overdispersion = ask_question(q_overdispersion, opts_overdispersion)
        if choice_overdispersion == 'y':
            # Ensuring these keys match the dictionary
            return print_recommendation(["31. Poisson Regression (Likelihood Ratio Test, Wald Test, Score Test)",
                                         "32. Negative Binomial Regression (Likelihood Ratio Test, Wald Test, Score Test) (handles overdispersion)"])
        else:
            return print_recommendation("31. Poisson Regression (Likelihood Ratio Test, Wald Test, Score Test)")
    return False


def handle_section_d():
    """Section D: Assessing Distributional Fit or Checking Model Assumptions"""
    q_d1 = "D1. What are you trying to assess?"
    opts_d1 = {
        'norm': "Normality of a single sample",
        'spec': "Goodness-of-Fit to a *specific* (non-normal) distribution for continuous data",
        'cat_gof': "Goodness-of-Fit for categorical data (one variable, observed vs. expected)",
        '2samp_dist': "Comparing if two samples come from the same overall distribution",
        'autocorr': "Checking for autocorrelation (serial correlation) in time series data or regression residuals"
    }
    choice_d1 = ask_question(q_d1, opts_d1)

    if choice_d1 == 'norm':
        return print_recommendation([
            "38. Shapiro-Wilk Test",
            "40. Anderson-Darling Test",
            "39. Kolmogorov-Smirnov (K-S) Test (One-sample)",
            "41. Lilliefors Test"
        ])
    elif choice_d1 == 'spec':
        return print_recommendation([
            "39. Kolmogorov-Smirnov (K-S) Test (One-sample)",
            "40. Anderson-Darling Test"
        ])
    elif choice_d1 == 'cat_gof':
        return print_recommendation("17. Chi-squared (χ²) Goodness-of-Fit Test")
    elif choice_d1 == '2samp_dist':
        print_recommendation("39. Kolmogorov-Smirnov (K-S) Test (Two-sample) (NP)")
        q_median_test = "Are you specifically interested in testing if medians of two or more groups are equal (less powerful than Mann-Whitney/Kruskal-Wallis for location shifts, but tests overall distribution equality more broadly)?"
        opts_median_test = {'y': "Yes", 'n': "No"}
        if ask_question(q_median_test, opts_median_test) == 'y':
            print_recommendation("16. Mood's Median Test (NP)")
        return True
    elif choice_d1 == 'autocorr':
        q_where_autocorr = "Where are you checking for autocorrelation?"
        opts_where_autocorr = {
            'reg': "In regression residuals",
            'ts': "In a time series itself"
        }
        choice_where_autocorr = ask_question(q_where_autocorr, opts_where_autocorr)
        if choice_where_autocorr == 'reg':
            return print_recommendation("42. Durbin-Watson Test")
        else: # ts
            return print_recommendation("43. Ljung-Box Test (or Box-Pierce Test)")
    return False

def handle_section_e():
    """Section E: Analyzing Time-Ordered Data (Time Series Analysis)"""
    q_e1 = "E1. What is the primary goal of your time series analysis?"
    opts_e1 = {
        'autocorr': "Testing for autocorrelation (series correlated with its past values)?",
        'stationarity': "Testing for stationarity (does mean/variance change over time)?"
    }
    choice_e1 = ask_question(q_e1, opts_e1)
    if choice_e1 == 'autocorr':
        # Ensuring keys match
        return print_recommendation(["43. Ljung-Box Test (or Box-Pierce Test)", "42. Durbin-Watson Test"])
    elif choice_e1 == 'stationarity':
        return print_recommendation([
            "44. Augmented Dickey-Fuller (ADF) Test",
            "45. Kwiatkowski-Phillips-Schmidt-Shin (KPSS) Test"
        ], notes="These two tests for stationarity have opposite null hypotheses; often good to use both.")
    return False

def handle_section_f():
    """Section F: Analyzing Time-to-Event Data (Survival Analysis)"""
    q_f1 = "F1. What is your primary goal?"
    opts_f1 = {
        'compare_curves': "Comparing survival curves between two or more independent groups?",
        'model_predictors': "Modeling the effect of predictors (covariates) on survival time/hazard rate?"
    }
    choice_f1 = ask_question(q_f1, opts_f1)
    if choice_f1 == 'compare_curves':
        return print_recommendation("46. Log-Rank Test")
    elif choice_f1 == 'model_predictors':
        return print_recommendation("47. Cox Proportional Hazards Model (Wald/Likelihood Ratio tests for coefficients)")
    return False

def handle_section_g():
    """Section G: Comparing Variances/Dispersion Between Groups"""
    q_g1 = "G1. How many groups are you comparing variances for?"
    opts_g1 = {'2': "Two Groups", 'm': "Two or More Groups"}
    choice_g1 = ask_question(q_g1, opts_g1)

    if choice_g1 == '2':
        q_norm_g = "Do your data meet normality assumptions (required for F-test, less so for Levene's)?"
        opts_norm_g = {'y': "Yes (or F-test is specifically desired despite sensitivity)", 'n': "No / Unsure (prefer robust test)"}
        choice_norm_g = ask_question(q_norm_g, opts_norm_g)
        if choice_norm_g == 'y':
            return print_recommendation(["34. F-test for Equality of Variances (P)", "35. Levene's Test"])
        else:
            # CORRECTED: Ensure these strings EXACTLY match the dictionary keys
            return print_recommendation(["35. Levene's Test", "37. Brown-Forsythe Test"])
    elif choice_g1 == 'm': # Two or more groups
        q_norm_g_multi = "Do your data meet normality assumptions (required for Bartlett's, less so for Levene's)?"
        opts_norm_g_multi = {'y': "Yes (or Bartlett's is specifically desired despite sensitivity)", 'n': "No / Unsure (prefer robust test)"}
        choice_norm_g_multi = ask_question(q_norm_g_multi, opts_norm_g_multi)
        if choice_norm_g_multi == 'y':
             # CORRECTED: Ensure these strings EXACTLY match the dictionary keys
             return print_recommendation(["36. Bartlett's Test (P)", "35. Levene's Test", "37. Brown-Forsythe Test"])
        else:
            # CORRECTED: Ensure these strings EXACTLY match the dictionary keys
            return print_recommendation(["35. Levene's Test", "37. Brown-Forsythe Test"])
    return False

def handle_section_h():
    """Section H: General Model Comparison or Parameter Testing"""
    q_h1 = "H1. What is your specific need?"
    opts_h1 = {
        'nested': "Comparing the fit of two nested statistical models (one model is simpler version of other)?",
        'params': "Testing the significance of one or more parameters in a statistical model (e.g., regression coefficients)?"
    }
    choice_h1 = ask_question(q_h1, opts_h1)
    if choice_h1 == 'nested':
        return print_recommendation("48. Likelihood Ratio Test (LRT)")
    elif choice_h1 == 'params':
        return print_recommendation([
            "49. Wald Test",
            "50. Score Test (Lagrange Multiplier Test)"
        ])
    return False

def guide_to_statistical_test():
    """
    Guides a user through a series of questions to help them choose an
    appropriate statistical test for their research.

    IMPORTANT NOTES:
    *   Assumptions are Key: Always check the assumptions of the chosen test.
        Violating assumptions can lead to incorrect conclusions.
    *   Sample Size: Some tests are better suited for small or large sample sizes.
        This guide provides some hints, but it's a critical consideration.
    *   Post-Hoc Tests: If an ANOVA or Kruskal-Wallis test is significant for 3+ groups,
        you'll need post-hoc tests (e.g., Tukey's, Dunn's) to see *which* specific
        groups differ. These aren't listed as separate primary tests but are crucial follow-ups.
    *   Multiple Comparisons: If you perform many tests, the chance of a false positive
        (Type I error) increases. Consider adjustments like Bonferroni correction or
        False Discovery Rate (FDR) control.
    *   This is a Guide: Complex research designs might require more nuanced choices
        or combinations of tests. When in doubt, consult a statistician.
    *   Effect Size: Significance (p-value) doesn't tell you the magnitude or
        practical importance of an effect. Always report and interpret effect sizes.
    *   Data Exploration: Before testing, always explore your data visually
        (histograms, boxplots, scatterplots) and with descriptive statistics.
    *   (P) indicates a Parametric test, (NP) indicates a Non-Parametric test in test names where relevant.
    """
    print("\nWelcome to the Statistical Test Guide!")
    print("Let's find a suitable test for your data.")
    print("Claudio Gelmi (2025) @  https://github.com/cagelmi")
    print("-" * 51)
    print(guide_to_statistical_test.__doc__) # Print the docstring with notes
    print("-" * 80)


    q_main = "1. What is your primary research goal?"
    opts_main = {
        'a': "Comparing groups (means, medians, proportions)",
        'b': "Examining relationships or associations between variables",
        'c': "Predicting an outcome based on predictor variables (Regression)",
        'd': "Assessing distributional fit or checking model assumptions",
        'e': "Analyzing time-ordered data (Time Series Analysis)",
        'f': "Analyzing time-to-event data (Survival Analysis)",
        'g': "Comparing variances/dispersion between groups",
        'h': "General model comparison or parameter testing"
    }
    main_choice = ask_question(q_main, opts_main)

    recommendation_made = False

    if main_choice == 'a':
        recommendation_made = handle_section_a()
    elif main_choice == 'b':
        recommendation_made = handle_section_b()
    elif main_choice == 'c':
        recommendation_made = handle_section_c()
    elif main_choice == 'd':
        recommendation_made = handle_section_d()
    elif main_choice == 'e':
        recommendation_made = handle_section_e()
    elif main_choice == 'f':
        recommendation_made = handle_section_f()
    elif main_choice == 'g':
        recommendation_made = handle_section_g()
    elif main_choice == 'h':
        recommendation_made = handle_section_h()

    if not recommendation_made:
        print("\nNo specific test identified for this path yet, or the path is incomplete in this guide.")
        print("Please review your choices or consult a statistician for complex scenarios.")

    print("\nEnd of consultation. Remember to verify test assumptions and consider effect sizes!")
    input("\nPress Enter to close this window...") 

if __name__ == "__main__":
    guide_to_statistical_test()
