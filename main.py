HZ_MAX_KEY_108=4186.009
SOLFEGGIOS=[174,285,396,417,528,639,741,852,936]
SOLFEGGIOS_VOICEORDER=[639,172,741,396,417,852,936,528,285]
SOLFEGGIOS_VOICEORDER_TUNING=[319.5,344,370.5,396,417,426,468,528,570]

ABSOLUTE_TONES = []
ABSOLUTE_TONES_MASTER = []
"TEST BY SWAPPING WITH 'SOLFEGGIOS'"
ABSOLUTE_OCTAVES = []
def toneGenerator():
    for index in SOLFEGGIOS:
        TONE = index
        "DETERMINE TONES ABOVE SOLFEGGIO"
        while TONE < HZ_MAX_KEY_108:
            ABSOLUTE_TONES.append(TONE)
            ABSOLUTE_TONES.sort()
            TONE = TONE * 2

        'DETERMINE TONES BELOW SOLFEGGIO'
        TONE = index
        while TONE > 0:
            if TONE%2 == 0:
                TONE = int(TONE/2)
                ABSOLUTE_TONES.append(TONE)
                ABSOLUTE_TONES.sort()
            if TONE%2 > 0:
                'SET TONE TO 0 TO BREAK LOOP IMMEDIATELY'
                TONE = 0
        print("-------------------------------------")
        print(str(index) + ':')
        print(ABSOLUTE_TONES)
        print("-------------------------------------")
        ABSOLUTE_TONES_MASTER.extend(ABSOLUTE_TONES)
        ABSOLUTE_TONES_MASTER.sort()
        #print(ABSOLUTE_TONES_MASTER)
        del ABSOLUTE_TONES[:]
    print(ABSOLUTE_TONES_MASTER)
    print(len(ABSOLUTE_TONES_MASTER))
#toneGenerator()
################################################
##SOURCE: https://www.johndcook.com/blog/2016/02/10/musical-pitch-notation/
from math import log2, pow

A4 = 440
C0 = A4 * pow(2, -4.75)
name = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
def pitch(freq):
    h = round(12 * log2(freq / C0))
    octave = h // 12
    n = h % 12
    return name[n] + str(octave)


######################################
##https://stackoverflow.com/questions/6487180/synthesize-musical-notes-with-piano-sounds-in-python
A4_TUNING=444
A4_NOTE_NUMBER=69
semiToneIncrement=3
print(pitch(A4_TUNING*(pow(pow(2,1/12),semiToneIncrement))))
print(A4_TUNING*(pow(pow(2,1/12),semiToneIncrement)))
print(semiToneIncrement+A4_NOTE_NUMBER)
################################################

####https://en.wikipedia.org/wiki/Piano_key_frequencies
for frequency in SOLFEGGIOS:
    print('SOLFEGGIOS as NOTES')
    print(str(pitch(frequency))+':'+ str(frequency))

for frequency in SOLFEGGIOS_VOICEORDER:
    print('SOLFEGGIO VoiceOrder as NOTES')
    print(str(pitch(frequency))+':'+ str(frequency))

for frequency in SOLFEGGIOS_VOICEORDER_TUNING:
    print('SOLFEGGIO TUNING ORDER:')
    print(str(pitch(frequency))+':'+ str(frequency))
#174 is A=348 -1 Octave
#285 is A=570 -1 Octave
