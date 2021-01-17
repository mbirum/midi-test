import time
import rtmidi

CHANNEL = 0xB0
CC_EXPRESSION = 11

INTERVAL = 0.1

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
    midiout.send_message([CHANNEL, CC_EXPRESSION, i])
    time.sleep(INTERVAL)

for i in range(60):
    ii = 59 - i
    print(ii)
    midiout.send_message([CHANNEL, CC_EXPRESSION, ii])
    time.sleep(INTERVAL)
