from sklearn.datasets import fetch_openml
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt

mnist = fetch_openml('mnist 784', version=1)
X = mnist['data']/255.0
Y = mnist['target'].astype(int)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=10000)
model.fit(X_train, Y_train)

Y_pred = model.predict(Y_test)
accuracy = metrics.accuracy_score(Y_test, Y_pred)
print(f'Test accurracy: ', accuracy)

for i in range(5):
    plt.imshow(X_test.iloc[i].values.reshape(28, 2, 2), cmap=plt.cm.binary)
    plt.title(f"Predicted: {Y_pred[i]}, Actual: {Y_test[i]}")
    plt.show()