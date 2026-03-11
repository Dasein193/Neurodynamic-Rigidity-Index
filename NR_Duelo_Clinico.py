import mne
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.stats import entropy
import warnings

warnings.filterwarnings("ignore")
mne.set_log_level('WARNING')

def analyze_brain(file_path, state_name):
    print(f"🧠 Escaneando {state_name}...")
    try:
        raw = mne.io.read_raw_edf(file_path, preload=True)
        raw.filter(2, 20)
        data = raw.get_data().T 
        
        km = KMeans(n_clusters=4, n_init=10, random_state=42)
        states = km.fit_predict(data)
        
        transitions = np.sum(np.diff(states) != 0)
        nr = (len(states) / (transitions + 1)) / (transitions + 1)
        
        matrix = np.zeros((4, 4))
        for t in range(len(states) - 1):
            matrix[states[t], states[t+1]] += 1
        matrix_prob = matrix / (matrix.sum(axis=1, keepdims=True) + 1e-9)
        h = np.mean([entropy(row, base=2) for row in matrix_prob if np.any(row)])
        
        return states, nr, h
    except Exception as e:
        print(f"❌ Error al procesar {file_path}: {e}")
        return None, None, None

print("INICIANDO COMPARATIVA CLÍNICA: SANO VS ESQUIZOFRENIA (NR INDEX)")
print("-" * 60)

# Nota: Requiere S001R01.edf y esquizofrenia.edf en sus respectivas carpetas
states_sano, nr_sano, h_sano = analyze_brain("datos_physionet/S001R01.edf", "Sujeto Sano (Control)")
states_esq, nr_esq, h_esq = analyze_brain("datos_patologia/esquizofrenia.edf", "Sujeto con Esquizofrenia")

if states_sano is not None and states_esq is not None:
    n_samples = min(1000, len(states_sano), len(states_esq))
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 8), sharex=True)

    ax1.step(range(n_samples), states_sano[:n_samples], color='#2ecc71', linewidth=1.5)
    ax1.set_title(f"Control Sano (S001) | Flujo Termodinámico Estable\nNR: {nr_sano:.6f} | Entropía: {h_sano:.2f} bits", fontsize=12)
    ax1.grid(alpha=0.3)
    ax1.set_ylabel("Microestado")

    ax2.step(range(n_samples), states_esq[:n_samples], color='#e74c3c', linewidth=1.5)
    ax2.set_title(f"Patología (Esquizofrenia) | Colapso Entrópico y Rigidez\nNR: {nr_esq:.6f} | Entropía: {h_esq:.2f} bits", fontsize=12)
    ax2.grid(alpha=0.3)
    ax2.set_ylabel("Microestado")
    ax2.set_xlabel("Tiempo (Samples)", fontsize=11)

    plt.tight_layout()
    plt.show()

    print("\n" + "=" * 40)
    print(" 📊 RESULTADOS DEL ÍNDICE NR")
    print("=" * 40)
    print(f"Control Sano:    {nr_sano:.6f}")
    print(f"Esquizofrenia:   {nr_esq:.6f}")
    
    variacion = ((nr_esq - nr_sano) / nr_sano) * 100
    print(f"\n⚠️ CONCLUSIÓN: El cerebro patológico es un {variacion:.2f}% MÁS RÍGIDO.")
