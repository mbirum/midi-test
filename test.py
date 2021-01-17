import time
import rtmidi
from amidiw import MIDIInterface

# set midi cc code
CC_EXPRESSION = 0xB0

INTERVAL = 0.1

# create midi interface
#midi = MIDIInterface()

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()
port_index = -1


for i in range(len(available_ports)):
    if "rtpmidi" in available_ports[i]:
        print(available_ports[i])
        port_index = i

if port_index == -1:
    raise Exception('rtpmidi port not available')

midiout.open_port(port_index)

for i in range(60):
    print(i)
    midiout.send_message([CC_EXPRESSION, 1, i])
    time.sleep(INTERVAL)

for i in range(60):
    ii = 59 - i
    print(ii)
    midiout.send_message([CC_EXPRESSION, 1, ii])
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