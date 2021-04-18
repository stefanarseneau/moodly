import progression_producer
import synth

vibe = 'ihop commercial'  # raw_input("Pick a vibe\n")
# print ("You picked: " + vibe)
mood = 'onyx'  # raw_input("Pick a mood\n")
spice = 'chili powder'  # raw_input("Pick a spice\n")

output = progression_producer.Progression(vibe, mood, spice)
print output

octave = 4
duration = 4
synthChord = None

for chord in output.chordSequence:
    synthNotesList = []
    for note in chord.notes:
        noteName = note.noteName
        synthNote = synth.Note(noteName, octave, duration)
        synthNotesList.append(synthNote)
    synthChord = synthChord + synth.Chord([synthNotesList])

