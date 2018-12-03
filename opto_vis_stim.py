from psychopy import visual, core, event

# Define the background
win=visual.Window([800,600],monitor="testMonitor",units="deg",fullscr=True)

# Number of epochs (repetitions)
EPOCH=15

# Duration of expansion
EXPANSION_MS=250

# Hold duration
HOLD_TIME_MS=250

# ISI duration
ISI_MS=500

# Start radius 

START_RADIUS=1

# Time-to-frame conversion assuming a 60Hz FR and RR
FRAMES=int((60*EXPANSION_MS)/1000)
HOLD_FRAMES=int((60*HOLD_TIME_MS)/1000)
ISI_FRAMES=int((60*ISI_MS)/1000)
print(FRAMES)

# Define the stimulus
circle=visual.Circle(win,radius=START_RADIUS,edges=1000,fillColor='black',lineColor='black')

while EPOCH > 0:
#for e in range(EPOCH):
    for f in range(FRAMES):
        if circle.radius<10:
            circle.radius=(circle.radius+(9/FRAMES))
            circle.draw()
            win.flip()
    for f in range(HOLD_FRAMES):
        circle.radius=10
        circle.draw()
        win.flip()
    for f in range(ISI_FRAMES):
        win.flip()
    print(circle.radius)
    circle.radius=1
    EPOCH -= 1

# Get keys to quit.
if len(event.getKeys())>0:
    event.clearEvents()
    win.close()





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
