import numpy as np
import matplotlib.pyplot as plt


class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, epochs=100):
        self.weights = np.zeros(input_size + 1)
        print(self.weights)
        self.learning_rate = learning_rate
        self.epochs = epochs

    def predict(self, inputs):
        # Dodajemy bias (1) do wejścia
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        if summation > 0:
            activation = 1
        else:
            activation = 0
        return activation

    def train(self, training_data, labels):
        for _ in range(self.epochs):
            for inputs, label in zip(training_data, labels):
                prediction = self.predict(inputs)
                # Aktualizujemy wagi w perceptronie w razie błędu
                self.weights[1:] += self.learning_rate * \
                    (label - prediction) * inputs
                self.weights[0] += self.learning_rate * (label - prediction)


# Prosty zbiór treningowy
# training_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# labels = np.array([0, 0, 0, 1])
training_data = np.array([[2, 0], [5, 0], [3, 2], [7, 1], [1, 3], [4, 3], [2, 5], [0, 7],
                          [9, 0], [8, 2], [7, 3], [9, 3], [7, 5], [3, 7], [8, 6], [6, 9], [0, 9]])
labels = np.array([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1])
# Inicjalizacja perceptronu
perceptron = Perceptron(input_size=2)


# Trening perceptronu na zbiorze treningowym
perceptron.train(training_data, labels)
print(perceptron.weights)

# Testowanie perceptronu
test_data = np.array([[7, 0], [5, 2], [3, 4], [0, 5],
                      [8, 4], [6, 4], [5, 7], [4, 8], [4, 5]])
predictions = []

for data_point in test_data:
    prediction = perceptron.predict(data_point)
    predictions.append(prediction)

# Konwertowanie wyników klasyfikacji na kolory
colors = ['r' if p == 0 else 'b' for p in predictions]

# Wykres punktowy
plt.scatter(test_data[:, 0], test_data[:, 1], c=colors)
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Klasyfikacja za pomocą Perceptronu')
plt.show()
