import numpy as np
import matplotlib.pyplot as plt

file_1="data_1\\transition_100.txt"
file_2="data_2\\transition_100.txt"
file_3="data_3\\transition_100.txt"

energy_1 = np.loadtxt(file_1, usecols=0)
energy_2 = np.loadtxt(file_2, usecols=0)
energy_3 = np.loadtxt(file_3, usecols=0)
energy_mean = (energy_1 + energy_2 + energy_3) / 3
energy_std = np.sqrt(((energy_1 ** 2 + energy_2 ** 2 + energy_3 ** 2) / 3 - energy_mean ** 2) / 3)

magnet_1 = np.loadtxt(file_1, usecols=2)
magnet_2 = np.loadtxt(file_2, usecols=2)
magnet_3 = np.loadtxt(file_3, usecols=2)
magnet_mean = (magnet_1 + magnet_2 + magnet_3) / 3
magnet_std = np.sqrt(((magnet_1 ** 2 + magnet_2 ** 2 + magnet_3 ** 2) / 3 - magnet_mean ** 2) / 3)

suscep_1 = np.loadtxt(file_1, usecols=4)
suscep_2 = np.loadtxt(file_2, usecols=4)
suscep_3 = np.loadtxt(file_3, usecols=4)
suscep_mean = (suscep_1 + suscep_2 + suscep_3) / 3
suscep_std = np.sqrt(((suscep_1 ** 2 + suscep_2 ** 2 + suscep_3 ** 2) / 3 - suscep_mean ** 2) / 3)

speche_1 = np.loadtxt(file_1, usecols=5)
speche_2 = np.loadtxt(file_2, usecols=5)
speche_3 = np.loadtxt(file_3, usecols=5)
speche_mean = (speche_1 + speche_2 + speche_3) / 3
speche_std = np.sqrt(((speche_1 ** 2 + speche_2 ** 2 + speche_3 ** 2) / 3 - speche_mean ** 2) / 3)



T = np.loadtxt(file_1, usecols=6)


f, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4)

plot_x = T
plot_y_1 = energy_mean
error_y_1 = 3*energy_std
plot_y_2 = magnet_mean
error_y_2 = 3*magnet_std
plot_y_3 = suscep_mean
error_y_3 = 3 * suscep_std
plot_y_4 = speche_mean
error_y_4 = 3*speche_std

f.suptitle('40x40 Lattice')

ax1.errorbar(plot_x, plot_y_1, yerr=error_y_1, marker='o')
ax1.set_xlabel('Temperature')
ax1.set_ylabel('Energy/Spin')


ax2.errorbar(plot_x, plot_y_2, yerr=error_y_2, marker='o')
ax2.set_xlabel("Temperature")
ax2.set_ylabel("Magnetization/Spin")

ax3.errorbar(plot_x, plot_y_3, yerr=error_y_3, marker='o')
ax3.set_xlabel("Temperature")
ax3.set_ylabel("Susceptebility")

ax4.errorbar(plot_x, plot_y_4, yerr=error_y_4, marker='o')
ax4.set_xlabel("Temperature")
ax4.set_ylabel("Specific Heat")

plt.show()
