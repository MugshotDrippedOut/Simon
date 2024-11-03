import matplotlib.pyplot as plt

# # Data for U_CE = 1 V
# IB_1V = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.3, 0.66, 1.04]  # mA
# UBE_1V = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.601, 0.7, 0.794, 0.886, 0.978]  # V
# # Data for U_CE = 2 V
# IB_2V = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.04, 0.22, 0.6, 0.98]  # µA
# UBE_2V = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7,0.796,0.888,0.98]  # V
# # Plotting the data
# plt.figure(figsize=(10, 6))
# plt.plot(IB_1V, UBE_1V, label=r"$U_{CE}$ = 1 V", marker="o", color="blue")
# plt.plot(IB_2V, UBE_2V, label=r"$U_{CE}$ = 2 V", marker="x", color="red")
# # Adding labels and title
# plt.xlabel(r"$I_B$ (μA)")
# plt.ylabel(r"$U_{BE}$ (V)")
# plt.legend()
# plt.grid(True)
# plt.show()
# 
# # Data pro U_CE = 1 V
# IB_1V = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.6, 6.0, 21.2, 50.6, 107.2, 169.8, 233.4, 297.8, 362.2]  # µA
# IC_1V = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.12, 0.70, 3.08, 7.46, 7.78, 7.82, 7.84, 7.85, 7.66]  # mA
# # Data pro U_CE = 2 V
# IB_2V = [0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 1.6, 6.0, 21.6, 53.2, 92.8, 143.6, 205.8, 270.0, 334.0]  # µA
# IC_2V = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.12, 0.72, 3.20, 8.32, 14.14, 15.56, 15.74, 15.80, 15.86]  # mA
# # Vykreslení grafu
# plt.figure(figsize=(10, 6))
# plt.plot(IB_1V, IC_1V, label=r"$U_{CE} = 1 \, V$", marker="o", color="blue")
# plt.plot(IB_2V, IC_2V, label=r"$U_{CE} = 2 \, V$", marker="x", color="red")
# # Popisky os a titulky
# plt.xlabel(r"$I_B$ [μA]")
# plt.ylabel(r"$I_C$ [mA]")
# plt.legend()
# plt.grid(True)
# plt.show()

# Data z tabulky pro I_B = 20 μA
IC_20uA = [2.92, 2.92, 2.94, 2.96, 2.96, 2.98, 3.00, 3.00, 3.02, 3.02, 3.04, 3.06, 3.06, 3.08, 3.10, 3.10, 3.20]  # mA
UCE_20uA = [2.377, 2.507, 2.645, 2.780, 2.918, 3.052, 3.195, 3.338, 3.481, 3.626, 3.769, 3.913, 4.060, 4.210, 4.360, 4.510, 4.640]  # V

# Data z tabulky pro I_B = 40 μA
IC_40uA = [4.58, 4.78, 4.98, 5.20, 5.38, 5.48, 5.52, 5.56, 5.60, 5.66, 5.70, 5.74, 5.84, 5.88, 5.94, 6.00, 6.06]  # mA
UCE_40uA = [0.703, 0.740, 0.786, 0.850, 0.960, 1.166, 1.410, 1.658, 1.906, 2.150, 2.416, 2.678, 2.932, 3.201, 3.482, 3.761, 4.050]  # V

# Vykreslení grafu
plt.figure(figsize=(10, 6))
plt.plot(IC_20uA, UCE_20uA, label=r"$I_B = 20 \, \mu A$", marker="o", color="blue")
plt.plot(IC_40uA, UCE_40uA, label=r"$I_B = 40 \, \mu A$", marker="x", color="red")

# Popisky os a titulky
plt.xlabel(r"$I_C$ [mA]")
plt.ylabel(r"$U_{CE}$ [V]")
plt.legend()
plt.grid(True)
plt.show()
