# Deep Learning & Neural Networks Roadmap

A practical guide to neural networks, TensorFlow, Keras, computer vision, natural language processing, sequence models, generative models, and speech applications.

> **Course focus:** Understand how neural networks learn, build models with TensorFlow and Keras, and apply deep learning to images, text, time series, audio, and real-world projects.

## At A Glance

| Stage | Coverage |
| --- | --- |
| Foundations | Perceptrons, multilayer networks, feedforward computation, and backpropagation |
| TensorFlow | Tensors, variables, operations, computational graphs, and automatic differentiation |
| Training | Gradient descent, optimizers, activations, regularization, and batch normalization |
| Keras | Sequential and Functional APIs, regression, classification, saving, and loading models |
| Specializations | CNNs, transfer learning, word embeddings, RNNs, LSTMs, GRUs, and seq2seq models |
| Generative and Audio AI | GANs, text-to-speech, speech-to-text, and voice automation |

## Contents

- [Setup](#setup)
- [Artificial Neural Networks](#artificial-neural-networks)
- [Deep Learning and TensorFlow](#deep-learning-and-tensorflow)
- [Optimizers and Training](#optimizers-and-training)
- [Activation Functions](#activation-functions)
- [Building an ANN](#building-an-ann)
- [Modern Optimizers and Regularization](#modern-optimizers-and-regularization)
- [Deep Networks with Keras](#deep-networks-with-keras)
- [Convolutional Neural Networks](#convolutional-neural-networks)
- [Word Embeddings](#word-embeddings)
- [RNNs, LSTMs, and GRUs](#rnns-lstms-and-grus)
- [Generative Adversarial Networks](#generative-adversarial-networks)
- [Speech Recognition APIs](#speech-recognition-apis)
- [Project Ideas](#project-ideas)

## Setup

Install TensorFlow and the supporting packages:

```bash
python -m pip install tensorflow numpy pandas matplotlib scikit-learn pillow opencv-python
```

For hardware acceleration, follow the current TensorFlow installation guidance for your operating system and GPU. Google Colab is a convenient alternative when local hardware is limited.

```python
import tensorflow as tf

print("TensorFlow:", tf.__version__)
print("Devices:", tf.config.list_physical_devices())
```

TensorFlow 2.x uses eager execution by default and provides `tf.function` when graph execution is useful. TensorFlow 1.x examples often use explicit sessions and graphs; modern projects should generally use TensorFlow 2.x and Keras.

## Artificial Neural Networks

An artificial neural network transforms inputs through weighted connections, biases, and activation functions. A perceptron is a single neuron; a multilayer perceptron (MLP) stacks hidden layers.

### Perceptron

```python
import numpy as np

inputs = np.array([1.0, 0.5])
weights = np.array([0.7, -0.2])
bias = 0.1

weighted_sum = inputs @ weights + bias
prediction = int(weighted_sum >= 0)
print(prediction)
```

### Feedforward and Backpropagation

Feedforward calculates predictions. Backpropagation applies the chain rule to calculate how each weight contributed to the loss, then an optimizer updates the weights.

```python
import tensorflow as tf

model = tf.keras.Sequential([
    tf.keras.layers.Dense(8, activation="relu", input_shape=(2,)),
    tf.keras.layers.Dense(1, activation="sigmoid"),
])

with tf.GradientTape() as tape:
    prediction = model(tf.constant([[1.0, 0.5]]))
    loss = tf.reduce_mean((prediction - 1.0) ** 2)

gradients = tape.gradient(loss, model.trainable_variables)
print("Loss:", float(loss))
print("Number of gradient tensors:", len(gradients))
```

## Deep Learning and TensorFlow

Deep learning uses neural networks with multiple learned layers to model complex patterns. Common applications include image classification, object detection, language modeling, recommendation, speech recognition, and time-series forecasting.

### Constants, Variables, Scalars, Vectors, and Matrices

```python
scalar = tf.constant(3.0)
vector = tf.constant([1.0, 2.0, 3.0])
matrix = tf.constant([[1.0, 2.0], [3.0, 4.0]])
weight = tf.Variable([[0.5, 0.2], [0.1, 0.7]])

print(tf.shape(vector))
print(tf.matmul(matrix, weight))
weight.assign_add(tf.ones_like(weight) * 0.01)
```

### TensorFlow and NumPy Operations

```python
numpy_values = np.array([1.0, 2.0, 3.0])
tensor_values = tf.constant([1.0, 2.0, 3.0])

print(numpy_values * 2)
print(tensor_values * 2)
print(tensor_values.numpy())
```

TensorFlow operations produce tensors and can be tracked by automatic differentiation. NumPy operations are excellent for general numerical work but are not automatically recorded by `GradientTape`.

### Computational Graph

Use `tf.function` to trace a Python function into a TensorFlow graph that can be optimized and reused.

```python
@tf.function
def add_and_square(first, second):
    total = first + second
    return total * total

print(add_and_square(tf.constant(2.0), tf.constant(3.0)))
```

## Optimizers and Training

An optimizer changes trainable weights in the direction that reduces loss. An epoch is one pass through the training data. Batch size controls how many samples contribute to one update.

```python
model = tf.keras.Sequential([
    tf.keras.layers.Dense(16, activation="relu", input_shape=(4,)),
    tf.keras.layers.Dense(3, activation="softmax"),
])

model.compile(
    optimizer=tf.keras.optimizers.SGD(learning_rate=0.01),
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
)
```

### Full-Batch, Mini-Batch, and Stochastic Gradient Descent

```python
model.fit(
    x_train,
    y_train,
    batch_size=len(x_train),  # Full-batch gradient descent
    epochs=10,
)

model.fit(
    x_train,
    y_train,
    batch_size=32,             # Mini-batch gradient descent
    epochs=10,
)

model.fit(
    x_train,
    y_train,
    batch_size=1,              # Stochastic gradient descent
    epochs=10,
)
```

## Activation Functions

Activation functions allow neural networks to learn nonlinear relationships.

```python
values = tf.constant([-2.0, -0.5, 0.0, 0.5, 2.0])

print("Sigmoid:", tf.keras.activations.sigmoid(values).numpy())
print("Tanh:", tf.keras.activations.tanh(values).numpy())
print("ReLU:", tf.keras.activations.relu(values).numpy())
print("Softmax:", tf.keras.activations.softmax(values).numpy())
```

- **Sigmoid:** Useful for binary probabilities, but can suffer from vanishing gradients.
- **Tanh:** Centers values around zero, but can also saturate.
- **ReLU:** Efficient and common in hidden layers, though it can produce inactive neurons.
- **Softmax:** Converts class scores into a multiclass probability distribution.

A practical model uses a numerically stable loss together with its output activation:

```python
classifier = tf.keras.Sequential([
    tf.keras.layers.Dense(32, activation="relu"),
    tf.keras.layers.Dense(3, activation="softmax"),
])
classifier.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
)
```

## Building an ANN

### MNIST Dataset

```python
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

ann = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dense(10, activation="softmax"),
])

ann.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
)
ann.fit(x_train, y_train, validation_split=0.1, epochs=5, batch_size=128)
print(ann.evaluate(x_test, y_test))
```

### Manual Training with Gradient Tape

```python
features = tf.random.normal((128, 4))
labels = tf.cast(tf.reduce_sum(features, axis=1) > 0, tf.float32)

manual_model = tf.keras.Sequential([
    tf.keras.layers.Dense(16, activation="relu"),
    tf.keras.layers.Dense(1, activation="sigmoid"),
])
optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
loss_function = tf.keras.losses.BinaryCrossentropy()

for epoch in range(5):
    with tf.GradientTape() as tape:
        predictions = manual_model(features, training=True)
        loss = loss_function(labels, predictions)
    gradients = tape.gradient(loss, manual_model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, manual_model.trainable_variables))
    print(f"Epoch {epoch + 1}: loss={loss.numpy():.4f}")
```

This demonstrates initialization of weights and biases, a loss function, gradient calculation, and weight updates.

## Modern Optimizers and Regularization

### SGD with Momentum, RMSprop, AdaGrad, and Adam

```python
optimizers = {
    "sgd_momentum": tf.keras.optimizers.SGD(learning_rate=0.01, momentum=0.9),
    "rmsprop": tf.keras.optimizers.RMSprop(learning_rate=0.001),
    "adagrad": tf.keras.optimizers.Adagrad(learning_rate=0.01),
    "adam": tf.keras.optimizers.Adam(learning_rate=0.001),
}
```

- **Momentum:** Smooths updates using previous gradients.
- **RMSprop:** Adapts the learning rate using recent squared gradients.
- **AdaGrad:** Gives frequently updated parameters smaller learning rates.
- **Adam:** Combines momentum and adaptive learning rates and is a strong default.

### Dropout and Batch Normalization

```python
regularized_model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation="softmax"),
])
```

Dropout randomly disables units during training to reduce overfitting. Batch normalization stabilizes layer inputs and can make optimization easier.

## Deep Networks with Keras

Keras is TensorFlow's high-level API for defining, compiling, training, evaluating, and exporting neural networks.

### Sequential API

```python
sequential_model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(10,)),
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dense(1),
])
sequential_model.compile(optimizer="adam", loss="mse", metrics=["mae"])
```

### Functional API

```python
inputs = tf.keras.Input(shape=(10,), name="features")
hidden = tf.keras.layers.Dense(64, activation="relu")(inputs)
hidden = tf.keras.layers.Dropout(0.2)(hidden)
outputs = tf.keras.layers.Dense(1, name="prediction")(hidden)
functional_model = tf.keras.Model(inputs, outputs)
```

### Regression and Classification

```python
regression_model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(8,)),
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dense(1),
])
regression_model.compile(optimizer="adam", loss="mse", metrics=["mae"])

classification_model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(8,)),
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dense(3, activation="softmax"),
])
classification_model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
)
```

### Save and Load a Model

```python
regression_model.save("regression_model.keras")
restored_model = tf.keras.models.load_model("regression_model.keras")
print(restored_model.summary())
```

Use callbacks such as `EarlyStopping` and `ModelCheckpoint` during training:

```python
callbacks = [
    tf.keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True),
    tf.keras.callbacks.ModelCheckpoint("best_model.keras", save_best_only=True),
]
```

## Convolutional Neural Networks

CNNs learn local spatial patterns using convolutional filters. Padding controls border handling, stride controls movement size, and pooling reduces spatial dimensions.

### CNN Architecture

```python
cnn = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(28, 28, 1)),
    tf.keras.layers.Conv2D(32, kernel_size=3, padding="same", activation="relu"),
    tf.keras.layers.MaxPooling2D(pool_size=2, strides=2),
    tf.keras.layers.Conv2D(64, kernel_size=3, padding="same", activation="relu"),
    tf.keras.layers.MaxPooling2D(pool_size=2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(10, activation="softmax"),
])
cnn.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
```

### Data Augmentation

```python
augmentation = tf.keras.Sequential([
    tf.keras.layers.RandomFlip("horizontal"),
    tf.keras.layers.RandomRotation(0.1),
    tf.keras.layers.RandomZoom(0.1),
])

augmented_image = augmentation(tf.expand_dims(x_train[0], axis=0), training=True)
```

### Training and Evaluation

```python
history = cnn.fit(
    x_train[..., np.newaxis],
    y_train,
    validation_split=0.1,
    epochs=10,
    batch_size=128,
    callbacks=callbacks,
)
cnn.evaluate(x_test[..., np.newaxis], y_test)
```

### Autoencoder

An autoencoder learns to reconstruct its input through a smaller latent representation.

```python
encoder = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(28, 28, 1)),
    tf.keras.layers.Conv2D(16, 3, activation="relu", strides=2, padding="same"),
    tf.keras.layers.Conv2D(8, 3, activation="relu", strides=2, padding="same"),
])

decoder = tf.keras.Sequential([
    tf.keras.layers.Conv2DTranspose(8, 3, activation="relu", strides=2, padding="same"),
    tf.keras.layers.Conv2DTranspose(16, 3, activation="relu", strides=2, padding="same"),
    tf.keras.layers.Conv2D(1, 3, activation="sigmoid", padding="same"),
])

autoencoder = tf.keras.Sequential([encoder, decoder])
autoencoder.compile(optimizer="adam", loss="mse")
```

### Transfer Learning

Use a pretrained CNN as a feature extractor, then fine-tune selected layers for a new task.

```python
base_model = tf.keras.applications.ResNet50(
    weights="imagenet",
    include_top=False,
    input_shape=(224, 224, 3),
)
base_model.trainable = False

transfer_model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(224, 224, 3)),
    tf.keras.applications.resnet50.preprocess_input,
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(2, activation="softmax"),
])
transfer_model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"],
)
```

LeNet, AlexNet, VGG16, and ResNet50 are important CNN architectures. YOLO is a family of one-stage object-detection models that predicts classes and bounding boxes in one pass.

## Word Embeddings

Word embeddings represent words as dense vectors so semantic relationships can be learned from their positions in vector space. Word2Vec includes CBOW and Skip-gram approaches; GloVe learns vectors from global word co-occurrence statistics.

### Keras Embedding Layer

```python
embedding_model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(100,)),
    tf.keras.layers.Embedding(input_dim=10_000, output_dim=128),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(1, activation="sigmoid"),
])
embedding_model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
```

### CBOW and Skip-Gram Data

```python
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import timeseries_dataset_from_array

sentences = ["deep learning learns patterns", "neural networks learn features"]
tokenizer = Tokenizer()
tokenizer.fit_on_texts(sentences)
encoded = tokenizer.texts_to_sequences(sentences)
print(tokenizer.word_index)
print(encoded)
```

For a complete Word2Vec implementation, create `(context, target)` pairs for CBOW or `(target, context)` pairs for Skip-gram, then train a shallow neural network to predict one from the other.

### Visualizing Embeddings

```python
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

vectors = np.random.default_rng(42).normal(size=(6, 50))
words = ["deep", "learning", "neural", "network", "image", "text"]
points = PCA(n_components=2).fit_transform(vectors)

plt.scatter(points[:, 0], points[:, 1])
for index, word in enumerate(words):
    plt.annotate(word, points[index])
plt.title("2D Word Embedding View")
plt.show()
```

Pretrained Google Word2Vec and GloVe embeddings can be loaded when their files are downloaded and their dimensions match the model's embedding layer.

## RNNs, LSTMs, and GRUs

Recurrent neural networks process sequences while carrying information from earlier time steps. LSTM and GRU gates help preserve useful long-term information and reduce vanishing-gradient problems.

### Basic RNN, LSTM, and GRU

```python
sequence_model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(50, 8)),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64, return_sequences=True)),
    tf.keras.layers.GRU(32),
    tf.keras.layers.Dense(1, activation="sigmoid"),
])
sequence_model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
```

### Text Classification with LSTM

```python
vocabulary_size = 10_000
text_classifier = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(200,)),
    tf.keras.layers.Embedding(vocabulary_size, 128),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64)),
    tf.keras.layers.Dense(1, activation="sigmoid"),
])
text_classifier.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
```

### Time-Series Prediction

```python
series = np.sin(np.arange(0, 100, 0.1)).astype("float32")
window_size = 20
windows = np.array([
    series[index:index + window_size]
    for index in range(len(series) - window_size)
])
X_sequence = windows[:, :-1, np.newaxis]
y_sequence = windows[:, -1]

forecast_model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(window_size - 1, 1)),
    tf.keras.layers.LSTM(32),
    tf.keras.layers.Dense(1),
])
forecast_model.compile(optimizer="adam", loss="mse")
forecast_model.fit(X_sequence, y_sequence, epochs=5, verbose=0)
```

### Encoder-Decoder and Seq2Seq

```python
encoder_inputs = tf.keras.Input(shape=(None, 32))
encoder_outputs, state_h, state_c = tf.keras.layers.LSTM(64, return_state=True)(encoder_inputs)
encoder_states = [state_h, state_c]

decoder_inputs = tf.keras.Input(shape=(None, 32))
decoder_outputs = tf.keras.layers.LSTM(64, return_sequences=True)(
    decoder_inputs,
    initial_state=encoder_states,
)
decoder_outputs = tf.keras.layers.Dense(32, activation="softmax")(decoder_outputs)
seq2seq_model = tf.keras.Model([encoder_inputs, decoder_inputs], decoder_outputs)
```

## Generative Adversarial Networks

A GAN trains two networks together:

- The **generator** creates synthetic samples from random noise.
- The **discriminator** predicts whether a sample is real or generated.

```python
generator = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(100,)),
    tf.keras.layers.Dense(7 * 7 * 128, activation="relu"),
    tf.keras.layers.Reshape((7, 7, 128)),
    tf.keras.layers.Conv2DTranspose(64, 4, strides=2, padding="same", activation="relu"),
    tf.keras.layers.Conv2DTranspose(1, 4, strides=2, padding="same", activation="tanh"),
])

discriminator = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(28, 28, 1)),
    tf.keras.layers.Conv2D(64, 4, strides=2, padding="same"),
    tf.keras.layers.LeakyReLU(0.2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(1),
])
```

A complete GAN training loop alternates discriminator updates on real and generated images with generator updates that try to fool the discriminator. Common GAN families include DCGAN, conditional GAN, and Wasserstein GAN.

## Speech Recognition APIs

Speech applications commonly use speech-to-text, text-to-speech, and a command router.

Install a simple cross-platform package:

```bash
python -m pip install SpeechRecognition pyttsx3 pyaudio
```

### Text to Speech

```python
import pyttsx3

speaker = pyttsx3.init()
speaker.say("Deep learning experiment started")
speaker.runAndWait()
```

### Speech to Text

```python
import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.Microphone() as microphone:
    print("Say something...")
    audio = recognizer.listen(microphone, timeout=5)

try:
    text = recognizer.recognize_google(audio)
    print("You said:", text)
except (sr.UnknownValueError, sr.RequestError) as error:
    print("Speech recognition failed:", error)
```

### Voice Automation and Web Search

```python
import webbrowser

command = text.lower()
if command.startswith("search "):
    query = command.removeprefix("search ").strip()
    webbrowser.open("https://www.google.com/search?q=" + query.replace(" ", "+"))
```

Only automate actions the user explicitly requested, and avoid sending sensitive spoken information to external services without consent.

## Project Ideas

Choose any four projects from the syllabus:

- Stock price prediction using LSTM
- Object detection with a pretrained CNN or YOLO
- Face-recognition attendance system
- Facial-expression and age prediction
- Neural machine translation with an encoder-decoder
- Handwritten digit and letter prediction
- Number-plate recognition with OpenCV
- Gender classification, with careful attention to dataset limitations and fairness
- Desktop assistant using speech recognition and text-to-speech
- Cat-versus-dog image classification with transfer learning

A strong project should include a clear problem definition, dataset description, preprocessing, baseline, model architecture, evaluation metrics, error analysis, and a reproducible README.

## Suggested Study Flow

1. Learn perceptrons, feedforward networks, backpropagation, and the role of activations.
2. Practice TensorFlow tensors, variables, gradient tapes, losses, and optimizer updates.
3. Build an ANN on MNIST with Keras and compare training and validation performance.
4. Add regularization, callbacks, and modern optimizers to control overfitting.
5. Build CNNs for image classification and experiment with augmentation and transfer learning.
6. Explore embeddings and sequence models for text and time-series problems.
7. Study GANs, speech APIs, and OpenCV through small focused experiments.
8. Complete four projects and document the full model-development lifecycle.

## Learning Outcomes

By the end of this course, you should be able to:

- Explain neurons, perceptrons, multilayer networks, forward passes, and backpropagation.
- Use TensorFlow and Keras to define, train, evaluate, save, and load models.
- Select activation functions, optimizers, losses, and regularization methods appropriately.
- Build ANN and CNN models for structured and image data.
- Apply transfer learning, embeddings, RNNs, LSTMs, and GRUs to practical tasks.
- Understand the generator and discriminator roles in GANs.
- Build introductory speech, video, face, and object-detection applications.
- Deliver reproducible deep-learning projects with documented evaluation and limitations.

## Source Material

- [`SYLLABUS.txt`](SYLLABUS.txt) - Original Deep Learning & Neural Networks course outline.
- [`../README.md`](../README.md) - Repository overview.
