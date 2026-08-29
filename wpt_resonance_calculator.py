import math

def calculate_compensation_capacitance(inductance_uH, freq_kHz=85.0):
    """Calculates required series resonant capacitance for target frequency."""
    L = inductance_uH * 1e-6
    f = freq_kHz * 1e3
    C = 1.0 / (4 * (math.pi ** 2) * (f ** 2) * L)
    return C * 1e9  # Convert to nF

# Coil parameters from paper
L_primary_uH = 40.58
L_secondary_uH = 44.46
target_freq_kHz = 85.0

C_p_nF = calculate_compensation_capacitance(L_primary_uH, target_freq_kHz)
C_s_nF = calculate_compensation_capacitance(L_secondary_uH, target_freq_kHz)

print("--- Resonant Compensation Network Calculator (85 kHz) ---")
print(f"Primary Coil Inductance (Lp)   : {L_primary_uH:.2f} uH")
print(f"Calculated Primary Cap (Cp)    : {C_p_nF:.2f} nF")
print("---------------------------------------------------------")
print(f"Secondary Coil Inductance (Ls) : {L_secondary_uH:.2f} uH")
print(f"Calculated Secondary Cap (Cs)  : {C_s_nF:.2f} nF")
