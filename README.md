### NN-DEPTH-STUDY
This is an observational study focused on optimization dynamics rather than benchmark performance.

## A Small Observational Study on Neural Network Depth (NumPy)
This project investigates how neural network depth influences learning behavior under controlled experimental conditions.
Rather than optimizing for performance, the study focuses on loss dynamics, gradient behavior, and training stability as depth increases.
All neural networks in this project are implemented entirely from scratch using NumPy, without relying on any deep learning frameworks.

## Controlled Setup (Fixed Variables)
To isolate the effect of network depth, the following variables were kept constant across all experiments:
- Dataset generation logic and data distribution
- Training procedure (train_loop.py, optimizer type, learning rate, batch size, number of epochs)
- Loss function (Binary Cross-Entropy)
- Activation functions
- Weight initialization strategy
- Random seed
Network depth is the only variable intentionally modified.

## Introduction
This project explores how the number of hidden layers affects the learning behavior of a simple fully connected neural network implemented from scratch using NumPy.
Instead of assuming that deeper models are inherently better, the study aims to observe how depth influences learning dynamics when all other factors are controlled.

## Research Question
How does increasing network depth affect learning behavior — including loss dynamics, gradient norms, and training stability — under controlled conditions?
Rather than interpreting “better” solely in terms of accuracy, this study examines multiple learning-related signals to provide a broader view of depth-related effects.

## Initial Hypothesis
Increasing network depth improves learning behavior only within a limited range.
Beyond that range, additional depth may introduce unnecessary optimization complexity, leading to increased instability and diminishing performance gains.

## Fairness in Depth Comparison
During early experimentation, the dead ReLU phenomenon emerged in deeper models, causing training to stall completely.
If left unaddressed, this issue would shift the study away from depth analysis and toward survivability under activation behavior.
To preserve fairness and experimental integrity:

- The learning rate was reduced from 0.1 to 0.001, as higher values disproportionately destabilized deeper models
- He initialization was adopted to improve gradient flow through ReLU layers
- Affected experiments were restarted to maintain consistency across depths

These adjustments were applied consistently across all experiments and are documented transparently to preserve experimental integrity.