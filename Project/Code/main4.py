import matplotlib.pyplot as plt

# Sample data
methods = ['Classical', 'Quantum-Enhanced']
response_times = [48, 24]  # hours

plt.figure(figsize=(10, 6))
plt.bar(methods, response_times, color=['blue', 'green'])
plt.title('Data Breach Response Time Comparison')
plt.xlabel('Encryption Method')
plt.ylabel('Response Time (hours)')
plt.ylim(0, 60)
plt.show()
