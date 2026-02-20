# Benchmark Protocol Specification
---
## 1. Seed Handling Policy
All experiments are conducted using 10 independent training seeds.
Training seeds are fixed as integers from 1 to 10.
For each training seed 
s, evaluation is performed using a distinct test seed equal to s+100.
Training and test seeds are strictly separated to prevent any overlap in dataset generation.
The same set of training and evaluation seeds is used consistently across all depth configurations.
The seed policy was established after the rebaseline event and remains fixed for all reported experiments.
This policy ensures reproducibility, deterministic comparisons across models, and elimination of train–test contamination.

--- 
## 2. Logging Framework
All results are recorded under a predefined logging structure.
Dataset-level results are logged in:
'results/results_framework.txt'
Observation records are dataset-specific:
- Dataset 1 (Circle):
'observations/day9_circle_rebaseline_observation.txt'
- Dataset 2 (Nested Rings):
'observations/day16_nestedrings_baseline_observation.txt'
The observation structure differs between datasets due to additional gradient-related metrics introduced in Dataset 2, as defined in:
'results/dataset1_reflection_dataset2_protocol.md'
Logging formats are fixed and are not modified across depth configurations.

---
## 3. Metric Computation Definition
The following metrics are computed for each model:
Training accuracy (mean over 10 runs)
Test accuracy (mean over 10 runs)
Gradient norm mean
Gradient norm standard deviation
Final 100-epoch loss samples per run
Gradient norm is computed as the global L2 norm across all parameters per training step.
All metric values are stored in their respective dataset observation files.
No additional metrics are included unless explicitly specified in the protocol.

---
## 4. Plot Standardization Rules
- 4.1 Loss Curve
X-axis: Epoch
Y-axis: Loss (BCE)
Title format:
Training Loss Curve (<Model Name>)
File names must encode model configuration explicitly.
- 4.2 Gradient Norm Plot
X-axis: Epoch
Y-axis: Gradient norm
Title format:
Gradiet Norm Trend (<Model Name>)
File names must encode model configuration explicitly.
File names encode model configuration explicitly.
Plot formatting conventions remain fixed across all runs.
Note : dataset 1 rebaseline's model name is depth1 for gradnorm plot

---
## 5. Depth Counting Rule
In this protocol:
One layer is defined as one Linear module followed by one activation function.
Depth equals the number of Linear + Activation blocks.
The output layer is excluded from depth counting.
Model naming follows explicit architecture declaration.
- Example:
Neural_Network([2,16,16,16,16,16,16,1])
is defined as a depth-6 model.
Width remains fixed across all depth configurations.

---
## 6. Valid Run Definition
A training run is considered valid if all the following conditions are met:
The training process completes the full predefined number of epochs.
No numerical instability occurs (e.g., NaN or Inf in loss or gradients).
Loss decreases during the early training phase (first N epochs) without divergence.
All required metrics are successfully logged.
Runs failing any of these conditions are excluded from aggregate statistics.

--- 
## 7. Failure Criteria
A model configuration is considered unstable or failed if:
Loss diverges or increases uncontrollably during training.
Gradient norms explode beyond a predefined numerical threshold.
Numerical instability (NaN/Inf) occurs.
Training terminates prematurely due to runtime errors.
All failures must be logged explicitly and are not silently discarded.