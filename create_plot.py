
# importing required libraries
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.animation as animation
from pathlib import Path
import sys

slope = float(sys.argv[1])
intercept = float(sys.argv[2])

dir = Path(__file__).parent.resolve()
ffmpegPath = dir.joinpath('ffmpeg')

plt.rcParams['animation.ffmpeg_path'] = ffmpegPath

# initializing a figure
fig = plt.figure()

# labeling the x-axis and y-axis
axis = plt.axes(xlim=(0, 1000),  ylim=(0, 1000))

# lists storing x and y values
x, y = [], []

line, = axis.plot(0, 0)


def animate(frame_number):
    x.append(frame_number)
    y.append(frame_number*slope + intercept)
    line.set_xdata(x)
    line.set_ydata(y)
    return line,


anim = animation.FuncAnimation(fig, animate, frames=1000,
                               interval=20, blit=True)
fig.suptitle('Straight Line plot', fontsize=14)

name = 'increasingStraightLine_m=%f_b=%f' % (slope, intercept)
filepath = 'static/%s.mp4' % name
# saving to m4 using ffmpeg writer
writervideo = animation.FFMpegWriter(fps=60)
anim.save(filepath, writer=writervideo)
plt.close()
print('created %s' % name)
