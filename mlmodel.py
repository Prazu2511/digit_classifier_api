import pickle
from sklearn.datasets import fetch_openml
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load MNIST dataset
X, y = fetch_openml(name='mnist_784', version=1, return_X_y=True)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Random Forest Classifier
clf = RandomForestClassifier(n_jobs=-1, random_state=42)
clf.fit(X_train, y_train)

# Evaluate the model on the test set
print("Model Accuracy:", clf.score(X_test, y_test))

# Save the trained model to a file
with open('mnist_model.pkl', 'wb') as f:
    pickle.dump(clf, f)
