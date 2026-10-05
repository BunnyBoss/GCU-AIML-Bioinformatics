---
course_code: 02BMSBI24365
course_title: AI and ML in Bioinformatics
assessment_title: Mid-Term Comprehensive Assessment Quiz (Days 01–10 Synthesis)
scheduled_session: Session 10 (Day 10)
duration: 20 minutes
total_questions: 18
total_marks: 18
ai_tier: "Tier 1: No AI"
---

# 📝 Comprehensive Synthesis Assessment Quiz (Days 01–10)

**Course Code:** `02BMSBI24365` — AI and ML in Bioinformatics  
**Programme:** M.Sc. Bioinformatics (Semester III)  
**Scheduled Administration:** Day 10 (20 Minutes)  
**Total Marks:** 18 Marks (1 Mark per Question)  
**Assessment Tier:** **Tier 1: No AI** (Closed-book, unaided individual assessment)  

**Instructions:**
* Select the single best answer for each question.
* Calculators are permitted for basic arithmetic.
* The questions are designed to test your understanding of machine learning concepts in biological contexts.

---

## Part 1: Conceptual Theory & Deep Thinking (~75% Weightage — 12 Questions)

### Question 1: Machine Learning Taxonomy & Problem Formulation
A biology research team collects gene expression measurements from 300 tumor samples. They have two computational goals:
1. Group the unlabeled tumor samples into new, undiscovered biological subtypes based on pattern similarity.
2. Predict the cancer stage (Stage 1, 2, 3, or 4) for each patient from their cell size and shape measurements.

Which machine learning paradigms correctly classify these two goals?

- **A)** Goal 1 is Supervised Regression; Goal 2 is Unsupervised Dimensionality Reduction.
- **B)** Goal 1 is Unsupervised Clustering; Goal 2 is Supervised Multi-Class Classification.
- **C)** Goal 1 is Supervised Binary Classification; Goal 2 is Reinforcement Learning.
- **D)** Goal 1 is Unsupervised PCA; Goal 2 is Supervised Continuous Regression.

---

### Question 2: Data Preprocessing & Missing Value Imputation
In a hospital dataset of 500 patients, `blood_glucose_level` is missing for 4% of the patients. A few patients in the study have severe medical emergencies with extreme high sugar spikes ($>500\text{ mg/dL}$), making the distribution heavily skewed.

Why is replacing these missing values with the column **mean** a bad idea, and what is the better statistical choice?

- **A)** The mean cannot be calculated for biological data; mode should always be used.
- **B)** The mean is pulled up by the extreme high outliers and will artificially inflate the imputed values for normal patients; the **median** should be used because it represents a robust middle value.
- **C)** Imputing with the mean produces negative numbers; Min-Max scaling should precede mean imputation.
- **D)** The mean can only be used when less than 1% of values are missing.

---

### Question 3: Feature Scaling & Multi-Omics Transformations
You are preparing biological data for a machine learning model:
* **Feature Set A:** Gene expression counts with a huge range (values spread from $0$ all the way to $250{,}000+$) where most values are small but a few are extremely large.
* **Feature Set B:** Blood protein measurements that contain genuine, extreme high spikes (real biological outliers).

Which pair of transformations is the best choice?

- **A)** Apply $Z$-score standardization (`StandardScaler`) to gene counts, and Min-Max scaling ($[0, 1]$) to protein measurements.
- **B)** Apply a $\log_2(\text{count} + 1)$ transform to compress the huge spread of gene counts, and use `RobustScaler` (median and IQR) on protein measurements so outliers do not crush the normal values.
- **C)** Set all gene counts above 100 to zero, and apply one-hot encoding to protein measurements.
- **D)** No transformations are needed because ML models automatically ignore scale differences.

---

### Question 4: Diagnostic Metrics & Asymmetric Clinical Costs
You are training a machine learning model to screen healthy people for a deadly cancer during routine checkups:
* Missing a cancer patient (**False Negative**) is fatal because the disease will go untreated.
* Falsely flagging a healthy person (**False Positive**) only requires a quick, harmless follow-up scan to confirm they are healthy.

Which classification evaluation metric is most critical to maximize?

- **A)** **Precision**, to make sure every positive alert is 100% guaranteed to be cancer.
- **B)** **Specificity**, to reduce the number of healthy people getting follow-up scans.
- **C)** **Recall (Sensitivity)**, to avoid missing any true cancer cases and prevent fatal False Negatives.
- **D)** **Negative Predictive Value**, because it ignores positive cases entirely.

---

