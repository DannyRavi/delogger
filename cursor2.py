import matplotlib.pyplot as plt
aa = []
def on_pick(event):
    artist = event.artist
    xmouse, ymouse = event.mouseevent.xdata, event.mouseevent.ydata
    x, y = artist.get_xdata(), artist.get_ydata()
    ind = event.ind
    #print 'Artist picked:', event.artist
    #print '{} vertices picked'.format(len(ind))
    #print 'Pick between vertices {} and {}'.format(min(ind), max(ind)+1)
    print 'x, y of mouse: {:.2f},{:.2f}'.format(xmouse, ymouse)
    # print 'Data point:', x[ind[0]], y[ind[0]]
    aa.append(x[ind[0]])
    return aa

fig, ax = plt.subplots()

tolerance = 10 # points
ax.plot(range(10), 'ro-', picker=tolerance)

xx = fig.canvas.callbacks.connect('pick_event', on_pick)

plt.show()
plt.close()

aa =[]

fig, ax = plt.subplots()
ax.plot(range(20), 'y', picker=tolerance)

xx = fig.canvas.callbacks.connect('pick_event', on_pick)

plt.show()
plt.close()
print("==>", aa)