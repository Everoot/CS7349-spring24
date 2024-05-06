import matplotlib.pyplot as plt

# Sample data
methods = ['Classical', 'Quantum-Enhanced (Grover\'s Algorithm)']
processing_times = [10, 2]  # time to process a large dataset, in hours

plt.figure(figsize=(10, 6))
plt.bar(methods, processing_times, color=['red', 'cyan'])
plt.title('Data Processing Time Comparison')
plt.xlabel('Method')
plt.ylabel('Processing Time (hours)')
plt.ylim(0, 12)
plt.show()
