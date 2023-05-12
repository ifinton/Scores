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

A4 = 319.5
C0 = A4 * pow(2, -4.75)
name = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
def pitch(freq):
    h = round(12 * log2(freq / C0))
    octave = h // 12
    n = h % 12
    return name[n] + str(octave)


######################################
##https://stackoverflow.com/questions/6487180/synthesize-musical-notes-with-piano-sounds-in-python
A4_TUNING=319.50
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


#SOLFEGGIO-TABLE-OF-STARTING-PITCHES-TO-PIANO-KEYS
import pandas
hz319 = pandas.read_csv('voice/List-of-Pitches/319.50(639)-List-of-88-Pitches.txt',delimiter=' ',index_col=1,header=None,)[3]
hz319.index.name='PianoKey'
hz319.name='319.50(639)'
#print(hz319.info)

hz344 = pandas.read_csv('voice/List-of-Pitches/344.00(172)-List-of-88-Pitches.txt',delimiter=' ',index_col=1,header=None,)[3]
hz344.index.name='PianoKey'
hz344.name='344.00(172)'
#print(hz344.info)

hz370 = pandas.read_csv('voice/List-of-Pitches/370.50(741)-List-of-88-Pitches.txt',delimiter=' ',index_col=1,header=None,)[3]
hz370.index.name='PianoKey'
hz370.name='370.50(741)'
#print(hz370.info)

hz396 = pandas.read_csv('voice/List-of-Pitches/396.00(396)-List-of-88-Pitches.txt',delimiter=' ',index_col=1,header=None,)[3]
hz396.index.name='PianoKey'
hz396.name='396.00(396)'
#print(hz396.info)

hz417 = pandas.read_csv('voice/List-of-Pitches/417.00(417)-List-of-88-Pitches.txt',delimiter=' ',index_col=1,header=None,)[3]
hz417.index.name='PianoKey'
hz417.name='417.00(417)'
#print(hz417.info)

hz426 = pandas.read_csv('voice/List-of-Pitches/426.00(852)-List-of-88-Pitches.txt',delimiter=' ',index_col=1,header=None,)[3]
hz426.index.name='PianoKey'
hz426.name='426.00(852)'
#print(hz426.info)

hz468 = pandas.read_csv('voice/List-of-Pitches/468.00(936)-List-of-88-Pitches.txt',delimiter=' ',index_col=1,header=None,)[3]
hz468.index.name='PianoKey'
hz468.name='468.00(936)'
#print(hz468.info)

hz528 = pandas.read_csv('voice/List-of-Pitches/528.00(528)-List-of-88-Pitches.txt',delimiter=' ',index_col=1,header=None,)[3]
hz528.index.name='PianoKey'
hz528.name='528.00(528)'
#print(hz528.info)

hz570 = pandas.read_csv('voice/List-of-Pitches/570.00(285)-List-of-88-Pitches.txt',delimiter=' ',index_col=1,header=None,)[3]
hz570.index.name='PianoKey'
hz570.name='570.00(285)'
#print(hz285.info)

hzAll = pandas.concat([hz319, hz344, hz370, hz396, hz417, hz426, hz468, hz528, hz570], axis=1)
hzAll.to_csv('voice/List-of-Pitches/List-of-Pitches-TABLE.csv')

print(hzAll)