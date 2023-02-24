# Create y_pred by predicting the target values of the unseen features X_new.
# Print the predicted labels for the set of predictions.



# Predict the labels for the X_new
y_pred =knn.predict(X_new)

# Print the predictions for X_new
print("Predictions: {}".format(y_pred))