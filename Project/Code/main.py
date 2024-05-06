import matplotlib.pyplot as plt
import numpy as np

# Dataset sizes in GB (x-axis)
dataset_sizes = np.array([1, 10, 100, 1000])

# Simulated processing times for classical methods (y-axis), assuming exponential growth
classical_times = np.array([1, 10, 100, 1000])

# Simulated processing times for quantum methods using Grover's algorithm (y-axis), assuming square root growth
quantum_times = np.sqrt(classical_times) * 10  # Adjusted for comparison

plt.figure(figsize=(10, 6))

plt.plot(dataset_sizes, classical_times, label='Classical Processing', marker='o')
plt.plot(dataset_sizes, quantum_times, label='Quantum Processing (Grover\'s Algorithm)', marker='s')

plt.title('Graph 1: Performance Comparison of Data Processing: Classical vs Quantum')
plt.xlabel('Dataset Size (GB)')
plt.ylabel('Processing Time (Arbitrary Units)')
plt.xscale('log')
plt.yscale('log')
plt.xticks(dataset_sizes, labels=[f'{size}GB' for size in dataset_sizes])
plt.legend()
plt.grid(True, which="both", ls="--")

plt.show()
