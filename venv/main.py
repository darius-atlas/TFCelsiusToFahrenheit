from __future__ import absolute_import, division, print_function, unicode_literals
import matplotlib.pyplot as plt
import tensorflow as tf
tf.logging.set_verbosity(tf.logging.ERROR)

import numpy as np

celsius_q    = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit_a = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

for i,c in enumerate(celsius_q):
  print("{} градусов Цельсия = {} градусов Фаренгейта".format(c, fahrenheit_a[i]))



l0 = tf.keras.layers.Dense(units=1, input_shape=[1])



model = tf.keras.Sequential([l0])


model.compile(loss='mean_squared_error',
              optimizer=tf.keras.optimizers.Adam(0.1))


history = model.fit(celsius_q, fahrenheit_a, epochs=500, verbose=False)
print("Завершили тренировку модели")

plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.plot(history.history['loss'])