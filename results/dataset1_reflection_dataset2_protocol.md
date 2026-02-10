# Dataset 1 Reflection and Dataset 2 Experimental Protocol

This document reflects on methodological and procedural lessons learned from Dataset 1 and formalizes a locked experimental protocol for Dataset 2. The goal is to prevent repeated friction, framework drift, and late-stage reconfiguration during subsequent experiments.

---

## 1. Rebaseline – Clarifying the boundary between survivability and performance

During Dataset 1, using a learning rate of ( lr = 0.1 ) resulted in smooth and fast convergence for shallow models (rebaseline and Depth 2). However, under the same configuration, deeper models exhibited severe noise and unstable training dynamics.

The realization that ( lr = 0.1 ) was unsuitable for deeper networks occurred relatively late. In particular, the Depth 4 model encountered training failures due to large oscillations, which necessitated reducing the learning rate to ( lr = 0.001 ) before continuing experiments with Depth 6 and higher depths.

This sequence of events led to the need for rebaselining in order to ensure that all depths were trainable under stable conditions. The experience highlighted that if a baseline does not guarantee survivability across the full depth range, observed results may reflect a model’s tolerance to fixed hyperparameters rather than its true architectural performance.

**Implication for Dataset 2:**
All hyperparameters (learning rate, initialization scheme, and training budget) must be fixed and validated before running the main experiments to avoid rebaselining and to ensure consistency in performance evaluation.

---

## 2. He Initialization

One key insight derived from Dataset 1 is the effectiveness of He initialization in mitigating the dead ReLU problem. Applying He initialization improved gradient propagation without significantly altering the research narrative or experimental objectives.

**Implication for Dataset 2:**
He initialization will be adopted as the default initialization method for all models.

---

## 3. Gradient Norm Analysis

Gradient norm measurements were introduced relatively late compared to basic metrics such as accuracy and loss curves. As a result, early-stage optimization dynamics were not systematically captured from the outset.

Once incorporated, gradient norm analysis provided valuable insights into training stability and depth-dependent optimization behavior.

**Implication for Dataset 2:**
The complete gradient norm pipeline (mean, standard deviation, coefficient of variation, and visualization) will be inherited and reused to accelerate experimentation and reduce implementation overhead.

---

## 4. Train/Test Accuracy and Multiple Runs

The inclusion of train accuracy, test accuracy, and evaluation over multiple runs with different random seeds (10 runs, 10 seeds) was implemented relatively late in Dataset 1, beginning at Day 11 with Depth 6. This required retroactive adjustments to earlier models (rebaseline, Depth 2, and Depth 4).

This experience demonstrated that multi-run evaluation should be integrated from the beginning to ensure fairness and consistency across models.

**Implication for Dataset 2:**
Depth 2 and all baseline models should be included in the multi-run evaluation pipeline from the outset rather than being added later.

---

## 5. Framework-Level and Minor Adjustments

### 5.1 Loss interpretation framework

In the early stages of Dataset 1, the loss interpretation framework was not locked, leading to heterogeneous observations. The later standardization into the C1–C5 criteria significantly improved cross-depth comparability but incurred additional restructuring cost.

**Implication for Dataset 2:**
The loss interpretation framework (including C1–C5 definitions) must be fully specified and frozen prior to training.

---

### 5.2 Results noting framework

Early result notes were exploratory and fragmented across days, which led to repeated content and difficulty in aggregating results into structured tables. Only after standardizing the results framework were observations efficiently consolidated.

**Implication for Dataset 2:**
A clear and fixed results noting framework (organized by aspects or predefined criteria) must be established before experimentation to avoid post hoc consolidation.

---

### 5.3 Minor pipeline adjustments (e.g., removal of `loss_show`)

Several minor adjustments were made during Dataset 1 to simplify the training and logging pipeline, such as removing `loss_show`. While these changes did not affect experimental outcomes, they improved readability and reduced unnecessary noise.

**Implication for Dataset 2:**
The training and logging pipeline should be streamlined and stabilized early, and components that do not directly contribute to analysis should be removed upfront.

---

### 5.4 Framework summary

Overall, framework-related adjustments in Dataset 1 primarily resulted from late decision locking. Although these changes improved clarity and consistency, they increased mid-experiment overhead.

**Implication for Dataset 2:**
All logging, result notation, and visualization frameworks should be treated as integral components of the experimental protocol rather than adjustable elements during experimentation.

---

## 6. Dataset 2 Experimental Protocol (Locked)

Based on the reflections above, the following protocol is fixed for Dataset 2.


### 6.1 Locked definitions

* Layer definition: one layer equals Linear + Activation
* Depth: number of hidden layers
* Training budget: fixed number of epochs for all depths
* Evaluation split: fixed across all experiments

### 6.2 Baseline and hyperparameters (LOCKED)

* Initialization: He initialization
* Learning rate: fixed prior to experimentation
* Optimizer: fixed
* Loss function: fixed
* Number of epochs: fixed

> All baselines must be validated to ensure that every depth can be trained stably before running full experiments.

### 6.3 Metrics and logging

* Loss behavior: C1–C5 framework
* Performance: train accuracy and test accuracy (mean ± std over multiple runs)
* Gradient analysis: mean, standard deviation, coefficient of variation, and qualitative gradient regime

### 6.4 Visualization

* Loss curves for all depths
* Gradient norm plots for all depths
* Figures generated as part of the experimental pipeline


---

