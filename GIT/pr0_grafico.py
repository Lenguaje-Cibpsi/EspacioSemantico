# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

# %load http://matplotlib.org/mpl_examples/showcase/integral_demo.py
"""
Plot demonstrating the integral as the area under a curve.

Although this is a simple example, it demonstrates some important tweaks:

    * A simple line plot with custom color and line width.
    * A shaded region created using a Polygon patch.
    * A text label with mathtext rendering.
    * figtext calls to label the x- and y-axes.
    * Use of axis spines to hide the top and right spines.
    * Custom tick placement and labels.
"""
import numpy as np
from math import exp
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def vecexp(x):
    l=x.size
    y=np.zeros(l)
    for i in range(l):
        y[i]=exp(x[i])
    return y


def func(x):
    return (x - 3) * (vecexp(x) - 5) * (x - 7) + 85


        
a, b = 0.2, 1.5 # integral limits
x = np.linspace(0, 1.5)
y = func(x)

fig, ax = plt.subplots()
plt.plot(x, y, 'r', linewidth=2)
plt.ylim(ymin=0)

# Make the shaded region
ix = np.linspace(a, b)
iy = func(ix)
verts = [(a, 0)] + list(zip(ix, iy)) + [(b, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)

plt.text(0.5 * (a + b), y[10], r"$\int_a^b f(x)\mathrm{d}x$",
         horizontalalignment='center', fontsize=20)

plt.figtext(0.9, 0.05, '$x$') #localizar klas etiquetas
plt.figtext(0.1, 0.9, '$y$')

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')

ax.set_xticks((a, b))
ax.set_xticklabels(('$a$', '$b$'))
ax.set_yticks([])

plt.show()