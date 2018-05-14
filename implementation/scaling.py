import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns


plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.preamble'] = [r'\usepackage{lmodern}']

colors = ["#d7191c", "#2b83ba", "#abdda4"]
labels = [r"$\beta=6.00,24^3\times 48$", r"$\beta=6.10, 28^3\times 56$", r"$\beta=6.20,32^3\times 64$", r"$\beta=6.45,48^3\times 96$"]
sns.set(style="whitegrid", font_scale=1.1, font="Times New Roman")


plt.figure(figsize=(8,4.5))
gen = np.loadtxt("genStrong.dat")
flow = np.loadtxt("flowStrong.dat")

genData = (gen[0,1]/gen[:,0]*64) / gen[:,1] * 100     #gen[0,1]/gen[:,1]
flowData= (flow[0,1]/flow[:,0]*64) / flow[:,1] * 100 

#plt.xlim([0,15])
plt.ylim([0,150])
plt.xscale('log', basex=2)
plt.xlabel(r"Number of Processors")
plt.ylabel(r"Strong Scaling Efficiency $\eta_S$")
plt.plot(gen[:,0], genData, "o-", color=colors[0], label="Gauge Generation")
plt.plot(flow[:,0], flowData, "o-", color=colors[1], label="Gradient Flow")
plt.title("Strong Scaling")
plt.legend()
plt.savefig("StrongScaling.pdf")
plt.show()


plt.figure(figsize=(8,4.5))
gen = np.loadtxt("genWeak.dat")
flow = np.loadtxt("flowWeak.dat")

genData = (gen[0,1]/gen[:,1]) * 100 
flowData= (flow[0,1]/flow[:,1]) * 100 
print flowData, flow[0,1]

#plt.xlim([0,15])
plt.ylim([0,150])
plt.xscale('log', basex=2)
plt.xlabel(r"Number of Processors")
plt.ylabel(r"Weak Scaling Efficiency $\eta_W$")
plt.plot(gen[:,0], genData, "o-", color=colors[0], label="Gauge Generation")
plt.plot(flow[:,0], flowData, "o-", color=colors[1], label="Gradient Flow")
plt.title("Weak Scaling")
plt.legend()
plt.savefig("WeakScaling.pdf")
plt.show()
