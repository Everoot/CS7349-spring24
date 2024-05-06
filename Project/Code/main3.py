import matplotlib.pyplot as plt

# QBER values
qber = [0.5, 1, 1.5, 2]

# Detection probabilities
intercept_resend = [99, 98, 95, 90]
photon_number_splitting = [95, 90, 85, 80]
side_channel = [90, 85, 80, 75]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(qber, intercept_resend, label='Intercept-Resend Attack', marker='o')
plt.plot(qber, photon_number_splitting, label='Photon Number Splitting Attack', marker='s')
plt.plot(qber, side_channel, label='Side-Channel Attack', marker='^')

# Labeling
plt.title('Probability of Detecting Eavesdropper vs. Quantum Bit Error Rate (QBER)')
plt.xlabel('QBER (%)')
plt.ylabel('Detection Probability (%)')
plt.xticks(qber)
plt.yticks(range(70, 101, 5))
plt.legend()
plt.grid(True)

# Show plot
plt.show()
