# -*- coding: utf8

from sklearn.cluster import MeanShift, estimate_bandwidth
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import kde

stars = np.loadtxt("output/stars-0.txt")

x = []
y = []
for i in range(0, len(stars)) :

    # 0 x
    # 1 y
    # 2 red
    # 3 blue
    # 4 green
    # 5 green2

    indice = stars[i][3] - stars[i][4] # blue - green

    x.append(indice)
    y.append(stars[i][4] + 15)


# Evaluate a gaussian kde on a regular grid of nbins x nbins
# over data extents
x = np.array(x)
y = np.array(y)

X = []
for i in range(0, len(x)) :
    X.append( [x[i],y[i]] )
X = np.array(X)

# Diagramme HR
nbins=400
k = kde.gaussian_kde([x,y])
xi, yi = np.mgrid[x.min():x.max():nbins*1j, y.min():y.max():nbins*1j]
zi = k(np.vstack([xi.flatten(), yi.flatten()]))
plt.pcolormesh(xi, yi, zi.reshape(xi.shape), cmap="binary" )
plt.savefig('output/hr0-density.png')

plt.scatter(x, y, alpha=0.5)
plt.savefig('output/hr0-dots.png')

# Algorithme pour trouver les centres des clusters parmi les points
bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=500)
ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
ms.fit(X)
labels = ms.labels_
cluster_centers = ms.cluster_centers_
labels_unique = np.unique(labels)
n_clusters_ = len(labels_unique)

print("number of estimated clusters : %d" % n_clusters_)
for cluster in cluster_centers :
    print(cluster)
