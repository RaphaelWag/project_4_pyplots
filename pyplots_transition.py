import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from numpy.core.multiarray import ndarray

energy_40 = np.loadtxt("transition_40.txt", usecols=0)
magnet_40 = np.loadtxt("transition_40.txt", usecols=2)
suszep_40 = np.loadtxt("transition_40.txt", usecols=4)
spezhe_40 = np.loadtxt("transition_40.txt", usecols=5)
T_40: ndarray = np.loadtxt("transition_40.txt", usecols=6)

energy_60 = np.loadtxt("transition_60.txt", usecols=0)
magnet_60 = np.loadtxt("transition_60.txt", usecols=2)
suszep_60 = np.loadtxt("transition_60.txt", usecols=4)
spezhe_60 = np.loadtxt("transition_60.txt", usecols=5)
T_60: ndarray = np.loadtxt("transition_60.txt", usecols=6)

energy_80 = np.loadtxt("transition_80.txt", usecols=0)
magnet_80 = np.loadtxt("transition_80.txt", usecols=2)
suszep_80 = np.loadtxt("transition_80.txt", usecols=4)
spezhe_80 = np.loadtxt("transition_80.txt", usecols=5)
T_80: ndarray = np.loadtxt("transition_80.txt", usecols=6)

energy_100 = np.loadtxt("transition_100.txt", usecols=0)
magnet_100 = np.loadtxt("transition_100.txt", usecols=2)
suszep_100 = np.loadtxt("transition_100.txt", usecols=4)
spezhe_100 = np.loadtxt("transition_100.txt", usecols=5)
T_100: ndarray = np.loadtxt("transition_100.txt", usecols=6)

f, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4)

plot_x = T_40
plot_y_1 = energy_40
plot_y_2 = magnet_40
plot_y_3 = suszep_40
plot_y_4 = spezhe_40

f.suptitle('40x40 Lattice')

ax1.plot(plot_x,plot_y_1, 'ro',plot_x,plot_y_1,'k')
ax1.set_xlabel('Temperature')
ax1.set_ylabel('Energy/Spin')


ax2.plot(plot_x,plot_y_2, 'ro',plot_x,plot_y_2,'k')
ax2.set_xlabel("Temperature")
ax2.set_ylabel("Magnetization/Spin")

ax3.plot(plot_x,plot_y_3, 'ro',plot_x,plot_y_3,'k')
ax3.set_xlabel("Temperature")
ax3.set_ylabel("Suszepzebility")

ax4.plot(plot_x,plot_y_4, 'ro',plot_x,plot_y_4,'k')
ax4.set_xlabel("Temperature")
ax4.set_ylabel("Spezific Heat")

plt.show()

f, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4)

plot_x = T_60
plot_y_1 = energy_60
plot_y_2 = magnet_60
plot_y_3 = suszep_60
plot_y_4 = spezhe_60

f.suptitle("60x60 Lattice")

ax1.plot(plot_x,plot_y_1, 'ro',plot_x,plot_y_1,'k')
ax1.set_xlabel("Temperature")
ax1.set_ylabel("Energy/Spin")


ax2.plot(plot_x,plot_y_2, 'ro',plot_x,plot_y_2,'k')
ax2.set_xlabel("Temperature")
ax2.set_ylabel("Magnetization/Spin")

ax3.plot(plot_x,plot_y_3, 'ro',plot_x,plot_y_3,'k')
ax3.set_xlabel("Temperature")
ax3.set_ylabel("Suszepzebility")

ax4.plot(plot_x,plot_y_4, 'ro',plot_x,plot_y_4,'k')
ax4.set_xlabel("Temperature")
ax4.set_ylabel("Spezific Heat")

plt.show()

f, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4)

plot_x = T_80
plot_y_1 = energy_80
plot_y_2 = magnet_80
plot_y_3 = suszep_80
plot_y_4 = spezhe_80

f.suptitle("80x80 Lattice")

ax1.plot(plot_x,plot_y_1, 'ro',plot_x,plot_y_1,'k')
ax1.set_xlabel("Temperature")
ax1.set_ylabel("Energy/Spin")


ax2.plot(plot_x,plot_y_2, 'ro',plot_x,plot_y_2,'k')
ax2.set_xlabel("Temperature")
ax2.set_ylabel("Magnetization/Spin")

ax3.plot(plot_x,plot_y_3, 'ro',plot_x,plot_y_3,'k')
ax3.set_xlabel("Temperature")
ax3.set_ylabel("Suszepzebility")

ax4.plot(plot_x,plot_y_4, 'ro',plot_x,plot_y_4,'k')
ax4.set_xlabel("Temperature")
ax4.set_ylabel("Spezific Heat")

plt.show()

f, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4)

plot_x = T_100
plot_y_1 = energy_100
plot_y_2 = magnet_100
plot_y_3 = suszep_100
plot_y_4 = spezhe_100

f.suptitle("100x100 Lattice")

ax1.plot(plot_x,plot_y_1, 'ro',plot_x,plot_y_1,'k')
ax1.set_xlabel("Temperature")
ax1.set_ylabel("Energy/Spin")


ax2.plot(plot_x,plot_y_2, 'ro',plot_x,plot_y_2,'k')
ax2.set_xlabel("Temperature")
ax2.set_ylabel("Magnetization/Spin")

ax3.plot(plot_x,plot_y_3, 'ro',plot_x,plot_y_3,'k')
ax3.set_xlabel("Temperature")
ax3.set_ylabel("Suszepzebility")

ax4.plot(plot_x,plot_y_4, 'ro',plot_x,plot_y_4,'k')
ax4.set_xlabel("Temperature")
ax4.set_ylabel("Spezific Heat")

plt.show()