import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def generate_microstate_sequence(n_samples, rigidity_level):
    states = np.zeros(n_samples, dtype=int)
    current_state = np.random.randint(0, 4) 
    for i in range(n_samples):
        if np.random.rand() > rigidity_level:
            current_state = np.random.randint(0, 4)
        states[i] = current_state
    return states

def calculate_transition_matrix(states, n_states=4):
    matrix = np.zeros((n_states, n_states))
    for (i, j) in zip(states[:-1], states[1:]):
        matrix[i, j] += 1
    row_sums = matrix.sum(axis=1, keepdims=True)
    matrix_prob = np.divide(matrix, row_sums, out=np.zeros_like(matrix), where=row_sums!=0)
    return matrix_prob

# --- EXPERIMENT ---
N = 2000 
flexible_states = generate_microstate_sequence(N, 0.05)
rigid_states = generate_microstate_sequence(N, 0.90)

tm_flex = calculate_transition_matrix(flexible_states)
tm_rigid = calculate_transition_matrix(rigid_states)

# --- VISUALIZATION ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

sns.heatmap(tm_flex, annot=True, fmt=".2f", cmap='Greens', ax=ax1, vmin=0, vmax=1, square=True)
ax1.set_title("Cerebro Flexible (Salud)\nTransiciones Distribuidas", fontsize=14)
ax1.set_xlabel("Estado Destino (t+1)", fontsize=12)
ax1.set_ylabel("Estado Origen (t)", fontsize=12)

sns.heatmap(tm_rigid, annot=True, fmt=".2f", cmap='Reds', ax=ax2, vmin=0, vmax=1, square=True)
ax2.set_title("Cerebro Rígido (Neurosis/Insolvencia)\nAtractores Profundos (Diagonal)", fontsize=14)
ax2.set_xlabel("Estado Destino (t+1)", fontsize=12)
ax2.set_ylabel("Estado Origen (t)", fontsize=12)

plt.tight_layout()
plt.show()
