import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load the dataset of transaction history
df = pd.read_csv('transaction_data.csv')

# Split the data into training and testing sets
train_data, test_data, train_labels, test_labels = train_test_split(df.drop(['Transaction ID', 'Label'], axis=1), df['Label'], test_size=0.2)

# Train a logistic regression model on the training data
model = LogisticRegression()
model.fit(train_data, train_labels)

# Use the model to predict the labels of the test data
predictions = model.predict(test_data)

# Print the accuracy of the model
accuracy = (predictions == test_labels).mean()
print(f'Accuracy: {accuracy}')

# Use the model to predict the label of a new transaction
new_transaction = [...insert values for new transaction features here...]
predicted_label = model.predict([new_transaction])
print(f'Predicted label for new transaction: {predicted_label}')
