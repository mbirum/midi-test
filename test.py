import time
import rtmidi
from amidiw import MIDIInterface

# set midi cc code
CC_EXPRESSION = 11

INTERVAL = 0.01

# create midi interface
#midi = MIDIInterface()

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()

print(available_ports)

midiout.open_port(0)

for i in range(15):
    print(i)
    midiout.send_message([0x1, 11, i])
    time.sleep(INTERVAL)

for i in range(15):
    ii = 14 - i
    print(ii)
    midiout.send_message([0x1, 11, i])
    time.sleep(INTERVAL)

# wipe right
#for i in range(15):
    #print(i)
    #midi.send_cc_message(CC_EXPRESSION, 1, i)

# wipe back left
#for i in range(15):
    #ii = 14 - i
    #print(ii)
    #midi.send_cc_message(CC_EXPRESSION, 1, ii)