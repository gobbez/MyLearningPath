# DeepLearningBook
**Deep Learning with Python** is a great book, written by F. Chollet the co-founder of Keras. It starts with theory and explanations and it will show code and practice in order to build your own Deep Learning model.

![alt text](book.jpg "Deep Learning con Python")


### Table of Contents
- [Chapter 1. What is Deep Learning](#chapter-1-what-is-deep-learning)
- [Chapter 2. Before we Start: Basic Math for Neural Networks](#chapter-2-before-we-start-basic-math-for-neural-networks)
- [Chapter 3. Introduction to Neural Networks](#chapter-3-introduction-to-neural-networks)


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