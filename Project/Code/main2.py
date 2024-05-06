import matplotlib.pyplot as plt
import numpy as np

# Dataset sizes (log scale)
sizes = np.array([1000, 10000, 100000, 1000000])
classical_times = np.array([1, 10, 100, 1000])
quantum_times = np.array([1, 3.16, 10, 31.6])

plt.figure(figsize=(10, 6))
plt.plot(sizes, classical_times, 'o-', label='Classical Processing')
plt.plot(sizes, quantum_times, 's-', label='Quantum Processing (Grover\'s Algorithm)')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Dataset Size (entries)')
plt.ylabel('Processing Time (s)')
plt.title('Graph 1: Data Processing Times: Classical vs. Quantum')
plt.legend()
plt.grid(True)
plt.show()