### Question 5: The Accuracy Paradox under Class Imbalance
A screening test looks for a rare disease gene found in only $0.5\%$ of the population (50 sick people out of 10,000). A lazy model simply predicts "Healthy / No Disease" for every single person.

What are the **Accuracy** and the **Recall (Sensitivity)** of this model?

- **A)** Accuracy $= 50.0\%$, Recall $= 50.0\%$
- **B)** Accuracy $= 99.5\%$, Recall $= 0.0\%$
- **C)** Accuracy $= 0.5\%$, Recall $= 99.5\%$
- **D)** Accuracy $= 99.5\%$, Recall $= 99.5\%$

---

### Question 6: Unsupervised Learning & PCA Scale Invariance
You run Principal Component Analysis (PCA) on tumor cell measurements without scaling the data first:
* `cell_area`: numbers range from $300$ to $2500$ (variance $\approx 120{,}000$).
* `membrane_roughness`: numbers range from $0.05$ to $0.16$ (variance $\approx 0.0002$).

What will happen to Principal Component 1 (PC1)?

- **A)** PC1 will give equal importance to both features because PCA scales features automatically.
- **B)** PC1 will be completely dominated by `cell_area` simply because its numbers have much larger variance, making PCA practically blind to `membrane_roughness`.
- **C)** PCA will crash with an error.
- **D)** PC1 will ignore `cell_area` because large numbers cause mathematical errors.

---

### Question 7: Residual Geometry in Linear Regression
A linear regression model predicts patient survival time (in months). A patient actually survived for $y = 24.0\text{ months}$, but the model predicted $\hat{y} = 30.0\text{ months}$.

What is the residual error for this patient, and what does it represent on a scatter plot?

- **A)** $+6.0\text{ months}$; the shortest diagonal distance from the point to the line.
- **B)** $-6.0\text{ months}$; the vertical distance along the $y$-axis from the actual data point to the fitted line.
- **C)** $+6.0\text{ months}$; the horizontal distance along the $x$-axis.
- **D)** $-6.0\text{ months}$; the error in the line's slope.

---

### Question 8: Biomarker Weight Sign & Clinical Risk Interpretation
A linear regression model is trained on standardized gene expression data to predict a patient's **Disease Severity Score** (where higher scores mean worse disease):

$$\text{Predicted Severity} = -2.5 \cdot \text{Gene}_1 + 3.5 \cdot \text{Gene}_2 + 0.8 \cdot \text{Gene}_3 + 12.0$$

Which statement correctly describes how $\text{Gene}_1$ and $\text{Gene}_2$ affect disease severity?

- **A)** $\text{Gene}_1$ is the main risk factor because negative weights mean bad mutations.
- **B)** $\text{Gene}_2$ is a risk factor ($w = +3.5$) because higher expression increases the disease score, while $\text{Gene}_1$ is protective ($w = -2.5$) because higher expression decreases the disease score.
- **C)** Both genes are equal risk factors because only the absolute number matters in regression.
- **D)** $\text{Gene}_3$ is the main driver because decimal numbers represent high biological importance.

---

### Question 9: Inverting the Clinical Target Endpoint
Suppose the same model equation from Question 8 is now used to predict **Patient Survival Time (in months)** instead of disease severity:

$$\text{Predicted Survival Months} = -2.5 \cdot \text{Gene}_1 + 3.5 \cdot \text{Gene}_2 + 0.8 \cdot \text{Gene}_3 + 48.0$$

Now that the goal is predicting how long a patient lives, which gene is the dangerous **risk factor**, and why?

- **A)** $\text{Gene}_2$, because its positive weight has the biggest size.
- **B)** $\text{Gene}_3$, because positive numbers extend life.
- **C)** $\text{Gene}_1$, because its negative weight ($w = -2.5$) means higher expression is linked to shorter survival time (patients die sooner).
- **D)** The answer does not change; $\text{Gene}_2$ is always the risk factor regardless of what is being predicted.

---

### Question 10: Multidimensional Dot Product Calculation ($\mathbf{w}^T \mathbf{x} + b$)
A linear regression model has learned the following weights for three standardized blood tests $[\text{Test}_A, \text{Test}_B, \text{Test}_C]$:
* Weights: $\mathbf{w} = [2.0, -1.5, 0.5]$
* Intercept (bias): $b = 1.0$

A new patient has test values $\mathbf{x} = [1.0, -2.0, 4.0]$. Using the formula $\hat{y} = \mathbf{w}^T \mathbf{x} + b = \sum_{j=1}^p w_j x_j + b$, what is the predicted value for this patient?

- **A)** $6.0$
- **B)** $7.0$
- **C)** $8.0$
- **D)** $2.0$

