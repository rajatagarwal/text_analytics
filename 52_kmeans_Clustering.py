#Taken from https://datasciencelab.wordpress.com/2013/12/12/clustering-with-k-means-in-python/
# Just added plotting for 3-k cases

import numpy as np
import random
import matplotlib.pyplot as plt

def init_board(N):
    X = np.array([(random.uniform(-1, 1), random.uniform(-1, 1)) for i in range(N)])
    return X

def cluster_points(X, mu):
    clusters  = {}
    for x in X:
        bestmukey = min([(i[0], np.linalg.norm(x-mu[i[0]])) \
                    for i in enumerate(mu)], key=lambda t:t[1])[0]
        try:
            clusters[bestmukey].append(x)
        except KeyError:
            clusters[bestmukey] = [x]
    return clusters

def reevaluate_centers(mu, clusters):
    newmu = []
    keys = sorted(clusters.keys())
    for k in keys:
        newmu.append(np.mean(clusters[k], axis = 0))
    return newmu

def has_converged(mu, oldmu):
    return (set([tuple(a) for a in mu]) == set([tuple(a) for a in oldmu]))

def find_centers(X, K):
    # Initialize to K random centers
    oldmu = random.sample(X, K)
    mu = random.sample(X, K)
    while not has_converged(mu, oldmu):
        oldmu = mu
        # Assign all points in X to clusters
        clusters = cluster_points(X, mu)
        # Reevaluate centers
        mu = reevaluate_centers(oldmu, clusters)
    return(mu, clusters)

def change_coords(array):
    return list(map(list, zip(*array)))

def parse_output(data):
    clusters = data[1]
    points1 = change_coords(clusters[0])
    plt.plot(points1[0], points1[1], 'ro')
    points2 = change_coords(clusters[1])
    plt.plot(points2[0], points2[1], 'g^')
    points3 = change_coords(clusters[2])
    plt.plot(points3[0], points3[1], 'ys')
    centroids = change_coords(data[0])
    plt.plot(centroids[0], centroids[1], 'kx')
    plt.axis([-1.0, 1, -1.0, 1])
    plt.show()

data = init_board(15)


data = np.array([[0.5,0.5],[0.6,0.6],[-0.5,-0.5], [-0.6,-0.6],[0.124,0.124], [0.135,0.135]])
#data = np.array([ [0.5,0.5],[0.6,0.6],[-0.5,-0.5], [-0.6,-0.6],[0.124,0.124], [0.135,0.135], [0.1, 0.1],
#    [-0.821, -0.821],[0.420,0.420], [0.230, 0.230], [-0.542,-0.542], [0.634,0.634], [-0.992,-0.992], 
#    [0.012,0.012], [-0.643,-0.643]])

data = np.array([[ -4.15438952e-01,   6.26913307e-01], [  9.54709897e-01,   1.10718367e-01],
    [  3.31959387e-01,  -7.57119499e-01], [  3.22947232e-01,  -9.20454993e-01], [ -4.07015169e-01,   3.37221092e-01],
 [  3.36825288e-01,   4.47151951e-01], [ -7.96256335e-01,   4.82305137e-01], [ -3.79401101e-01,   6.53849222e-01],
 [  7.39554956e-01,  -2.09416327e-01], [ -8.92701206e-02,   6.60700742e-02], [ -9.29120804e-01,   2.85630759e-01],
 [  5.37031039e-01,   9.54568654e-02], [  2.57568681e-04,  -5.85311206e-01], [ -7.77886677e-01,   6.66566489e-01],
 [  7.55295395e-01,   7.95911922e-01]])

print(data)
print(type(data))
out = find_centers(list(data), 3)
parse_output(out)