#%%
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from matplotlib.patches import Wedge
import numpy as np

#%%

def get_pesapall_field():
    """ Return pesapallo field plot."""
    field_plot = plt.figure(figsize=(3, 5))
    plt.plot([50,29],[96,65],ls = '-',lw = 1,c = "black")   
    plt.plot([50,71],[96,65],ls = '-',lw = 1,c = "black")   

    plt.plot([29,29],[65,10],ls = '-',lw = 1,c = "black")
    plt.plot([71,71],[65,10],ls = '-',lw = 1,c = "black")
    plt.plot([29,71],[10,10],ls = '-',lw = 1,c = "black")

    plt.plot([31.5,68],[58.5,58.5],ls = '-',lw = 1,c = "black") # From 2 to 3
    plt.plot([61.22,31.5],[79.42,60],ls = '-',lw = 1,c = "black") # From 1 to 2

    #plt.scatter([50,29,71,29,71],[96,65,65,10,10],c = "black", lw = 1)

    a = 3 # diameter
    b = 3
    x_0 = 58.5
    y_0 = 29
    x = np.linspace(-a + x_0, a + x_0)
    y = b * np.sqrt(1 - ((x - x_0) / a) ** 2) + y_0
    plt.plot(y, x, c = "black")

    a = 3 # diameter
    b = 3
    x_0 = 58.5
    y_0 = 71
    x = np.linspace(-a + x_0, a + x_0)
    y = - b * np.sqrt(1 - ((x - x_0) / a) ** 2) + y_0
    plt.plot(y, x, c = "black")


    # the points to be plotted
    x = 0
    y = 0
    # radius of the wedge
    radius = 15
    # start angle of the wedge
    start_angle = 1
    # end angle of the wedge
    end_angle = 2
    # plotting the graph
    Wedge((2, 2), 1, 3, 4)
    return(field_plot)

