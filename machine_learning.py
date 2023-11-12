import matplotlib.pyplot as plt
import numpy as np

# Tworzenie danych treningowych
x = np.linspace(0, 2 * np.pi, 1000)  # Przykładowe dane wejściowe
y = np.cos(x)  # Oczekiwane dane wyjściowe

# Inicjalizacja wag i biasów
input_size = 1
hidden_size = 64
output_size = 1

weights_input_hidden = np.random.randn(input_size, hidden_size)
bias_hidden = np.zeros((1, hidden_size))
weights_hidden_output = np.random.randn(hidden_size, output_size)
bias_output = np.zeros((1, output_size))

# Definicja funkcji aktywacji (ReLU)


def relu(x):
    return np.maximum(0, x)

# Definicja funkcji straty (Mean Squared Error)


def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred)**2)


# Uczenie modelu
learning_rate = 0.01
epochs = 200

for epoch in range(epochs):
    # Przebieg przez dane treningowe
    for i in range(len(x)):
        # Przejście w przód
        hidden_input = np.dot(x[i], weights_input_hidden) + bias_hidden
        hidden_output = relu(hidden_input)
        final_input = np.dot(
            hidden_output, weights_hidden_output) + bias_output
        final_output = final_input

        # Obliczanie straty
        loss = mean_squared_error(y[i], final_output)

        # Propagacja wsteczna
        dloss_doutput = -2 * (y[i] - final_output)
        doutput_dfinal_input = 1
        dfinal_input_dweights_hidden_output = hidden_output
        dfinal_input_dbias_output = 1

        dloss_dweights_hidden_output = np.dot(
            dfinal_input_dweights_hidden_output.T, dloss_doutput)
        dloss_dbias_output = dloss_doutput.sum()

        dloss_dhidden_output = np.dot(dloss_doutput,
                                      weights_hidden_output.T)
        dhidden_output_dhidden_input = (hidden_input > 0).astype(float)
        dhidden_input_dweights_input_hidden = x[i]
        dhidden_input_dbias_hidden = 1

        dloss_dweights_input_hidden = np.dot(
            dhidden_input_dweights_input_hidden.T, dloss_dhidden_output * dhidden_output_dhidden_input)
        dloss_dbias_hidden = (dloss_dhidden_output *
                              dhidden_output_dhidden_input).sum()

        # Aktualizacja wag i biasów
        weights_input_hidden -= learning_rate * dloss_dweights_input_hidden
        bias_hidden -= learning_rate * dloss_dbias_hidden
        weights_hidden_output -= learning_rate * dloss_dweights_hidden_output
        bias_output -= learning_rate * dloss_dbias_output

    # Obliczanie straty dla epoki
    total_loss = 0
    for i in range(len(x)):
        hidden_input = np.dot(x[i], weights_input_hidden) + bias_hidden
        hidden_output = relu(hidden_input)
        final_input = np.dot(
            hidden_output, weights_hidden_output) + bias_output
        final_output = final_input
        total_loss += mean_squared_error(y[i], final_output)
    total_loss /= len(x)

    print(f'Epoka {epoch + 1}/{epochs}, Strata: {total_loss}')

# Przewidywanie wartości na nowych danych
x_new = np.linspace(0, 2 * np.pi, 100)
predictions = []

for i in range(len(x_new)):
    hidden_input = np.dot(x_new[i], weights_input_hidden) + bias_hidden
    hidden_output = relu(hidden_input)
    final_input = np.dot(hidden_output, weights_hidden_output) + bias_output
    final_output = final_input
    predictions.append(final_output[0])

# Wykres aproksymacji funkcji sinus
plt.plot(x, y, label='Rzeczywiste dane')
plt.plot(x_new, predictions, label='Aproksymacja')
plt.legend()
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.show()
