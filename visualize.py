def visualize(netErr):
    import matplotlib.pyplot as plt
    from mpl_toolkits import mplot3d
    
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    xdat = [netErr[i][0] for i in range(len(netErr))]
    ydat = [netErr[i][1] for i in range(len(netErr))]
    zdat = [netErr[i][2] for i in range(len(netErr))]
    
    ax.scatter3D(xdat, ydat, xdat)
    plt.show()
