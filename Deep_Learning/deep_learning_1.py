import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt


(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()


x_train = x_train / 255.0
x_test = x_test / 255.0


model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),  
    keras.layers.Dense(128, activation='relu'), 
    keras.layers.Dense(10, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)


model.fit(x_train, y_train, epochs=5)


test_loss, test_acc = model.evaluate(x_test, y_test)

print("\nAccuracy:", test_acc)


prediction = model.predict(x_test)


plt.imshow(x_test[0], cmap='gray')
plt.title(f"Prediction: {prediction[0].argmax()}")
plt.show()