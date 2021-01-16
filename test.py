import time
from amidiw import MIDIInterface

# set midi cc code
CC_EXPRESSION = 11

INTERVAL = 0.0001

# create midi interface
midi = MIDIInterface()

# wipe right
for i in range(128):
    print(i)
    midi.send_cc_message(CC_EXPRESSION, 1, i)
    #time.sleep(INTERVAL)

# wipe back left
for i in range(128):
    ii = 127 - i
    print(ii)
    midi.send_cc_message(CC_EXPRESSION, 1, ii)
    #time.sleep(INTERVAL)
