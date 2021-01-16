import time
from amidiw import MIDIInterface

# set midi cc code
CC_EXPRESSION = 11

# create midi interface
midi = MIDIInterface()

# wipe right
for i in range(128):
    print(i)
    midi.send_cc_message(CC_EXPRESSION, 1, i)
    time.sleep(0.001)

# wipe back left
for i in range(128):
    ii = 127 - i
    print(ii)
    midi.send_cc_message(CC_EXPRESSION, 1, ii)
    time.sleep(0.001)