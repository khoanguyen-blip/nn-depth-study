A Small Observational Study on Network Depth, Gradients, and Learning Behavior
Research Question
Does increasing network depth actually improve learning behavior, and if so, within what range?
Rather than evaluating “better” solely through accuracy, this study investigates how network depth influences loss dynamics, gradient norms, and training stability under controlled conditions.
Experimental Design and Dataset Progression
To isolate the effect of depth, fully connected neural networks were implemented entirely from scratch using NumPy, with all variables held constant except the number of layers.
Two synthetic datasets with increasing difficulty were used:
Circle dataset: a simple nonlinear task used as a sanity check for implementation correctness and baseline behavior.
Nested Rings dataset: a more complex nonlinear structure used to stress-test learning dynamics as depth increases.
Network depths of 1, 2, 4, 6, and 8 layers were evaluated under identical training procedures, loss functions (Binary Cross-Entropy), activation functions (ReLU + Sigmoid), initialization strategy, and random seeds.
Key Observations (Loss & Depth)
On the circle dataset, increasing depth does not improve training or testing accuracy. Performance saturates early, while loss curves become more oscillatory as depth increases.
Gradient-based metrics (mean gradient norm, standard deviation, coefficient of variation) increase consistently with depth, even when performance remains unchanged.
On the nested rings dataset, testing accuracy improves with depth up to an intermediate range (around depth 4), after which gains saturate.
Loss curves and gradient metrics exhibit clearer depth-dependent patterns on the harder dataset, suggesting that depth influences learning behavior more strongly as task complexity increases.
What Failed (and Why It Matters)
Dead ReLU activations were observed in early experiments due to unsuitable initialization, preventing effective gradient flow.
Initial hyperparameter choices, particularly learning rate, caused unstable training in deeper models and required rebaselining.
Crucial metrics (gradient statistics, accuracy, repeated runs) were missing in early stages, limiting the reliability of initial observations.
These failures were explicitly documented, corrected, and carried forward into later experiments, shaping a more robust experimental protocol.
What This Suggests (Not Conclusions)
Increasing depth appears to amplify gradient activity regardless of performance gains.
Depth improves learning behavior only within a limited range, particularly on more complex datasets.
Beyond that range, additional depth introduces instability without clear benefits.
The alignment between gradient norm saturation and performance saturation suggests that depth-related benefits may be constrained by optimization dynamics rather than representational capacity alone.
These observations are specific to the controlled setup of this study and should not be generalized beyond its scope.
Scope and Limitations
This study is limited to small fully connected networks, simple optimization schemes, and low-dimensional synthetic datasets. No modern architectural components (e.g., residual connections, normalization, adaptive optimizers) are used. The goal is interpretability rather than performance.
Note: This summary is intended as an observational reference rather than a performance claim. Results are recorded honestly, including instability and failure cases, to preserve interpretability and experimental integrity.