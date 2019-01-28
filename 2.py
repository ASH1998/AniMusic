from mido import MidiFile

mid = MidiFile('Accel World - Bye Bye.mid')
print(mid)
for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        print(msg)
