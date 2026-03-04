import numpy as np
import pandas as pd
from scipy.stats import zscore

def compute_nr_metrics(states, signal=None):
    """
    Computes dynamical metrics for the Neurodynamic Rigidity (NR) Index.
    Based on the energetic constraints framework (Tapia-Castañeda, 2026).
    """
    # 1. Switching Rate: Frequency of transitions between states
    transitions = np.sum(states[1:] != states[:-1])
    sw_rate = transitions / len(states)

    # 2. Mean Dwell Time: Average time spent in a single state
    diffs = np.where(states[1:] != states[:-1])[0]
    dwells = np.diff(np.concatenate(([0], diffs, [len(states)-1])))
    mean_dwell = np.mean(dwells)

    # 3. Lag-1 Autocorrelation: Temporal persistence of the signal
    ac1 = 0
    if signal is not None:
        ac1 = np.corrcoef(signal[:-1], signal[1:])[0, 1]

    return sw_rate, mean_dwell, ac1

def compute_nr_index(sw_rate, mean_dwell, ac1):
    """
    Synthesizes the NR Index using Z-scored metrics.
    NR increases with persistence and decreases with flexibility.
    """
    # Switching rate is subtracted as it indicates flexibility, not rigidity
    nr_score = zscore([mean_dwell])[0] + zscore([ac1])[0] - zscore([sw_rate])[0]
    return nr_score

if __name__ == "__main__":
    print("Neurodynamic Rigidity Index engine loaded successfully.")