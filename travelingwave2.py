'''
GOAL:
* show animation of traveling wave and history graph


REFERENCES:
* https://matplotlib.org/3.1.1/api/animation_api.html
* https://towardsdatascience.com/how-to-create-animated-graphs-in-python-bb619cc2dec1

WHITEBOARD PROBLEM 16.1
'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib

#matplotlib.use('TkAgg')
# make a triangular pulse
pulse_y = np.array([0,2,0,-2,0])

# define the velocity - this doesn't do anything yet
pulse_v = 1

# create a figure with two subplots
fig1, (ax1, ax2) = plt.subplots(2,1,figsize=(8,6))
plt.style.use("ggplot")
fig1.subplots_adjust(hspace=.5)
# intialize two line objects (one in each axes)
line1, = ax1.plot([], [], lw=2,color='b')
line2, = ax1.plot([], [], 'ro',lw=2,markersize=12)
title1 = ax1.set_title('test')
line3, = ax2.plot([], [], lw=2, color='r')
myline = [line1, line2, line3]

ax2.set_title('history graph for x=5m')
ax2.set_xlabel('time (s)')
ax2.set_ylabel('y (m)')
ax1.set_xlabel('x (m)')
ax1.set_ylabel('y (m)')
# add grid lines
# the same axes initalizations as before (just now we do it for both of them)
for ax in [ax1, ax2]:
    ax.set_ylim(-2.5, 2.5)
    ax.set_xlim(-.2, 10)
    ax.grid()

t = []
timedot=[]
ydot=[]
def animate(frame):
    x=np.arange(10)
    y=np.zeros(10)
    # pulse position steps to the right with each frame
    endpoint=frame+len(pulse_y)

    # check to see if pulse extends beyond from
    # if it does, but it off at the end of the frame
    if endpoint > (len(y)):
        
        endpoint = len(y)
        npoints_pulse = endpoint - frame
        if npoints_pulse >0:
            y[frame:endpoint]=pulse_y[0:npoints_pulse]
    else:
        y[frame:endpoint]=pulse_y
    
    # update position of pulse
    myline[0].set_data(x,y)

    # show position of reference dot on traveling wave
    dotlocation = 5
    myline[1].set_data(x[dotlocation],y[dotlocation])
    
    # show history graph of the specified location
    timedot.append(frame)
    ydot.append(y[dotlocation])
    myline[2].set_data(timedot,ydot)
    
    ax1.set_title('snapshot graph: t = {} sec'.format(frame))
    ax1.set_facecolor('0.8')
    ax2.set_facecolor('0.8')    
    ax1.grid(True,c='w')
    ax2.grid(True,c='w')    
    return myline
    
# this runs the animation
ani = animation.FuncAnimation(fig1, animate, interval=1000,frames=11,repeat=False)
plt.show()

#writervideo = animation.FFMpegWriter(fps=60)
#matplotlib.rcParams['animation.ffmpeg_path'] = '/usr/bin/ffmpeg' 
#ani.save('travelingwave-historygraph.gif')


