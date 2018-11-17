import numpy as np
import matplotlib.pyplot as plt

energy_T1 = np.loadtxt("D:/Uni/Lectures/Computational_Physics/project_4_Codes/probability/cmake-build-debug/energy_probability_T1.txt")
energy_T2 = np.loadtxt("D:/Uni/Lectures/Computational_Physics/project_4_Codes/probability/cmake-build-debug/energy_probability_T2.txt")

bins_1 = 34
bins_2 = 5
f, (ax1, ax2) = plt.subplots(1, 2)

f.suptitle("Probability distribution")

ax1.set_title("T=1")
ax1.set_xlabel("Energy")
ax1.set_ylabel("Energy counts for 5*10^5 MC cycles")

ax1.hist(energy_T1,bins_2)

ax2.set_title("T=2.4")
ax2.set_xlabel("Energy")
ax2.set_ylabel("Energy counts for 5*10^5 MC cycles")

ax2.hist(energy_T2,bins_1)
plt.show()