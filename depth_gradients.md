                                        A SMALL STUDY ON NETWORK'S DEPTH, GRADIENTS, AND LEARNING BEHAVIOR
                                        

I/Introduction
-Motivation:
This study was carried out mainly out of curiosity about how neural networks are designed, especially how the depth of a network relates to its behavior during learning. Instead of starting from the assumption that deeper models are always better, this work aims to observe how changing the number of layers affects the learning process under controlled conditions. In particular, the study explores whether there appears to be a minimum or maximum depth at which the model learns more effectively or more stably.
This study does not aim to propose an optimal architecture or achieve high performance. Rather, it is intended as a small observational reference that highlights differences in learning behavior as network depth increases. The results may be useful for future projects or studies that require a basic but careful understanding of how depth influences learning in neural networks.
-Paper philosophy (observational-first):
This study is conducted in a context where I did not begin with clear knowledge, but only a small set of initial hypotheses about how network depth might affect gradient norms, accuracy, and loss behavior. In short, the study is carried out in an “on-the-fly” manner, where observations are formed during experimentation rather than being fixed in advance. Throughout the process, I record model performance, loss behavior, and gradient norms, together with corresponding loss curves and gradient norm plots. At the end of each dataset, these observations are summarized to gradually improve my understanding of how depth influences learning behavior.
In this study, results are recorded as honestly as possible, without adjusting or beautifying outcomes. Both visual outputs and textual notes are preserved as direct representations of the experiments. This can be seen most clearly in the inclusion of raw loss samples for each observation, which are presented without selection or filtering. During the research process, several issues emerged, particularly in the first dataset (Circle), such as dead ReLU activations, the absence of certain metrics, and the need to re-establish a baseline due to unsuitable hyperparameter choices across the project. These issues are explicitly documented and carried forward as considerations when transitioning to the second dataset (Nested Rings).
Regarding the scope of this study, no external deep learning libraries or predefined modules are used to construct the neural networks. All network components, data generation procedures, and datasets are implemented with the support of NumPy, and visualized using Matplotlib. This deliberate choice is made to help me better understand neural network structures, identify issues arising from activation functions, and learn how to address them directly, rather than relying on or modifying existing deep learning library implementations.
II/Research Questions and Working Hypotheses
-Research questions: 
This study is motivated by a simple question I had when first learning about neural networks: does increasing depth actually make a model better at learning? Rather than interpreting “better” only in terms of accuracy, this study expands the question to consider multiple aspects of the learning process.
Specifically, the research focuses on how changes in network depth affect not only final accuracy, but also gradient norms, loss behavior, and the shape of loss curves during training. By shifting the focus away from accuracy alone, the study aims to compare learning behavior across different depths from several perspectives, instead of relying on a single performance metric.
-Working Hypotheses:
At the beginning of this study, I initially believed that increasing network depth would consistently lead to better learning on nonlinear datasets. This belief came from the idea that adding depth also increases the number of neurons involved in processing the data, which could allow the model to represent more complex patterns and learn more effectively.
However, as I reflected on this assumption before conducting the experiments, this initial belief was gradually replaced by a more cautious hypothesis. I began to consider that increasing depth might improve learning only up to a certain point. Beyond that point, making the network deeper could introduce unnecessary complexity, potentially leading to unstable training behavior and reduced effectiveness across metrics such as accuracy, loss behavior, and gradient norms. This study is therefore guided by the hypothesis that depth improves learning only within a limited range, rather than indefinitely.
III/Experimental Setup and Scope
-From-scratch NN
-Controlled variables
-Dataset design (Circle → Nested Rings)
-Scope
IV/Observed Failures and Training Instabilities
V/Results Overview
VI/Analysis / Interpretation
VII/Limitations
IX/Conclusion