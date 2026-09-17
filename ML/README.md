# Machine Learning Roadmap

A hands-on guide to the machine-learning workflow: prepare data, train models, evaluate results, tune performance, and turn models into useful projects.

> **Course focus:** Understand the ideas behind common algorithms and implement them with Python, NumPy, Pandas, and scikit-learn.

## At A Glance

| Stage | Coverage |
| --- | --- |
| Foundations | ML concepts, terminology, preprocessing, supervised and unsupervised learning |
| Supervised Learning | KNN, regression, logistic regression, SVM, decision trees, and ensembles |
| Model Quality | Metrics, cross-validation, grid search, and randomized search |
| Unsupervised Learning | K-means, hierarchical clustering, elbow plots, and silhouette scores |
| Advanced Topics | Recommendation systems, NLP, PCA, and OpenCV |
| Projects | Python and SQL, Python and ML, and Power BI reporting projects |

## Contents

- [Setup](#setup)
- [Introduction to Machine Learning](#introduction-to-machine-learning)
- [Data Preprocessing](#data-preprocessing)
- [Supervised and Unsupervised Learning](#supervised-and-unsupervised-learning)
- [KNN Classification](#knn-classification)
- [Performance Metrics](#performance-metrics)
- [Regression](#regression)
- [Logistic Regression](#logistic-regression)
- [Support Vector Machines](#support-vector-machines)
- [Decision Trees](#decision-trees)
- [Ensemble Learning](#ensemble-learning)
- [Model Selection](#model-selection)
- [Recommendation Systems](#recommendation-systems)
- [Clustering](#clustering)
- [Text Analysis](#text-analysis)
- [Dimensionality Reduction](#dimensionality-reduction)
- [OpenCV](#opencv)
- [Project Ideas](#project-ideas)

## Setup

Install the libraries used in the examples:

```bash
python -m pip install numpy pandas matplotlib seaborn scikit-learn scipy nltk opencv-python
```

Common imports:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
```

## Introduction to Machine Learning

Traditional programming uses explicit rules and data to produce results. Machine learning learns patterns from examples and uses those patterns to make predictions.

### Typical ML Workflow

1. Define the business or scientific problem.
2. Collect and understand the data.
3. Clean and preprocess the data.
4. Split data into training and testing sets.
5. Select a baseline model.
6. Train the model on the training data.
7. Evaluate it with suitable metrics.
8. Tune hyperparameters and compare models.
9. Save, deploy, and monitor the model.

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

iris = load_iris(as_frame=True)
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42, stratify=iris.target
)

model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, predictions))
```

### Common Terminology

- **Feature:** An input column used for prediction.
- **Target:** The output the model learns to predict.
- **Sample:** One observation or row.
- **Training data:** Data used to learn model parameters.
- **Testing data:** Unseen data used for evaluation.
- **Parameter:** A value learned during training.
- **Hyperparameter:** A setting chosen before training.
- **Overfitting:** Excellent training performance but poor generalization.
- **Underfitting:** The model is too simple to capture the pattern.

## Data Preprocessing

Preprocessing keeps training and testing transformations consistent. Use a `Pipeline` and `ColumnTransformer` to reduce leakage and make the workflow reproducible.

```python
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

numeric_features = ["age", "income"]
categorical_features = ["city", "membership"]

preprocessor = ColumnTransformer([
    ("numeric", Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ]), numeric_features),
    ("categorical", Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore")),
    ]), categorical_features),
])
```

## Supervised and Unsupervised Learning

### Supervised Learning

The dataset contains labeled targets. Classification predicts categories, while regression predicts continuous values.

```python
from sklearn.linear_model import LinearRegression, LogisticRegression

classification_model = LogisticRegression(max_iter=1000)
regression_model = LinearRegression()
```

### Unsupervised Learning

The dataset has no target column. Clustering discovers groups, while dimensionality reduction creates a smaller representation of the features.

```python
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

clusters = KMeans(n_clusters=3, random_state=42, n_init=10)
compact_representation = PCA(n_components=2, random_state=42)
```

## KNN Classification

K-Nearest Neighbors classifies a sample using the labels of nearby training samples. Scaling is important because distance is affected by feature magnitude.

### KNN Implementation

```python
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42, stratify=iris.target
)

knn = make_pipeline(
    StandardScaler(),
    KNeighborsClassifier(n_neighbors=5, weights="distance", metric="minkowski"),
)
knn.fit(X_train, y_train)
print("KNN accuracy:", knn.score(X_test, y_test))
```

Important KNN hyperparameters include `n_neighbors`, `weights`, `metric`, and `p`. Test several values rather than assuming that five neighbors is always best.

## Performance Metrics

### Classification Metrics

```python
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)

predictions = knn.predict(X_test)
print("Confusion matrix:\n", confusion_matrix(y_test, predictions))
print("Accuracy:", accuracy_score(y_test, predictions))
print("Precision:", precision_score(y_test, predictions, average="weighted"))
print("Recall:", recall_score(y_test, predictions, average="weighted"))
print("F1:", f1_score(y_test, predictions, average="weighted"))
print(classification_report(y_test, predictions))
```

- **Accuracy:** Fraction of all predictions that are correct.
- **Precision:** Of predicted positives, how many are truly positive.
- **Recall:** Of actual positives, how many were found.
- **F1 score:** Harmonic mean of precision and recall.
- **Confusion matrix:** Counts true positives, true negatives, false positives, and false negatives.

Accuracy can be misleading for imbalanced classes, so inspect precision, recall, F1, and the confusion matrix together.

### Regression Metrics

```python
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

actual = np.array([3, 5, 7, 9])
predicted = np.array([2.5, 5.5, 6.5, 8.5])

print("MAE:", mean_absolute_error(actual, predicted))
print("MSE:", mean_squared_error(actual, predicted))
print("RMSE:", np.sqrt(mean_squared_error(actual, predicted)))
print("R2:", r2_score(actual, predicted))
```

## Regression

Regression predicts continuous values. The model learns coefficients that minimize a loss function such as mean squared error.

### Simple Linear Regression

```python
from sklearn.linear_model import LinearRegression

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 5, 8, 10])

simple_model = LinearRegression()
simple_model.fit(X, y)
print("Slope:", simple_model.coef_[0])
print("Intercept:", simple_model.intercept_)
print("Prediction:", simple_model.predict([[6]]))
```

### Multiple Linear Regression

```python
X = pd.DataFrame({
    "area": [800, 1000, 1200, 1500, 1800],
    "bedrooms": [1, 2, 2, 3, 3],
})
y = np.array([40, 55, 65, 82, 95])

multiple_model = LinearRegression().fit(X, y)
print(multiple_model.predict([[1300, 2]]))
```

### Polynomial Regression

Polynomial regression adds powers of input features to model curved relationships.

```python
from sklearn.preprocessing import PolynomialFeatures

polynomial_model = Pipeline([
    ("features", PolynomialFeatures(degree=2, include_bias=False)),
    ("regressor", LinearRegression()),
])

polynomial_model.fit(X[["area"]], y)
print(polynomial_model.predict([[1300]]))
```

### Housing Price Prediction

The original Boston Housing dataset has been removed from modern scikit-learn versions because of ethical and data-quality concerns. Use California Housing for a current regression exercise:

```python
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

housing = fetch_california_housing(as_frame=True)
X_train, X_test, y_train, y_test = train_test_split(
    housing.data, housing.target, test_size=0.2, random_state=42
)

housing_model = Pipeline([
    ("scaler", StandardScaler()),
    ("regressor", LinearRegression()),
])
housing_model.fit(X_train, y_train)
print("Housing R2:", housing_model.score(X_test, y_test))
```

### Cost and Loss Functions

```python
def mean_absolute_error_manual(actual, predicted):
    return np.mean(np.abs(actual - predicted))


def mean_squared_error_manual(actual, predicted):
    return np.mean((actual - predicted) ** 2)


def root_mean_squared_error_manual(actual, predicted):
    return np.sqrt(mean_squared_error_manual(actual, predicted))


def least_square_error(actual, predicted):
    return np.sum((actual - predicted) ** 2)
```

MAE is less sensitive to outliers. MSE penalizes large errors more heavily. RMSE returns the error in the target's original units. Least-squares fitting minimizes the sum of squared residuals.

### Regularization

Regularization discourages overly complex models. Ridge uses an L2 penalty and Lasso uses an L1 penalty.

```python
from sklearn.linear_model import Ridge, Lasso

ridge_model = Pipeline([
    ("scaler", StandardScaler()),
    ("model", Ridge(alpha=1.0)),
])

lasso_model = Pipeline([
    ("scaler", StandardScaler()),
    ("model", Lasso(alpha=0.1)),
])
```

## Logistic Regression

Logistic regression estimates class probabilities with the sigmoid function for binary classification. Multiclass problems can use one-vs-rest or multinomial strategies.

### Sigmoid and Softmax

```python
def sigmoid(value):
    return 1 / (1 + np.exp(-value))


def softmax(values):
    shifted = values - np.max(values)
    probabilities = np.exp(shifted)
    return probabilities / probabilities.sum()

print(sigmoid(1.5))
print(softmax(np.array([2.0, 1.0, 0.5])))
```

### Binary and Multiclass Classification

```python
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42, stratify=iris.target
)

logistic_model = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression(max_iter=1000, multi_class="auto")),
])
logistic_model.fit(X_train, y_train)
print(logistic_model.predict_proba(X_test[:2]))
```

The same pattern can be used with the Titanic dataset after handling missing values and encoding categorical columns.

## Support Vector Machines

SVMs find a decision boundary with a large margin. Kernels allow nonlinear boundaries.

```python
from sklearn.svm import SVC

svm_model = Pipeline([
    ("scaler", StandardScaler()),
    ("model", SVC(kernel="rbf", C=1.0, gamma="scale", probability=True)),
])
svm_model.fit(X_train, y_train)
print("SVM accuracy:", svm_model.score(X_test, y_test))
```

- `kernel` controls the transformation, such as `linear`, `poly`, or `rbf`.
- `C` controls the penalty for misclassification.
- `gamma` controls the influence of a training example for RBF and other nonlinear kernels.

## Decision Trees

Decision trees split features into increasingly pure nodes. Splits can be selected with criteria such as Gini impurity or entropy.

```python
from sklearn.tree import DecisionTreeClassifier, plot_tree

tree_model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    min_samples_split=4,
    random_state=42,
)
tree_model.fit(X_train, y_train)

plt.figure(figsize=(14, 8))
plot_tree(tree_model, feature_names=iris.feature_names, filled=True)
plt.show()
```

The model's `max_depth`, `min_samples_leaf`, and `min_samples_split` help control overfitting.

## Ensemble Learning

Ensembles combine multiple models to improve stability or predictive power.

### Random Forest

```python
from sklearn.ensemble import RandomForestClassifier

forest_model = RandomForestClassifier(
    n_estimators=200,
    max_depth=6,
    random_state=42,
    n_jobs=-1,
)
forest_model.fit(X_train, y_train)
print(forest_model.score(X_test, y_test))
```

### Bagging and Boosting

```python
from sklearn.ensemble import BaggingClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier

bagging_model = BaggingClassifier(
    estimator=DecisionTreeClassifier(max_depth=4),
    n_estimators=100,
    random_state=42,
)
boosting_model = GradientBoostingClassifier(random_state=42)

bagging_model.fit(X_train, y_train)
boosting_model.fit(X_train, y_train)
```

### Voting Classifier

```python
from sklearn.ensemble import VotingClassifier

voting_model = VotingClassifier(
    estimators=[
        ("logistic", logistic_model),
        ("svm", svm_model),
        ("forest", forest_model),
    ],
    voting="hard",
)
voting_model.fit(X_train, y_train)
print(voting_model.score(X_test, y_test))
```

## Model Selection

### Cross-Validation

```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(logistic_model, iris.data, iris.target, cv=5, scoring="accuracy")
print("Fold scores:", scores)
print("Average score:", scores.mean())
```

### Grid Search

```python
from sklearn.model_selection import GridSearchCV

parameter_grid = {
    "model__C": [0.1, 1, 10],
    "model__solver": ["lbfgs"],
}

grid_search = GridSearchCV(logistic_model, parameter_grid, cv=5, scoring="accuracy")
grid_search.fit(iris.data, iris.target)
print(grid_search.best_params_)
print(grid_search.best_score_)
```

### Randomized Search

```python
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import loguniform

random_search = RandomizedSearchCV(
    svm_model,
    {"model__C": loguniform(0.01, 100), "model__gamma": ["scale", "auto"]},
    n_iter=10,
    cv=5,
    random_state=42,
)
random_search.fit(iris.data, iris.target)
print(random_search.best_params_)
```

## Recommendation Systems

### Content-Based Recommendation

Recommend items with similar feature vectors using cosine similarity.

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

items = pd.DataFrame({
    "title": ["Python Basics", "Advanced Python", "SQL Fundamentals"],
    "description": [
        "python programming variables loops",
        "python classes decorators modules",
        "sql database tables queries",
    ],
})

vectorizer = TfidfVectorizer()
features = vectorizer.fit_transform(items["description"])
similarity = cosine_similarity(features)

recommendations = similarity[0].argsort()[::-1][1:]
print(items.iloc[recommendations]["title"].tolist())
```

### Collaborative Filtering

Collaborative filtering uses user-item interactions instead of item descriptions.

```python
ratings = pd.DataFrame({
    "user": ["A", "A", "B", "B", "C"],
    "item": ["Python", "SQL", "Python", "Power BI", "SQL"],
    "rating": [5, 3, 4, 5, 4],
})

user_item = ratings.pivot_table(index="user", columns="item", values="rating")
user_similarity = user_item.T.corr(method="pearson")
print(user_similarity)
```

For a production recommender, evaluate recommendations with a held-out set and metrics such as precision at `k`, recall at `k`, and mean average precision.

### Classification-Based Recommendations

A classification model can predict whether a user will like or click an item:

```python
from sklearn.ensemble import RandomForestClassifier

features = ratings[["rating"]]
target = (ratings["rating"] >= 4).astype(int)
recommendation_model = RandomForestClassifier(random_state=42)
recommendation_model.fit(features, target)
```

## Clustering

### K-Means Clustering

K-means assigns records to the nearest centroid and updates centroids repeatedly.

```python
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris

iris = load_iris()
kmeans = Pipeline([
    ("scaler", StandardScaler()),
    ("model", KMeans(n_clusters=3, random_state=42, n_init=10)),
])
labels = kmeans.fit_predict(iris.data)
print(labels[:10])
```

### Elbow Technique and Silhouette Coefficient

```python
from sklearn.metrics import silhouette_score

inertias = []
silhouette_scores = []
for cluster_count in range(2, 8):
    model = KMeans(n_clusters=cluster_count, random_state=42, n_init=10)
    labels = model.fit_predict(iris.data)
    inertias.append(model.inertia_)
    silhouette_scores.append(silhouette_score(iris.data, labels))

plt.plot(range(2, 8), inertias, marker="o")
plt.title("Elbow Curve")
plt.xlabel("Number of clusters")
plt.ylabel("Inertia")
plt.show()

print("Silhouette scores:", silhouette_scores)
```

### Hierarchical Clustering and Dendrogram

```python
from scipy.cluster.hierarchy import dendrogram, linkage

linkage_matrix = linkage(StandardScaler().fit_transform(iris.data), method="ward")
dendrogram(linkage_matrix, truncate_mode="level", p=4)
plt.title("Hierarchical Clustering Dendrogram")
plt.show()
```

## Text Analysis

Install NLTK data once before using tokenizers or stop words:

```python
import nltk

nltk.download("punkt")
nltk.download("stopwords")
```

### Tokenization and Stop Words

```python
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

text = "Machine learning is useful. It finds patterns in data."
sentences = sent_tokenize(text)
words = word_tokenize(text.lower())
stop_words = set(stopwords.words("english"))
filtered_words = [word for word in words if word.isalpha() and word not in stop_words]

print(sentences)
print(filtered_words)
```

Customize stop words by extending the set:

```python
stop_words.update({"machine", "data"})
```

### Stemming and Lemmatization

```python
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download("wordnet")
words = ["connect", "connected", "connecting"]
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

print([stemmer.stem(word) for word in words])
print([lemmatizer.lemmatize(word, pos="v") for word in words])
```

### Count Vectorizer and TF-IDF

```python
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

messages = [
    "python is easy to learn",
    "python is useful for machine learning",
    "machine learning finds patterns",
]

count_features = CountVectorizer().fit_transform(messages)
tfidf_features = TfidfVectorizer().fit_transform(messages)
print(count_features.toarray())
print(tfidf_features.toarray())
```

### Sentiment Analysis with Naive Bayes

```python
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

training_text = ["excellent course", "very helpful", "poor explanation", "bad experience"]
training_labels = [1, 1, 0, 0]

sentiment_model = make_pipeline(TfidfVectorizer(), MultinomialNB())
sentiment_model.fit(training_text, training_labels)
print(sentiment_model.predict(["helpful course"]))
```

## Dimensionality Reduction

Principal Component Analysis (PCA) projects features into a smaller number of components while preserving as much variance as possible.

```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

scaled_data = StandardScaler().fit_transform(iris.data)
pca = PCA(n_components=2)
reduced_data = pca.fit_transform(scaled_data)

plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=iris.target, cmap="viridis")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("Iris Data Reduced with PCA")
plt.show()
print("Explained variance:", pca.explained_variance_ratio_)
```

## OpenCV

OpenCV supports image processing, feature detection, video capture, and computer-vision applications.

### Reading, Grayscale, and Resizing Images

```python
import cv2

image = cv2.imread("photo.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
resized_image = cv2.resize(image, (640, 480))

cv2.imshow("Gray image", gray_image)
cv2.imwrite("photo_gray.jpg", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### Haar Classifiers for Face and Eye Detection

```python
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
eye_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml"
)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

for x, y, width, height in faces:
    face_region = gray[y:y + height, x:x + width]
    eyes = eye_detector.detectMultiScale(face_region)
    cv2.rectangle(image, (x, y), (x + width, y + height), (255, 0, 0), 2)
```

### Webcam, Video Capture, and Dataset Collection

```python
camera = cv2.VideoCapture(0)
frame_number = 0

while True:
    success, frame = camera.read()
    if not success:
        break

    cv2.imshow("Camera", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("s"):
        cv2.imwrite(f"dataset/frame_{frame_number:04d}.jpg", frame)
        frame_number += 1
    if key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
```

For face classification in video, run the Haar detector inside the capture loop, draw rectangles on each frame, and write frames to a video file with `cv2.VideoWriter`.

## Project Ideas

### 1. Python and SQL Project

Build a student-management or sales-reporting application that:

- Stores records in MySQL or SQLite.
- Uses parameterized queries and CRUD operations.
- Exports summary results to CSV.
- Includes a Python menu or GUI.

### 2. Python and Machine Learning Project

Build a customer-churn, house-price, sentiment-analysis, or course-recommendation project:

- Define the target and evaluation metric.
- Build preprocessing and model pipelines.
- Compare a baseline with tuned models.
- Save the final model with `joblib`.

```python
import joblib

joblib.dump(sentiment_model, "sentiment_model.joblib")
loaded_model = joblib.load("sentiment_model.joblib")
print(loaded_model.predict(["this is a great course"]))
```

### 3. Power BI Dashboard

Prepare a clean output table from the ML or SQL project, save it as CSV, and create a Power BI dashboard with:

- KPI cards for total records and key performance measures.
- Trend charts over time.
- Category or region slicers.
- A detail table and an explanatory project summary.

## Suggested Study Flow

1. Learn the ML workflow, terminology, and preprocessing pipeline.
2. Practice classification with KNN, logistic regression, SVM, decision trees, and ensembles.
3. Practice regression with linear, polynomial, and regularized models.
4. Compare models with appropriate metrics and cross-validation.
5. Explore clustering, recommendation systems, PCA, and text features.
6. Finish with an OpenCV experiment and an end-to-end project connected to SQL or Power BI.

## Learning Outcomes

By the end of this course, you should be able to:

- Explain the difference between supervised and unsupervised learning.
- Prepare numerical, categorical, text, image, and missing data for modeling.
- Train classification, regression, clustering, recommendation, and NLP models.
- Evaluate models with metrics that match the problem.
- Tune hyperparameters with cross-validation and search techniques.
- Reduce dimensions with PCA and visualize learned patterns.
- Build introductory image and video applications with OpenCV.
- Present a complete Python and ML project through a Power BI dashboard.

## Source Material

- [`SYLLABUS.txt`](SYLLABUS.txt) - Original Machine Learning course outline.
- [`../README.md`](../README.md) - Repository overview.
