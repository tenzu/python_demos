import numpy as np
import matplotlib.pyplot as plt


def aggregate_plot():
    filename = 'B' + aggregate_type + '_LOCATIONS.txt'
    file = open(filename, 'r')
    x, y, z, r = [], [], [], []
    for line in file:  # read location information of aggregates
        x.append(float(line[0:11]))
        y.append(float(line[12:23]))
        z.append(float(line[24:35]))
        r.append(float(line[36:47]))

    RD1 = np.linspace(0, 2 * np.pi, 8)
    RD2 = np.linspace(0, np.pi, 8)
    DISK_R = 0.0375e3  # disk radius
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim([-DISK_R, DISK_R])
    ax.set_ylim([-DISK_R, DISK_R])
    ax.set_zlim([-DISK_R, DISK_R])  # for plotting unstreched model
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    for i in range(0, len(x)):
        cx = x[i - 1] + r[i - 1] * np.outer(np.cos(RD1), np.sin(RD2))
        cy = y[i - 1] + r[i - 1] * np.outer(np.sin(RD1), np.sin(RD2))
        cz = z[i - 1] + r[i - 1] * np.outer(np.ones(np.size(RD1)), np.cos(RD2))
        if aggregate_type == 'a' or aggregate_type == 'A':
            ax.plot_surface(cx, cy, cz, color='y')
        elif aggregate_type == 'b' or aggregate_type == 'B':
            ax.plot_surface(cx, cy, cz, color='g')
        elif aggregate_type == 'c' or aggregate_type == 'C':
            ax.plot_surface(cx, cy, cz, color='b')
        elif aggregate_type == 'd' or aggregate_type == 'D':
            ax.plot_surface(cx, cy, cz, color='r')

    plt.show()
    return


while True:
    aggregate_type = input('Please input aggregate type: ')
    if aggregate_type in ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D']:
        aggregate_plot()
    else:
        break
