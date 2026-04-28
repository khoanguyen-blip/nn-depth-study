# Extended Experiments
This directory extends the original nn-depth-study with a second phase of experiments motivated by external feedback received after the project's initial completion.

## Why This Exists
After sharing the original findings with researchers in the deep learning community, a recurring point of critique emerged:

"Deeper networks are tougher to train, but in practice successful training of deep networks often has benefits over shallow networks — lower param count for the same results, better obtainable results overall."
— Yonatan Ariel Slutzky, MSc Researcher

A separate conversation with Yuval Ran-Milo (PhD candidate) further reinforced the importance of situating these experiments within the broader literature — noting that questions around depth and optimization have been studied since at least Glorot & Bengio (2010).
Both conversations pointed to the same gap: the original experiments used a fixed SGD optimizer with no scheduling, which may have systematically disadvantaged deeper models rather than revealing a genuine property of depth itself.
This phase directly addresses that limitation.

## Central Question

Does the apparent underperformance of deeper networks in Phase 1 reflect a fundamental property of depth — or an artifact of undertrained optimization?

Concretely: if deeper models are given proper training conditions (adaptive optimizer, learning rate scheduling), do they recover — or even outperform — shallower baselines?