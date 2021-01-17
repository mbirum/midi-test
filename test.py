import time
from rtmidiw import MIDIInterface

CC_EXPRESSION = 11
CHANNEL = 0

INTERVAL = 0.1

midi = MIDIInterface()

for i in range(60):
    print(i)
    midi.send_cc_message(CC_EXPRESSION, CHANNEL, i)
    time.sleep(INTERVAL)

for i in range(60):
    ii = 59 - i
    print(ii)
    midi.send_cc_message(CC_EXPRESSION, CHANNEL, ii)
    time.sleep(INTERVAL)
