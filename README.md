# nn-depth-study
Studying the effect of neural network depth using NumPy
# Neural Network Depth Study (NumPy)
## Fixed Variables 
To isolate the effect of network depth, the following variables were kept constant across all experiments 
    1/dataset generation logic and data distribution
    2/training procedure(train_loop.py, optimizer type, learning rate, batch size, number of epochs)
    3/loss function
    4/activation function 
    5/weight initialization method
    6/random seed
## Introduction
This project explores how the number of hidden layers affects the learning ability of a simple neural network implemented from scratch using NumPy.

## Research Question
How does increasing the number of hidden layers impact model accuracy and learning behavior when trained on the same dataset?

## Initial Hypothesis
Increasing depth will improve performance on non-linear datasets up to a certain point, after which training becomes less stable or inefficient.

## Fairness in Depth Comparison
-The original goal of this research is to study the effect of network depth on prediction performance and training loss. However, during experimentation, the dead ReLU phenomenon emerged, causing models with greater depth than the baseline to stop learning entirely. As a result, the study no longer reflects the impact of depth itself, but instead becomes an investigation of which depths can survive the activation behavior.
-Therefore, an adjustment is necessary to realign the methodology with the original research goal and to produce a fair and unbiased comparison across different depths.
-Learning rate is an important factor alongside activation functions. Using an excessively large learning rate can bias the experimental results, as a learning rate of 0.1 is only suitable for shallow networks. Therefore, redesigning the baseline is necessary to ensure that the study accurately reflects the effect of network depth.
## Scope
- Fully connected neural networks
- Implemented from scratch (no PyTorch / TensorFlow)
- Fixed dataset and training procedure


## Architectural Decisions (across two datasets) 
-ReLU is used in the hidden layers due to its constant derivative in the active region, which allows gradients to propagate more effectively through multiple layers compared to saturating activations such as sigmoid or tanh.
This choice mitigates vanishing gradient effects and enables the study of increased network depth without introducing additional optimization difficulties unrelated to representational capacity.
A sigmoid activation is applied at the output layer to constrain predictions to the [0,1]
[0,1] range, making them interpretable as class probabilities and naturally compatible with binary cross-entropy loss.
-Dataset 1 (Simple Circle)
Role: Sanity Check
In Dataset 1, the role of ReLU is primarily to serve as a sanity check for the network architecture.
The circular decision boundary can be approximated with a small number of linear partitions, allowing a shallow ReLU network to capture the underlying structure without requiring deep compositional representations.
In this setting, ReLU provides the minimal non-linearity needed to form a closed boundary around the circle, verifying that the implementation and training dynamics behave as expected. 

-Dataset 2 (Nested Rings)
Role: Stress Test
Dataset 2 is designed as a stress test in that it places increased representational demands on the network.
The nested ring structure requires the coordination of multiple linear partitions, providing a structured setting to examine how classification performance and gradient behavior vary as network depth increases.
