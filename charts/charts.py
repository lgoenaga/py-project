import matplotlib.pyplot as plt
import numpy as np

def generate_pie_chart():
    labels = ['A', 'B', 'C', 'D']
    values = [15, 30, 45, 10]

    fig1, ax1 = plt.subplots()
    ax1.pie(values, labels=labels)
    plt.savefig('pie_chart.png')
    plt.close()