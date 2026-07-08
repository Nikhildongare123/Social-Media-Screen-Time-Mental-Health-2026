# 📱 Social Media Screen Time & Mental Well-being Analysis

## 📌 Project Overview

This project analyzes how social media usage impacts users' mental well-being. The analysis explores relationships between screen time, sleep duration, anxiety, loneliness, self-esteem, FOMO, and life satisfaction using Exploratory Data Analysis (EDA) and Machine Learning.

The project demonstrates the complete Data Science workflow, including data cleaning, visualization, feature engineering, model building, and prediction.

---

## 🎯 Business Problem

Excessive social media usage has become a major concern affecting people's mental health.

The objective of this project is to:

- Analyze social media usage patterns.
- Identify factors affecting mental well-being.
- Discover relationships between screen time and mental health.
- Predict users' Well-being Band using Machine Learning.

---

## 📂 Project Structure

```
Social Media Screen Time & Mental Well-being Analysis
│
├── Data
│   └── social_media_screentime_mental_health.csv
│
├── Notebook
│   ├── 01_Data_Cleaning.ipynb
│   └── logistic_regression_model.pkl
│
└── README.md
```

---

# 📊 Dataset Information

**Rows:** 7000

**Columns:** 25

### Important Features

- Age
- Gender
- Occupation
- Region
- Most Used Platform
- Daily Screen Hours
- Daily Notifications
- Night Time Use
- Sleep Hours
- Anxiety Score
- Low Mood Score
- Life Satisfaction
- Loneliness
- Self Esteem
- FOMO
- Social Comparison
- Physical Activity
- Digital Detox
- Mental Health Support
- Wellbeing Band (Target)

---

# 🧹 Data Cleaning

Performed the following preprocessing steps:

- Checked missing values
- Filled missing values
- Removed duplicate records
- Corrected data types
- Feature Engineering
- Created Sleep Category
- Created Screen Time Category
- Label Encoding
- Feature Scaling

---

# 📈 Exploratory Data Analysis (EDA)

Performed detailed analysis including:

- Age Distribution
- Gender Distribution
- Occupation Analysis
- Most Used Platform
- Daily Screen Time Distribution
- Sleep Hours Distribution
- Anxiety Score Analysis
- Correlation Heatmap
- Boxplots
- Scatterplots
- Groupby Analysis
- Crosstab Analysis

---

# 🤖 Machine Learning

## Target Variable

**Wellbeing Band**

### Model Used

- Logistic Regression

### Workflow

- Data Cleaning
- Feature Engineering
- Label Encoding
- Train-Test Split
- Standard Scaling
- Model Training
- Prediction
- Model Evaluation

---

# 📊 Evaluation Metrics

- Accuracy
- Precision
- Confusion Matrix
- Classification Report

---

# 📦 Model File

The trained model is saved as:

```
logistic_regression_model.pkl
```

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Jupyter Notebook

---

# 📚 Key Business Insights

- Higher screen time is associated with increased anxiety.
- Night-time social media usage is linked with lower sleep duration.
- Better sleep is associated with higher life satisfaction.
- Higher FOMO is strongly related to social comparison.
- Digital detox participants generally show better mental well-being.
- Physical activity positively influences overall well-being.

---

# 👨‍💻 Author

**Nikhil Dongare**

- Aspiring Data Scientist
- Python | SQL | Power BI | Machine Learning

---

## ⭐ If you found this project helpful, don't forget to Star the repository!
