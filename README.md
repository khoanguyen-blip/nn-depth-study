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
Network depth is the only variable intentionally varied.

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
If left unaddressed, this issue would shift the study away from depth analysis and toward analyzing activation failure rather than depth effects.
To preserve fairness and experimental integrity:

- The learning rate was reduced from 0.1 to 0.001, as higher values disproportionately destabilized deeper models
- He initialization was adopted to improve gradient flow through ReLU layers
- Affected experiments were restarted to maintain consistency across depths

These adjustments were applied consistently across all experiments and are documented transparently to preserve experimental integrity.

## Reproducibility
All experiments in this study were conducted using the same core implementation located in the module/ directory.
A unified setup was applied across all models, based on the post-rebaseline configuration introduced after Dataset 1 adjustments.

To ensure fair comparison across depths:
- 10 training seeds (`data/testing_seeds.txt`)
- 10 evaluation seeds (offset by +100 from training seeds)
- Identical hyperparameters across depths
- Post-rebaseline configuration (Dataset 1 stabilized setup)

Libraries Used
The following libraries were used during experimentation:
- numpy
- matplotlib

Baseline Notebook
All subsequent experiments were carried out based on a shared baseline established in:
notebooks/day9_circle_rebaseline.ipynb
From this baseline, only the network depth or dataset was modified depending on the experiment.

Experiment Timeline
- Day 9–14: Circle dataset experiments
- Day 16–19: Nested Rings dataset experiments
All numerical results, visualizations, and experimental observations are documented in:
- results/
- observations/ 

## Contributions

This study provides:
- A controlled empirical comparison of fully-connected networks across increasing depth.
- Gradient norm diagnostics across multiple random seeds.
- Transparent documentation of instability phenomena (dead ReLU, depth sensitivity).
- A transparent NumPy-based experimental framework.

## References

Foundational Papers
The following foundational works informed the theoretical background of this project:
- Glorot & Bengio (2010) — Understanding the difficulty of training deep feedforward neural networks
- Bengio, Simard & Frasconi (1994) — Learning long-term dependencies with gradient descent is difficult
- He et al. (2015) — Delving Deep into Rectifiers
These works provide theoretical and empirical foundations for understanding gradient propagation, instability, and initialization behavior in deep neural networks, which directly motivate the depth-based experiments conducted in this project.

Online Learning Resources and Insights
1. [3Blue1Brown — Neural Networks Series](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr)


2. [Towards Data Science — The Dying ReLU Problem Clearly Explained](https://towardsdatascience.com/the-dying-relu-problem-clearly-explained-42d0c54e0d24/)



## Installation
1. Clone the repository
```bash
git clone https://github.com/khoanguyen-blip/nn-depth-study.git
cd nn-depth-study
```
2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # macOS / Linux
```
3. Install dependencies
```bash
pip install -r requirements/dev.txt
```


## How to Run
Main experiments were conducted using Jupyter notebooks.
Start Jupyter
```bash 
jupyter notebook
```
Then open the relevant notebook inside the notebooks/ directory.
Results and figures will be saved in:
- 'results/'
- 'figures/'

Note:
Some early notebooks (pre-rebaseline phase) may not run under the final configuration.
They are preserved for transparency to reflect the original experimental progression.
