### Audio stim info
The stimuli order text file includes the exact order in which the audio stimuli will be presented.

There are 4 different "nonsense" words that are made up of three syllables each... and each syllable is identified by a specific number. These numbers are what appear in the stimuli order text file.

# pautone (12, 7, 9)
12 = wave.open('audio_stim/pau.wav', 'r')
7 = wave.open('audio_stim/to.wav', 'r')
9 = wave.open('audio_stim/ne.wav', 'r')
# nurafi (11, 1, 8)
11 = wave.open('audio_stim/nu.wav', 'r')
1 = wave.open('audio_stim/ra.wav', 'r')
8 = wave.open('audio_stim/fi.wav', 'r')
# mailoki (5, 4, 2)
5 = wave.open('audio_stim/mai.wav', 'r')
4 = wave.open('audio_stim/lo.wav', 'r')
2 = wave.open('audio_stim/ki.wav', 'r')
# gabalu (10, 3, 6)
10 = wave.open('audio_stim/ga.wav', 'r')
3 = wave.open('audio_stim/ba.wav', 'r')
6 = wave.open('audio_stim/lu.wav', 'r')

In the experiment, we want the FIRST syllable in each nonsense word to start at the exact time the dot crosses the fixation point. This way, it will be in phase with the visual stimuli. We can't just play all the audio, we have to ensure that every 3rd syllable aligns with the dot frequency and if it is too early - it needs to wait for that moment.
