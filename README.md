# nn-depth-study
Studying the effect of neural network depth using NumPy
# Neural Network Depth Study (NumPy)

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
