    plt.subplot(413)
    y = distance.__gt__(12)
    plt.plot(y, 'y-', linewidth=2, label='filtered data')
    plt.title('output norm abs')