# MIT 6.S191 - INTRODUCTION TO DEEP LEARNING

First video of the Season 6.S191. Alexander Amini explains the basics of Deep Learning and its applications.

## Introduction

The field of deep learning has made significant progress in recent years, with notable advancements in image and video generation, and the course will cover the fundamental techniques that drive this progress.
<br>
The course will introduce students to the concept of intelligence, artificial intelligence, machine learning, and deep learning, and will teach students how to teach computers to learn and perform tasks.
<br>
It will provide a solid foundation in deep learning through lectures and software labs, allowing students to get hands-on experience with deep learning techniques 
<br>
Key points in modern deep learning, including guest lectures from industry leaders on state-of-the-art methods, and will introduce TensorFlow and PyTorch software labs 
<br>
Students will work on labs, including building a language model, a facial detection system, and fine-tuning a large language model, with opportunities to win prizes and participate in a final project pitch competition 


<br>

## Fundamentals of Deep Learning and Neural Networks
**Scalars** can be represented as a single equation using linear algebra in terms of vectors and dot products, where the output Y is obtained by taking the dot product between X and W, adding the bias, and passing through a nonlinearity.
<br>

**Sigmoid function** is a common example of a nonlinearity, which outputs values between 0 and 1, making it suitable for probabilities, and there are many types of nonlinear functions used in neural networks 
<br>

**Activation function** purpose is to introduce nonlinearities into the model, allowing it to approximate complex functions, and without a nonlinear activation function, the model would be linear 
<br>
Common activation functions are:
<li>Sigmoid: Outputs values between 0 and 1.​</li>
<li>Tanh: Outputs values between -1 and 1.​</li>
<li>ReLU (Rectified Linear Unit): Outputs zero for negative inputs and the input itself for positive inputs.​</li>

<br>
A single neuron with two inputs can be represented graphically, and the output can be obtained by computing the dot product, adding the bias, and passing it through a nonlinearity, such as the sigmoid function 
<br>
A multi-output neural network can be created by adding neurons, where each neuron has the same inputs but different weights, resulting in different outputs, and these types of layers are typically called dense layers 
<br>
A neural network with a single hidden layer is formed by placing the hidden layer between the input and output layers, and it requires two weight matrices, W1 and W2, to transform the inputs to the hidden layer and the hidden layer to the outputs 
<br>
To create a deep neural network, multiple linear layers followed by nonlinearities are stacked sequentially in a hierarchical fashion, allowing the model to learn more complex representations of the data 
<br>
The number of layers and outputs in a neural network can be adjusted based on the problem definition, with more complex tasks requiring deeper networks and more outputs, such as generating an image versus predicting a single temperature value 


<br>

## Training Deep Neural Networks
The goal is to find and build models that minimize the loss on a dataset, which measures the difference between predicted and true values, by optimizing the weights in the model 
<br>
The process of optimizing the weights involves computing the gradient of the loss function with respect to the weights, and then taking a small step in the opposite direction of the gradient, which is known as gradient descent

<br>

**Gradient descent** is computed using back propagation, which is an application of the chain rule from differential calculus, and is used to update the weights in the model 
<br>

**Learning rate** of the model dictates how quickly the weights are updated, and setting the learning rate can be challenging, with options including trying different learning rates, or using adaptive algorithms that adjust the learning rate based on the gradients and data 
<br>
There are different types of learning rate schedulers, and trying them out can be as simple as changing a single line of code in the learning loop 
<br>

**Stochastic gradient descent** is a type of gradient descent algorithm that computes the gradient over one data point, which is noisy but faster than computing the gradient over the entire data set 
<br>

**Mini-batched gradient descent** is a middle ground between stochastic gradient descent and full gradient descent, where the gradient is computed over a small batch of data points, allowing for more stability and speed 


<br>

## Addressing Overfitting in Deep Learning
Overfitting occurs when a model memorizes the training data and fails to generalize to new, unseen data, and regularization techniques such as Dropout can be used to discourage complex memorization 
<br>

**Dropout** is used in deep neural networks to prevent overfitting by randomly setting some activations of hidden neurons to zero with a certain probability 
<br>

**Early stopping** is a technique used to prevent overfitting of a model by monitoring the deviation between the training loss and the test loss, and stopping the training when the test loss starts to increase 
<br>
The training data can be split into a ratio, such as 70% for training and 30% for testing and validation, to evaluate the model's performance and prevent overfitting.

<br>

## Conclusions
This ends the first lesson, with more insights on Deep Learning and basic Neural Networks!


