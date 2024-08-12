# Reference: https://ipython-books.github.io/117-creating-a-sound-synthesizer-in-the-notebook/

# import numpy as np
# from IPython.display import Audio

def generate_sine_wave(frequency, duration, sample_rate=44100, amplitude=0.5):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = amplitude * np.sin(2 * np.pi * frequency * t)
    return wave

note_frequencies = {
    'A': 440.00,
    'B': 493.88,
    'C': 261.63,
    'D': 293.66,
    'E': 329.63,
    'F': 349.23,
    'G': 392.00,
    'A#': 466.16,
    'C#': 277.18,
    'D#': 311.13,
    'F#': 369.99,
    'G#': 415.30,
}

def play_chord(notes, duration=1.0, sample_rate=44100):
    chord_wave = np.zeros(int(sample_rate * duration))
    for note in notes:
        freq = note_frequencies[note]
        wave = generate_sine_wave(freq, duration, sample_rate)
        chord_wave += wave
    chord_wave /= len(notes)
    return Audio(chord_wave, rate=sample_rate)

a_minor = ['A', 'C', 'E']

display(play_chord(a_minor))