---

### Question 11: Polynomial Regression & Saturation Kinetics
When modeling how a drug works at different doses, the response naturally flattens out at high doses (saturation curve).

Why is a **Degree 3 (cubic)** curve usually better than a **Degree 1 (straight line)** or a **Degree 10 (complex high-order polynomial)**?

- **A)** Degree 1 models flattening curves well, while Degree 3 always underfits.
- **B)** Degree 1 underfits because a straight line cannot bend to show a flattening curve; Degree 10 overfits by wiggling wildly to connect noisy lab data points. Degree 3 bends smoothly to fit the natural curve.
- **C)** Degree 10 is always the best choice because higher degrees always give better predictions on new patients.
- **D)** Scikit-learn cannot calculate curves higher than Degree 3.

---

### Question 12: Regression Metrics & Fatal Clinical Outliers
A machine learning model predicts the radiation dose for cancer treatment. For almost every patient, the model is off by only a small amount ($\pm 0.5\text{ units}$). But for one patient, the model makes a huge mistake of $15.0\text{ units}$ (a dangerous, lethal overdose).

Which regression evaluation metric punishes this single large mistake the most, and why?

- **A)** **Mean Absolute Error (MAE)**, because it adds up error distances directly without changing them.
- **B)** **Root Mean Squared Error (RMSE)**, because squaring the errors ($(15)^2 = 225$) gives huge penalties to big mistakes.
- **C)** **$R^2$ Score**, because it only looks at small mistakes.
- **D)** Neither, because MAE and RMSE always give the exact same numbers.

---

## Part 2: Scikit-Learn Syntax & Code Implementation (~25–30% Weightage — 6 Questions)

### Question 13: Core Estimator Training Method
In Scikit-Learn, which method is used to train a machine learning model (such as `LinearRegression`, `LogisticRegression`, or `KMeans`) on training data `X_train` and labels `y_train`?

- **A)** `model.predict(X_train, y_train)`
- **B)** `model.transform(X_train, y_train)`
- **C)** `model.fit(X_train, y_train)`
- **D)** `model.train(X_train, y_train)`

---

### Question 14: Data Preprocessing & Imputation Syntax
You want to replace missing continuous values in a patient feature table using the column median in Scikit-Learn. Which code snippet correctly does this?

- **A)**  
  ```python
  from sklearn.impute import SimpleImputer
  imputer = SimpleImputer(strategy='median')
  X_clean = imputer.fit_transform(X_train)
  ```
- **B)**  
  ```python
  from sklearn.preprocessing import MissingValueImputer
  X_clean = MissingValueImputer(metric='median').fit(X_train)
  ```
- **C)**  
  ```python
  from sklearn.clean import ImputeTable
  X_clean = ImputeTable().fit_transform(X_train)
  ```
- **D)**  
  ```python
  from sklearn.impute import FillNaN
  X_clean = FillNaN(method='median').transform(X_train)
  ```

---

### Question 15: Model Inference & Generating Predictions
After fitting a machine learning model named `model` on training data, which Scikit-Learn method is used to generate predictions on unseen test samples `X_test`?

- **A)** `model.predict(X_test)`
- **B)** `model.evaluate(X_test)`
- **C)** `model.forecast(X_test)`
- **D)** `model.run(X_test)`

---

### Question 16: Splitting Data into Train and Test Sets
Which Scikit-Learn function is used to randomly divide feature matrix `X` and target labels `y` into training and testing subsets?

- **A)** `from sklearn.data import split_samples`
- **B)** `from sklearn.preprocessing import partition_data`
- **C)** `from sklearn.model_selection import train_test_split`
- **D)** `from sklearn.metrics import split_train_test`

---

### Question 17: Accessing Learned Regression Coefficients (Weights)
After training a `LinearRegression` model object named `model` on gene expression features, which attribute holds the learned feature weights ($w_1, w_2, \dots, w_p$)?

- **A)** `model.weights_`
- **B)** `model.parameters_`
- **C)** `model.coef_`
- **D)** `model.slopes_`

---

### Question 18: Evaluating Model Performance (Accuracy)
Which Scikit-Learn function from `sklearn.metrics` is used to calculate classification accuracy by comparing ground-truth test labels `y_test` against predicted labels `y_pred`?

- **A)** `accuracy_score(y_test, y_pred)`
- **B)** `calculate_accuracy(y_test, y_pred)`
- **C)** `classification_rate(y_test, y_pred)`
- **D)** `eval_correctness(y_test, y_pred)`

---
**End of Assessment Quiz**
