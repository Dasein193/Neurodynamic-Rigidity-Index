import mne
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import warnings

warnings.filterwarnings("ignore")
mne.set_log_level('WARNING')

def get_nr(file_path):
    raw = mne.io.read_raw_edf(file_path, preload=True)
    raw.filter(2, 20)
    data = raw.get_data().T
    labels = KMeans(n_clusters=4, n_init=10, random_state=42).fit_predict(data)
    
    transitions = np.sum(np.diff(labels) != 0)
    nr = (len(labels) / (transitions + 1)) / (transitions + 1)
    return labels, nr

print("🧠 Analizando Reposo vs Tarea (Sujeto Sano 001)...")
# Nota: Requiere los archivos S001R01.edf y S001R04.edf en la carpeta datos_physionet
st_reposo, nr_reposo = get_nr("datos_physionet/S001R01.edf")
st_tarea, nr_tarea = get_nr("datos_physionet/S001R04.edf")

# --- VISUALIZATION ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 8), sharex=True)

ax1.step(range(1000), st_reposo[:1000], color='#2ecc71')
ax1.set_title(f"Estado Flexible (Reposo) | NR: {nr_reposo:.6f}")

ax2.step(range(1000), st_tarea[:1000], color='#e67e22')
ax2.set_title(f"Estado Hiper-Flexible (Tarea Cognitiva) | NR: {nr_tarea:.6f}")

plt.xlabel("Tiempo (Samples)")
plt.tight_layout()
plt.show()

print(f"\nVariación del Índice NR: {((nr_tarea - nr_reposo)/nr_reposo)*100:.2f}%")
