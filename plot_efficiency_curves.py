import matplotlib.pyplot as plt
import numpy as np

# Set figure configuration
plt.rcParams['font.sans-serif'] = 'Arial'
plt.figure(figsize=(7, 5), dpi=300)

# Misalignment range (0 to 50 cm / 0 to 500 mm)
x_dist = np.linspace(0, 50, 100)

# Efficiency models
baseline_air = 80.0 * np.exp(-x_dist / 15.0)
single_nim = 85.0 * np.exp(-x_dist / 25.0)
double_nim = 89.4 * np.exp(-x_dist / 40.0)

# Plot curves
plt.plot(x_dist, double_nim, 'b-', linewidth=2.5, label='Double-Sided NIM (Proposed)')
plt.plot(x_dist, single_nim, 'g--', linewidth=2.0, label='Single-Sided NIM')
plt.plot(x_dist, baseline_air, 'r:', linewidth=2.0, label='Air-Core Baseline')

# Reference lines
plt.axhline(y=89.4, color='black', linestyle='-.', alpha=0.5, label='Peak Target Efficiency (89.4%)')
plt.axhline(y=50.0, color='gray', linestyle=':', alpha=0.5)

# Axis formatting
plt.title('DC-DC Link Efficiency vs Lateral Misalignment (f = 85 kHz)', fontsize=11, fontweight='bold')
plt.xlabel('Lateral Misalignment Offset (cm)', fontsize=10)
plt.ylabel('DC-DC Stage Efficiency (%)', fontsize=10)
plt.xlim(0, 50)
plt.ylim(0, 100)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(fontsize=9, loc='lower left')

# Save high-res plot
output_img = 'Efficiency_vs_Misalignment_300DPI.png'
plt.savefig(output_img, dpi=300, bbox_inches='tight')
plt.show()

print(f"Saved publication figure: {output_img}")
