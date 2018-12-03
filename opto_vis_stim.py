from __future__ import division, print_function
import os
import sys
import numpy as np
from psychopy import visual, logging
import psychopy



NUM_FRAMES = 15
NUM_TRIALS = 15
HOLD_FRAMES = 15
ISI_FRAMES = 30

# Most arguments are just defaults made explicit in case they are relevant in future.

win=psychopy.visual.Window(size=(800, 600),
     pos=None,
     color=(0, 0, 0),
     colorSpace='rgb',
     rgb=None,
     dkl=None,
     lms=None,
     fullscr=None, 
     allowGUI=None,
     monitor=None,
     bitsMode=None,
     winType=None,
     units=None,
     gamma=None,
     blendMode='avg',
     screen=1,
     viewScale=None,
     viewPos=None,
     viewOri=0.0,
     waitBlanking=True,
     allowStencil=False,
     multiSample=False,
     numSamples=2,
     stereo=False,
     name='window1',
     checkTiming=True,
     useFBO=False,
     useRetina=True,
     autoLog=True,
     #*args,
     #**kwargs
)
'''
# For recording dropped frames

win.recordFrameIntervals=True

# By default, the threshold is set to 120% of the estimated refresh
# duration, but arbitrary values can be set.
#
# I've got 85Hz monitor and want to allow 4 ms tolerance; any refresh that
# takes longer than the specified period will be considered a "dropped"
# frame and increase the count of win.nDroppedFrames.
win.refreshThreshold = 1/85 + 0.004

# Set the log module to report warnings to the standard output window
# (default is errors only).
logging.console.setLevel(logging.WARNING)

print('Overall, %i frames were dropped.' % win.nDroppedFrames)
'''

circle=psychopy.visual.Circle(win=win,
    units='deg', # units in degress of visual angle - parameters set in Monitor Settings.
    lineWidth=1.5,
    lineColor='black',
    lineColorSpace='rgb',
    fillColor='black',
    fillColorSpace='rgb',
    vertices=((-0.5, 0), (0, 0.5), (0.5, 0)),
    #windingRule=None,
    closeShape=True,
    pos=(0, 0),
    size=2,
    ori=0.0,
    opacity=1.0,
    contrast=1.0,
    depth=0,
    interpolate=True,
    name=None,
    autoLog=None,
    autoDraw=False
)

# loop through NUM_TRIALS then loop through frames of NUM_FRAMES for stimulus
#

while NUM_TRIALS > 0:
    for frames in range(NUM_FRAMES):
        circle.draw()
        win.flip()
        for frames in ISI_FRAMES:
            win.flip()
        circle.size += 1
        NUM_TRIALS -= 1


while NUM_TRIALS > 0 and circle.size <= 20:
    for f in NUM_TRIALS:
        circle.draw()
        win.flip()
        circle.size+=1











