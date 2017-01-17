import numpy as np 
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

#https://jeremykarnowski.wordpress.com/2015/08/07/detection-error-tradeoff-det-curves/

def DETCurve(fps,fns):
    """
    Given false positive and false negative rates, produce a DET Curve.
    The false positive rate is assumed to be increasing while the false
    negative rate is assumed to be decreasing.
    """
    axis_min = min(fps[0],fns[-1])
    fig,ax = plt.subplots()
    plt.plot(fps,fns, label='DET (Detection Error Tradeoff) curve')
    plt.yscale('log')
    plt.xscale('log')
    ticks_to_use = [0.01,0.02,0.05,0.1,0.2,0.5,1,2,5,10,20,50]
    ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    ax.set_xticks(ticks_to_use)
    ax.set_yticks(ticks_to_use)
    plt.axis([0.001,50,0.001,50])
    ax.set_xlim((0.02, 1))
    plt.xlabel('False Positive Rate')
    plt.ylabel('Missed Detection Rate')
    plt.title('DET Curve')
    plt.legend(loc="lower right")
    plt.show()

fps = [0.02, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
fns = [0.8, 0.5, 0.4, 0.2, 0.12, 0.1, 0.05, 0.04, 0.03, 0.02]

DETCurve(fps, fns)