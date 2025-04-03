# DeepLearningBook
**Deep Learning with Python** is a great book, written by F. Chollet the co-founder of Keras. It starts with theory and explanations and it will show code and practice in order to build your own Deep Learning model.

![alt text](book.jpg "Deep Learning con Python")


### Table of Contents
- [Chapter 1. What is Deep Learning](#chapter-1-what-is-deep-learning)
- [Chapter 2. Before we Start: Basic Math for Neural Networks](#chapter-2-before-we-start-basic-math-for-neural-networks)
- [Chapter 3. Introduction to Neural Networks](#chapter-3-introduction-to-neural-networks)
- [Chapter 4. Machine Learning Fondamentals](#chapter-4-machine-learning-fondamentals)
- [Chapter 5. Deep Learning for computer vision](#chapter-5-deep-learning-for-computer-vision)


## Step-By-Step Learning

### Chapter 1. What is Deep Learning
In this chapter we will study the theory behind Deep Learning. What is it, when it was born, and the main techniques used.

This is a simple schema on how the deep learning mechanism works:

![alt text](dlprocess.jpg "Deep Learning Process")


### Chapter 2. Before we Start: Basic Math for Neural Networks
In this chapter we will study some basic math to better understand Neural Networks.
The book tries to explain the concepts using Python Numpy instead of pure Math.

<br>
The chapter starts with a very simple Neural Network code to begin with:

[Files/mnist.py](files/mnist.py)

Then the book explains the different tensor's types using Numpy:

Each code will start with: 
```bash
import numpy as np
```
And ends with this command to check the Dimension of the Numpy Array: 
```bash
print(x.dim)
```

<li>Scalars (tensors 0D):</li>

```bash
x = np.array(12)
```
(DIM = 0)

<li>Vectors (tensors 1D):</li>

```bash
x = np.array([12,3,6,14])
```
(DIM = 1)

<li>Matrix (tensors 2D):</li>

```bash
x = np.array([5,78,2,34,0],
            [6,79,3,35,1],
            [7,80,4,36,2])
```
(DIM = 2)

<li>Tensors 3D or more:</li>

```bash
x = np.array([[[5,78,2,34,0],
            [6,79,3,35,1],
            [7,80,4,36,2]],
            [[5,78,2,34,0],
            [6,79,3,35,1],
            [7,80,4,36,2]]])
```
(DIM = 3)


#### - Tensors are defined by 3 main attributes:
<li>Numer of Axis (rank)</li>
<li>Shape</li>
<li>Type of data (dtype)</li>

<br>
The book continues with other examples and methods to work with Tensors and more advanced Math concepts.


<br>

### Chapter 3. Introduction to Neural Networks

This chapter starts to explain how to use Keras, how to setup an environment and there are a few examples of different Deep Learning codes for classification and regression.

Files created:

- [Files/imdb.py](files/imdb.py) = Predict Internet Movie Recensions (Classification)
- [Files/reuters.py](files/reuters.py) = Predict '86 Agency Work-Sectors (Classification)
- [Files/bostonhousing.py](files/bostonhousing.py) - Predict Boston '70 House Prices (Regression)

<br>
Now we have seen some Deep Learning models for classification and regression using Keras!


<br>

### Chapter 4. Machine Learning Fondamentals

In this chapter we learned the 4 different types of Machine Learning:
<li>Supervised Learning</li>
<li>Unsupervised Learning</li>
<li>Auto-Supervised Learning</li>
<li>Reinforced Learning</li>

<br>

We have seen some protocols for model evaluation:
<li>Hold-Out</li>
<li>K-fold</li>
<li>K-fold with shuffling</li>

<br>

Then we have seen some data pre-elaboration:
<li>Vectorization</li>
<li>Values Normalization</li>
<li>Missing data handling</li>

<br>

The book explained some methods to avoid Overfitting or Underfitting:
<li>Reduce network dimension</li>
<li>Weights Regularization</li>
<li>Use Dropout</li>

<br>

Finally, we learned a common path to follow when dealing with Machine Learning:
<li>Define problem and create/find dataset</li>
<li>Select the evaluation param (example: accuracy or roc auc curve..)</li>
<li>Find an evaluation protocol</li>
<li>Prepare data</li>
<li>Create a model that performs better than a random one</li>
<li>Create a model that does Overfit</li>
<li>Regularize the model and optimize hyperparams</li>
<li>Test your model</li>


<br>

### Chapter 5. Deep Learning for computer vision

This chapter starts introducing ConvNet, an useful neural network for computer vision.
<br>
We can see some examples on how to use convnet for the mnist image dataset, explaining how to Convolution works.
<br>
We learn about Max-Pooling and how it's used with convnet.
<br>
We can create a code using Kaggle "dogs vs cats" dataset, in order to create a convnet to predict images of dogs and cats.

**Standard approach**
<li>Download dataset</li>
<li>Create folders for train, test and validation sets</li>
<li>Create neural network using Conv2d and MaxPooling</li>
<li>Add a Flatten and some Dense layers</li>
<li>Pre-elaborate data (the images) using ImageDataGenerator from Keras</li>

```bash
from keras.preprocessing.image import ImageDataGenerator
```

This class is useful for elaborate images and you can use it for data-augmentation as well!

<li>Save the model and plot the results</li>
We got around 70% precision on our validation sets!

<br>

**Data Augmentation**
<li>Add some data-augmentation using ImageDataGenerator</li>
<li>Create a new neural network using these augmented data</li>
<li>Save model and show results</li>
This time we haven't received any Overfitting and the model reached a 82% precision!

<br>

**Use a pre-trained convnet without data-augmentation**
<li>Use the VGG16 pre-trained model from Keras</li>

```bash
from keras.applications import VGG16
```

<li>Define our neural network that will receive the VGG16 pre-trained model</li>
<li>Freeze the VGG16 layers so that the pre-trained model won't update its weights and just use them for our new model</li>
<li>Plot results</li>
Now the Overfitting is back but we've got around 90% precision!

<br>

**Use a pre-trained convnet with data-augmentation**
<li>Use VGG16 with our augmented-data</li>
<li>Plot results</li>
Now the Overfit is much lower and the accuracy went to 96%!

<br>

**Fine Tuning**

Those are the steps required for Fine-Tune a pre-trained neural network:
<li>Add your personalized network above a pre-trained network</li>
<li>Freeze the layers of the base network (the pre-trained one)</li>
<li>Train the new network</li>
<li>Unfreeze the last layers of the pre-trained network</li>
<li>Train the whole network (both the unfreezed layers and your new network)</li>

We proceeded on Fine-Tuning a pre-trained network
<li>Unfreeze last layers</li>
<li>Retrain the network and show results</li>
Now our accuracy increased to 97%!

<br>

**Visualize middle activations**
The book shows how to visualize the middle activations of a convnet, showing the images (or the part of the images) that the net is processing, step-by-step. 
<br>
Then it shows how to see filters of a convnet and show the parts of the image that best activates the layers.

<br>
For a general guide you can see this code:

- [Files/convnet.py](files/convnet.py) = Some code explained in Chapter 5, using convnet