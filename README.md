# Neurodynamic Rigidity (NR) Index

Official implementation of the **NR Index**, a computational metric to quantify stability and energetic costs of neural inference in psychiatry.

## Theoretical Background
## 🚀 Latest Empirical Validation (March 2026)
The NR Index has been validated using high-resolution EEG data. 

**Key Findings:**
* **Pathological Rigidity:** Clinical schizophrenia models (ASZED) show a **1803.89% increase** in NR compared to healthy controls.
* **The Entropy Paradox:** Traditional Shannon Entropy remained identical ($H=0.57$) between subjects, while the NR Index successfully captured the "Erasure Insolvency" and temporal freezing.
* **Task-Induced Flexibility:** In healthy subjects, cognitive load decreases NR by ~71%, demonstrating adaptive dissipative capacity.
[cite_start]While contemporary models propose dimensional frameworks [cite: 300] [cite_start]or measure statistical complexity loss[cite: 436, 484], the **NR Index** identifies the underlying mechanical cause: energetic saturation due to dimensional over-parameterization.

System stability is governed by:
$$\frac{d\Phi}{dt} = \eta \cdot \Omega(\xi) - \alpha(\Phi)$$

Where:
- **$\Phi$**: Accumulated Entropic Overhead.
- **$\alpha$**: Dissipative Capacity of the neural substrate.

## Quick Start
1. Install dependencies: `pip install -r requirements.txt`
2. Run analysis on your state trajectories (e.g., HMM outputs).

## Suggested Citation

Tapia-Castañeda, H. E. (2026). *Energetic and Regulatory Constraints as a Missing Mechanistic Layer in Computational Psychiatry*.
