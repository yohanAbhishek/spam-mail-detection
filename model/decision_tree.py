"""
◉ This is a class to run KNN on the spambase dataset.
Additional:
    ◦ In terms of finding the best hyper parameters to use in this model I have implemented a grid search.
"""

from sklearn.tree import DecisionTreeClassifier
import preprocess as p
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


def run_grid():
    # Create the decision tree classifier
    classifier = DecisionTreeClassifier()

    # Define the hyperparameters to tune
    parameters = {
        'max_depth': [2, 5, 10],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 5]
    }

    # Perform a grid search to find the best hyperparameters
    grid_search = GridSearchCV(classifier, parameters, cv=5)
    grid_search.fit(p.get_X_train(), p.get_y_train())

    # Print the best hyperparameters
    print("Best hyper parameters:", grid_search.best_params_)
    return grid_search.best_params_


# Run grid search and get the best parameters
search = run_grid()

# Train the model with the best hyperparameters
clf = DecisionTreeClassifier(**search)
clf.fit(p.get_X_train(), p.get_y_train())

# Make predictions on the testing set
y_pred = clf.predict(p.get_X_test())

# Calculate the accuracy score, confusion matrix, and classification report
accuracy = accuracy_score(p.get_y_test(), y_pred)
matrix = confusion_matrix(p.get_y_test(), y_pred)
report = classification_report(p.get_y_test(), y_pred)

print(f"Accuracy: {accuracy}")
print(f"Confusion Matrix:\n{matrix}")
print(f"Classification Report:\n{report}")
