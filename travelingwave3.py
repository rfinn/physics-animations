'''
GOAL:
* show animation of traveling wave and history graph


REFERENCES:
* https://matplotlib.org/3.1.1/api/animation_api.html
* https://towardsdatascience.com/how-to-create-animated-graphs-in-python-bb619cc2dec1

WHITEBOARD PROBLEM 16.3
'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib

#matplotlib.use('TkAgg')
# make a triangular pulse

# define the velocity - this doesn't do anything yet
pulse_v = 1

# create a figure with two subplots
fig1, (ax1, ax2) = plt.subplots(2,1,figsize=(8,6))
plt.style.use("ggplot")
fig1.subplots_adjust(hspace=.5)
# intialize two line objects (one in each axes)
refpoint = 6 # x position of reference point
line1, = ax1.plot([], [], lw=2,color='b')
line2, = ax1.plot([], [], 'ro',lw=2,markersize=12)
title1 = ax1.set_title('test')
line3, = ax2.plot([], [], lw=2, color='r')
myline = [line1, line2, line3]


ax2.set_xlabel('time (s)')
ax2.set_ylabel('y (m)')
ax1.set_xlabel('x (m)')
ax1.set_ylabel('y (m)')
# add grid lines
# the same axes initalizations as before (just now we do it for both of them)
for ax in [ax1, ax2]:
    ax.set_ylim(-.1,.1)
    ax.set_xlim(-.2, 6)
    ax.grid()
ax2.set_xlim(-.01,.25)
t = []
timedot=[]
ydot=[]
def animate(frame):
    # frame represents time step in half sections seconds
    timescale = 0.005 # how many seconds per frame
    t = frame*timescale
    
    # wave characteristics
    A=.05 # m
    k = 1.5 #rad/m
    v = 100 #m/s
    omega = 150 #rad/s
    phi = np.pi/2 # phase of wave

    x = np.linspace(0,6,100)
    y = A*np.sin(k*x-omega*t+phi)

    ## derived properties
    wavelength = 2*np.pi/k
    
    # update position of pulse
    myline[0].set_data(x,y)

    # show position of reference dot on traveling wave
    dotlocation = np.arange(len(x))[int(len(x)/2)] # show history graph for x=6 m
    myline[1].set_data(x[dotlocation],y[dotlocation])
    
    # show history graph of the specified location
    timedot.append(t)
    ydot.append(y[dotlocation])
    myline[2].set_data(timedot,ydot)
    
    ax1.set_title('snapshot graph: t = {:.3f} sec'.format(t))
    ax2.set_title('history graph for x={:.1f}m'.format(x[dotlocation]))    
    ax1.set_facecolor('0.8')
    ax2.set_facecolor('0.8')    
    ax1.grid(True,c='w')
    ax2.grid(True,c='w')    
    return myline
    
# this runs the animation
ani = animation.FuncAnimation(fig1, animate, interval=200,frames=51,repeat=False)
plt.show()

#writervideo = animation.FFMpegWriter(fps=60)
#matplotlib.rcParams['animation.ffmpeg_path'] = '/usr/bin/ffmpeg' 
#ani.save('travelingwave-historygraph.gif')


