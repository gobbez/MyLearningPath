from keras.datasets import boston_housing
from keras import models, layers
import numpy as np
import matplotlib.pyplot as plt

(train_data, train_targets), (test_data, test_targets) = boston_housing.load_data()

# Prepare data
mean, std = train_data.mean(axis=0), train_data.std(axis=0)
train_data = (train_data - mean) / std
test_data = (test_data - mean) / std
input_shape = (train_data.shape[1],)

# Create Neural Network
def build_model():
    model = models.Sequential([
        layers.Dense(64, activation='relu', input_shape=input_shape),
        layers.Dense(64, activation='relu'),
        layers.Dense(1)
    ])
    model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
    return model

# K-fold validation
k, num_epochs = 4, 50
num_val_samples = len(train_data) // k
all_mae_histories = []

for i in range(k):
    print(f'Processing fold #: {i}')
    val_data, val_targets = train_data[i * num_val_samples:(i + 1) * num_val_samples], train_targets[i * num_val_samples:(i + 1) * num_val_samples]
    partial_train_data = np.vstack((train_data[:i * num_val_samples], train_data[(i + 1) * num_val_samples:]))
    partial_train_targets = np.hstack((train_targets[:i * num_val_samples], train_targets[(i + 1) * num_val_samples:]))

    model = build_model()
    history = model.fit(partial_train_data, partial_train_targets, validation_data=(val_data, val_targets), epochs=num_epochs, batch_size=1, verbose=0)
    all_mae_histories.append(history.history['val_mae'])

average_mae_history = np.mean(all_mae_histories, axis=0)

# Create plots without first 10 points
def smooth_curve(points, factor=0.9):
    smoothed = [points[0]]
    for point in points[1:]:
        smoothed.append(smoothed[-1] * factor + point * (1 - factor))
    return smoothed

smooth_mae_history = smooth_curve(average_mae_history[10:])
plt.plot(range(1, len(smooth_mae_history) + 1), smooth_mae_history)
plt.xlabel('Epochs')
plt.ylabel('Validation MAE')
plt.show()