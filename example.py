from midiutil import MIDIFile
from Musicify import Musicify
from pidigits import piGenerator
from collections import deque

# Instantiate pidigits
pi = piGenerator()

# Any sequence of integers without decimals
number = "3141592653"

# This set changes the duration of the notes
other = "2526477538"

# Convert sequence to list
e = list(number)
f = []
for digits in e:
    f.append(int(digits))

# Convert note durations to list
d = list(other)
da = []
for other in d:
    da.append(int(other))

# Initialize pi queue
test = deque([next(pi) for j in range(0, len(f))])
i = len(test)

# Compare sequence against pi
length = len(test)
# Output the final amount of digits and sequence found in pi
#print(i-len(f))
#print(test)

SharpOrFlat = 0
mode = 0
octave = 0

# Instantiate musicify
music = Musicify(f, SharpOrFlat, mode, octave)

# Set key
music.to_key_extension("C")

# Get mapping
c = music.notes
print(c)

# Set MIDI Parameters
degrees = c
track    = 0
channel  = 0
time     = 0    # In beats
duration = 0    # In beats
tempo    = 60   # In BPM
volume   = 80  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
MyMIDI.addTempo(track, time, tempo)

for i, pitch in enumerate(degrees):
    duration = (da[i]+1)/4
    if i == 0:
        MyMIDI.addNote(track, channel, pitch, time, duration, volume)
    else:
        time = time + (da[i-1]+1)/4
        MyMIDI.addNote(track, channel, pitch, time, duration, volume)

# Output MIDI files
with open("test.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
