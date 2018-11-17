import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

energy_ordered_T1 = np.loadtxt("D:/Uni/Lectures/Computational_Physics/project_4_Codes/equilibrium/cmake-build-debug/ordered_T1.txt", usecols=0)
magnet_ordered_T1 = np.loadtxt("D:/Uni/Lectures/Computational_Physics/project_4_Codes/equilibrium/cmake-build-debug/ordered_T1.txt", usecols=1)
moves_ordered_T1 =np.loadtxt("D:/Uni/Lectures/Computational_Physics/project_4_Codes/equilibrium/cmake-build-debug/ordered_T1.txt", usecols=2)

energy_ordered_T2 = np.loadtxt("D:/Uni/Lectures/Computational_Physics/project_4_Codes/equilibrium/cmake-build-debug/ordered_T2.txt", usecols=0)
magnet_ordered_T2 = np.loadtxt("D:/Uni/Lectures/Computational_Physics/project_4_Codes/equilibrium/cmake-build-debug/ordered_T2.txt", usecols=1)
moves_ordered_T2 =np.loadtxt("D:/Uni/Lectures/Computational_Physics/project_4_Codes/equilibrium/cmake-build-debug/ordered_T2.txt", usecols=2)


energy_random_T1 = np.loadtxt("D:/Uni/Lectures/Computational_Physics/project_4_Codes/equilibrium/cmake-build-debug/random_T1.txt", usecols=0)
magnet_random_T1 = np.loadtxt("D:/Uni/Lectures/Computational_Physics/project_4_Codes/equilibrium/cmake-build-debug/random_T1.txt", usecols=1)
moves_random_T1 =np.loadtxt("D:/Uni/Lectures/Computational_Physics/project_4_Codes/equilibrium/cmake-build-debug/random_T1.txt", usecols=2)

energy_random_T2 = np.loadtxt("D:/Uni/Lectures/Computational_Physics/project_4_Codes/equilibrium/cmake-build-debug/random_T2.txt", usecols=0)
magnet_random_T2 = np.loadtxt("D:/Uni/Lectures/Computational_Physics/project_4_Codes/equilibrium/cmake-build-debug/random_T2.txt", usecols=1)
moves_random_T2 =np.loadtxt("D:/Uni/Lectures/Computational_Physics/project_4_Codes/equilibrium/cmake-build-debug/random_T2.txt", usecols=2)


f, (ax1, ax2, ax3) = plt.subplots(1, 3)

f.suptitle("T=1")

ax1.plot(energy_ordered_T1, "blue")
ax1.plot(energy_random_T1, "red")

ax1.set_ylabel("Energy")
ax1.set_xlabel("Lattice sweeps")

ax2.plot(magnet_ordered_T1, "blue")
ax2.plot(magnet_random_T1, "red")

ax2.set_ylabel("Magnetization")
ax2.set_xlabel("Lattice sweeps")

ax3.plot(moves_ordered_T1, "blue")
ax3.plot(moves_random_T1, "red")

ax3.set_ylabel("Accepted moves")
ax3.set_xlabel("Lattice sweeps")

ordered = mpatches.Patch(color='blue', label='Ordered')
random = mpatches.Patch(color='red', label='Random')
plt.legend(handles=[random,ordered])

plt.show()

f, (ax1, ax2, ax3) = plt.subplots(1, 3)

f.suptitle("T=2.4")
ax1.plot(energy_ordered_T2, "blue")
ax1.plot(energy_random_T2, "red")

ax1.set_ylabel("Energy")
ax1.set_xlabel("Lattice sweeps")

ax2.plot(magnet_ordered_T2, "blue")
ax2.plot(magnet_random_T2, "red")

ax2.set_ylabel("Magnetization")
ax2.set_xlabel("Lattice sweeps")

moves_random_T2 = moves_random_T2 / 1000 #rescale to get better plots
moves_ordered_T2 = moves_ordered_T2 / 1000

ax3.plot(moves_ordered_T2, "blue")
ax3.plot(moves_random_T2, "red")

ax3.set_ylabel("Accepted moves/1000")
ax3.set_xlabel("Lattice sweeps")

ordered = mpatches.Patch(color='blue', label='Ordered')
random = mpatches.Patch(color='red', label='Random')
plt.legend(handles=[random,ordered])

plt.show()