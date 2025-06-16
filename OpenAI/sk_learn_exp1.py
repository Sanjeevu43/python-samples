
# 1. Import necessary libraries
from sklearn.datasets import load_iris          # To load the Iris dataset
from sklearn.model_selection import train_test_split # To split data
from sklearn.neighbors import KNeighborsClassifier   # The classifier model
from sklearn.metrics import accuracy_score         # To evaluate the model

# 2. Load the dataset
# The Iris dataset contains measurements of 3 different species of Iris flowers.
# 'data' holds the features (sepal length, sepal width, petal length, petal width)
# 'target' holds the labels (0, 1, or 2, corresponding to the species)
iris = load_iris()
X = iris.data    # Feature matrix
y = iris.target  # Target vector (labels)

# Optional: Print to see the data shape and target names
print(f"Features shape: {X.shape}") # (150 samples, 4 features)
print(f"Target shape: {y.shape}")   # (150 labels)
print(f"Class names: {iris.target_names}") # ['setosa', 'versicolor', 'virginica']cd\


print("-" * 20)

# 3. Split data into training and testing sets
# We train the model on the training set and evaluate it on the unseen testing set.
# test_size=0.3 means 30% of the data will be used for testing, 70% for training.
# random_state ensures the split is the same every time we run the code (for reproducibility).
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print(f"Training samples: {X_train.shape[0]}")
print(f"Testing samples: {X_test.shape[0]}")
print("-" * 20)

# 4. Create and Train the Classifier
# We'll use K-Nearest Neighbors (KNN) with k=3 neighbors.
# This means a sample will be classified based on the majority class among its 3 nearest neighbors in the training data.
knn_model = KNeighborsClassifier(n_neighbors=3)

# Train the model using the training data (features X_train and labels y_train)
knn_model.fit(X_train, y_train)
print("KNN Model training complete.")
print("-" * 20)

# 5. Make Predictions
# Use the trained model to predict the species for the test features (X_test)
y_pred = knn_model.predict(X_test)

# Optional: Compare predictions to actual labels for the first few test samples
# print(f"Predicted labels: {y_pred[:10]}")
# print(f"Actual labels:    {y_test[:10]}")
# print("-" * 20)

# 6. Evaluate the Model
# Calculate the accuracy by comparing the predicted labels (y_pred) with the true labels (y_test).
accuracy = accuracy_score(y_test, y_pred)

print(f"Model: K-Nearest Neighbors (k=3)")
print(f"Test Set Accuracy: {accuracy:.4f}") # Format accuracy to 4 decimal places

# Example: Predict a single new flower measurement
# Let's create a hypothetical flower measurement
new_flower = [[5.0, 3.1, 1.5, 0.4]] # Sepal L, Sepal W, Petal L, Petal W
predicted_species_index = knn_model.predict(new_flower)
predicted_species_name = iris.target_names[predicted_species_index[0]]
print(f"\nPrediction for new flower {new_flower}: {predicted_species_name} (Class {predicted_species_index[0]})")