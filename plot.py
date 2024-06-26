
import numpy

import matplotlib.pyplot as plt

xdata = numpy.load("xdata.npy")
ydata = numpy.load("ydata.npy")


x_data = numpy.ravel(xdata[:50,:,0])

fig = plt.figure(figsize=(25,9),dpi=150)

ax = fig.add_subplot(1,1,1)
ax.plot(numpy.arange(len(x_data)),x_data)

plt.show()
