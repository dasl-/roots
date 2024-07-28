# Enumerate every possible Major, Minor, Major 7th and Minor 7th chord 
# and all possible inversions, beginning with A2 and ending with D5.
def enumerate_inversions(chord):
    inversions = [chord]
    inversion = chord
    for note_with_octave in chord:
        if note_with_octave == chord[-1]:
            break
        note = note_with_octave[0]
        octave = int(note_with_octave[1])
        inversion = inversion[1:]
        inversion.append(f'{note}{octave + 1}')
        inversions.append(inversion)
    return inversions

# https://en.wikipedia.org/wiki/Octave#Octave_of_a_pitch
def enumerate_root_position_chords():
    notes = ('C', 'D', 'E', 'F', 'G', 'A', 'B')
    root_position_chords = []
    for root_octave in (2, 3, 4, 5):
        for root_idx in range(len(notes)):
            root = notes[root_idx]
            if root == 'B':
                continue
            if root_octave == 2 and (root != 'A' and root != 'B'):
                continue
            if root_octave == 5 and (root != 'C' and root != 'D'):
                continue

            third_idx = (root_idx + 2) % len(notes)
            third_octave = root_octave
            if third_idx < root_idx:
                third_octave = root_octave + 1

            fifth_idx = (root_idx + 4) % len(notes)
            fifth_octave = root_octave
            if fifth_idx < root_idx:
                fifth_octave = root_octave + 1

            seventh_idx = (root_idx + 6) % len(notes)
            seventh_octave = root_octave
            if seventh_idx < root_idx:
                seventh_octave = root_octave + 1

            triad = [f'{root}{root_octave}', f'{notes[third_idx]}{third_octave}', f'{notes[fifth_idx]}{fifth_octave}']
            seventh = triad + [f'{notes[seventh_idx]}{seventh_octave}']
            root_position_chords += [triad, seventh]

    return root_position_chords

base = {"C": 24, "D": 26, "E": 28, "F": 29, "G": 31, "A": 33, "B": 35}

def note_to_midi(note):
    note, octave = note[0], note[1]
    out = base[note]
    out += int(octave) * 12
    return out


def main():
    root_position_chords = enumerate_root_position_chords()
    print(f"root position chords: {root_position_chords}\n")
    all_chords = []
    for chord in root_position_chords:
        all_chords += enumerate_inversions(chord)
    print(f"all chords: {all_chords}")

    print("int chords[][4] = {")
    for chord in all_chords:
        notes = [str(note_to_midi(note)) for note in chord]
        if len(notes) == 3:
            notes.append("0")
        print("    {" + ",".join(notes) + "},")
    print("}")
    print(len(all_chords))




main()
