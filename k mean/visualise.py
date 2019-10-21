import pandas as pd
import matplotlib.pyplot as plt

def visualise(*args):
    data = []
    for ar in args:
        data.append((ar.x,ar.y))
    data = tuple(data)


    colors = ("red", "green", "blue")
    groups = ("C1", "C2", "C3")


    for data, color, group in zip(data, colors, groups):
        x, y = data

        plt.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)

    plt.title('Matplot scatter plot')
    plt.legend(loc=2)
    plt.show()