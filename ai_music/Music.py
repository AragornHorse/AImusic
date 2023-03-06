import mido

idx2time = [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.5, 3, 4]
time2idx = {}
for i, time in enumerate(idx2time):
    time2idx[time] = i

def nb2num(note, base_num):
    return 7 * (base_num + 1) + note - 1

def time2t(time):
    try:
        return time2idx[time]
    except:
        return 0

mid = mido.MidiFile()
track = mido.MidiTrack()
mid.tracks.append(track)

data = []


# bpm = \frac{60000000}{tempo}
def music(note ,base_num ,base_time):

    num = nb2num(note, base_num)
    t = time2t(base_time)
    if num >= 21 or num < 0:
        return None
    data.append([num, t])

    # meta_time = 60 * 60 * 10 / bpm
    major_notes = [0, 2, 2, 1, 2, 2, 2, 1]
    base_note = 60
    track.append(mido.Message('note_on', note=base_note +base_num *12 + sum(major_notes[0:note]), velocity=96, time=0
                              ,channel=1))
    track.append(mido.Message('note_off', note=base_note +base_num *12 + sum(major_notes[0:note]), velocity=96, time=int(480 *base_time) ,channel=1))
    # track.append(mido.Message('note_on', note=base_note, velocity=96, time=0))
    # track.append(mido.Message('note_off', note=base_note, velocity=96, time=480*base_time))

def lemon_music():
    # 1
    music(1 ,1 ,0.5)
    music(2 ,1 ,0.5)   # a-1+7(b+1)

    music(3 ,1 ,1)
    music(1 ,1 ,0.5)
    music(6 ,0 ,1.5)
    music(2 ,1 ,1)

    music(7 ,0 ,1)
    music(5 ,0 ,0.5)
    music(3 ,0 ,1.5)
    music(7 ,0 ,1)

    music(6 ,0 ,1)
    music(5 ,0 ,0.5)
    music(1 ,0 ,1.5)
    music(5 ,0 ,1)

    music(3 ,0 ,3)
    # 2
    music(2 ,0 ,0.5)
    music(3 ,0 ,0.5)

    music(4 ,0 ,2)
    #
    music(1 ,1 ,1)
    music(7 ,0 ,0.5)
    music(1 ,1 ,0.5)

    music(5 ,0 ,2)
    music(4 ,0 ,1)
    music(3 ,0 ,0.75)
    music(4 ,0 ,0.25)

    music(4 ,0 ,2)
    #
    music(1 ,1 ,1)
    music(7 ,0 ,0.5)
    music(6 ,0 ,0.5)

    music(5 ,0 ,3)
    #
    music(1 ,1 ,0.5)
    music(2 ,1 ,0.5)

    music(3 ,1 ,1)
    music(1 ,1 ,0.5)
    music(6 ,0 ,1.5)
    music(2 ,1 ,1)

    music(7 ,0 ,1)
    music(5 ,0 ,0.5)
    music(3 ,0 ,1.5)
    music(7 ,0 ,1)

    music(6 ,0 ,1)
    music(5 ,0 ,0.5)
    music(1 ,0 ,1.5)
    music(5 ,0 ,1)

    music(3 ,0 ,3)
    #
    music(2 ,0 ,0.5)
    music(3 ,0 ,0.5)

    music(4 ,0 ,2)
    #
    music(5 ,0 ,1)
    music(4 ,0 ,0.5)
    music(5 ,0 ,0.5)

    music(3 ,0 ,1)
    music(5 ,0 ,1)
    music(1 ,1 ,1)
    music(3 ,1 ,1)

    music(2 ,1 ,1.5)
    music(2 ,1 ,0.5)
    music(2 ,1 ,0.5)
    music(1 ,1 ,1)
    music(1 ,1 ,0.5)

    music(1 ,1 ,4)
    # 加空白
    track.append(mido.Message('note_on', note=0, velocity=0, time=0))
    track.append(mido.Message('note_off', note=0, velocity=0, time=480 *7))


    music(1 ,1 ,0.5)
    music(2 ,1 ,0.5)

    music(3 ,1 ,1)
    music(1 ,1 ,0.5)
    music(6 ,0 ,1.5)
    music(2 ,1 ,1)

    music(7 ,0 ,1)
    music(5 ,0 ,0.5)
    music(3 ,0 ,1.5)
    music(7 ,0 ,1)

    music(6 ,0 ,1)
    music(5 ,0 ,0.5)
    music(1 ,0 ,1.5)
    music(5 ,0 ,1)

    music(3 ,0 ,3)

    #
    music(2 ,0 ,0.5)
    music(3 ,0 ,0.5)

    music(4 ,0 ,2)
    #
    music(1 ,1 ,1)
    music(7 ,0 ,0.5)
    music(1 ,1 ,0.5)

    music(5 ,0 ,2)
    music(4 ,0 ,1)
    music(3 ,0 ,0.75)
    music(4 ,0 ,0.25)

    music(4 ,0 ,2)
    #
    music(1 ,1 ,1)
    music(7 ,0 ,0.5)
    music(6 ,0 ,0.5)

    music(5 ,0 ,3)
    #
    music(1 ,1 ,0.5)
    music(2 ,1 ,0.5)

    music(3 ,1 ,1)
    music(1 ,1 ,0.5)
    music(6 ,0 ,1.5)
    music(2 ,1 ,1)

    music(7 ,0 ,1)
    music(5 ,0 ,0.5)
    music(3 ,0 ,1.5)
    music(7 ,0 ,1)

    music(6 ,0 ,1)
    music(5 ,0 ,0.5)
    music(1 ,0 ,1.5)
    music(5 ,0 ,1)

    music(3 ,0 ,3)
    #
    music(2 ,0 ,0.5)
    music(3 ,0 ,0.5)

    music(4 ,0 ,2)
    music(5 ,0 ,1)
    music(4 ,0 ,0.5)
    music(5 ,0 ,0.5)

    music(3 ,0 ,1)
    music(5 ,0 ,1)
    music(1 ,1 ,1)
    music(3 ,1 ,1)

    music(2 ,1 ,0.5)
    music(2 ,1 ,1.5)
    music(2 ,1 ,0.75)
    music(1 ,1 ,1.25)

    music(1 ,1 ,4)
    #
    music(6 ,0 ,1.5)
    music(7 ,0 ,0.5)
    music(1 ,1 ,1)
    music(7 ,0 ,0.5)
    music(6 ,0 ,0.5)

    music(5 ,0 ,1)
    music(3 ,1 ,1)
    music(3 ,1 ,2)
    #

    music(2 ,1 ,1.5)
    music(3 ,1 ,0.5)
    music(4 ,1 ,1)
    music(3 ,1 ,0.5)
    music(2 ,1 ,0.5)

    music(1 ,1 ,1)
    music(2 ,1 ,1)
    music(5 ,0 ,2)
    #
    music(4 ,0 ,1.5)
    music(5 ,0 ,0.5)
    music(6 ,0 ,1)
    music(5 ,0 ,0.5)
    music(4 ,0 ,0.5)

    music(3 ,0 ,1)
    music(1 ,1 ,1)
    music(1 ,1 ,1)
    music(1 ,1 ,1)

    #
    music(7 ,0 ,2)
    music(6 ,0 ,1)
    music(7 ,0 ,1)

    music(1 ,1 ,1)
    # 加空白
    track.append(mido.Message('note_on', note=0, velocity=0, time=0))
    track.append(mido.Message('note_off', note=0, velocity=0, time=480 *1))
    music(2 ,1 ,0.75)
    music(3 ,1 ,0.25)
    music(2 ,1 ,0.75)
    music(1 ,1 ,0.25)

    music(6 ,0 ,0.5)
    music(1 ,1 ,1.5)
    music(3 ,1 ,0.75)
    music(5 ,1 ,1.25  )  # /

    music(2 ,1 ,0.5)
    music(1 ,1 ,1.5)
    #
    music(2 ,1 ,0.75)
    music(3 ,1 ,0.25)
    music(2 ,1 ,0.75)
    music(1 ,1 ,0.25)

    music(6 ,0 ,0.5)
    music(1 ,1 ,1.5)
    music(3 ,1 ,0.75)
    music(5 ,1 ,1.25)

    music(2 ,1 ,0.5)
    music(1 ,1 ,1.5)
    #
    music(2 ,1 ,0.75)
    music(3 ,1 ,0.25)
    music(2 ,1 ,0.75)
    music(1 ,1 ,0.25)

    music(6 ,0 ,0.5)
    music(1 ,1 ,1.5)
    music(3 ,1 ,0.75)
    music(5 ,1 ,1.25  )  # \

    music(5 ,1 ,0.125)
    music(6 ,1 ,0.375)
    music(5 ,1 ,1.5)

    music(5 ,1 ,0.5)
    music(1 ,2 ,1.5)

    music(7 ,1 ,0.5)
    music(5 ,1 ,1.5)
    music(3 ,1 ,0.5)
    music(5 ,1 ,1)
    music(2 ,1 ,0.5)

    music(2 ,1 ,2)
    #
    music(2 ,1 ,0.75)
    music(3 ,1 ,0.25)
    music(2 ,1 ,0.75)
    music(1 ,1 ,0.25)

    music(6 ,0 ,0.5)
    music(1 ,1 ,1.5)
    music(3 ,1 ,0.75)
    music(5 ,1 ,1.25)
    #
    music(2 ,1 ,0.5)
    music(1 ,1 ,1.5)
    music(1 ,1 ,0.75)
    music(1 ,1 ,0.25)
    music(2 ,1 ,0.75)
    music(3 ,1 ,0.25)

    music(4 ,1 ,0.75)
    music(3 ,1 ,1.25  )  # \
    music(3 ,1 ,0.125)
    music(2 ,1 ,0.875  )  # \
    music(7 ,0 ,1)

    music(1 ,1 ,3)
    #
    music(1 ,1 ,0.75)
    music(7 ,0 ,0.25)

    music(6 ,0 ,1)
    music(7 ,0 ,1)
    music(1 ,1 ,1)
    music(2 ,1 ,1)

    music(1 ,1 ,1)
    music(5 ,0 ,1)
    music(3 ,0 ,1  )  # \
    music(5 ,0 ,1)

    music(6 ,0 ,0.75)
    music(2 ,1 ,1.25)
    music(7 ,0 ,0.75)
    music(1 ,1 ,1.25)

    music(1 ,1 ,3)
    music(1 ,1 ,0.75)
    music(7 ,0 ,0.25)

    music(6 ,0 ,1)
    music(7 ,0 ,1)
    music(1 ,1 ,1)
    music(2 ,1 ,1)

    music(1 ,1 ,1)
    music(5 ,0 ,1)
    music(1 ,1 ,1  )  # \
    music(2 ,1 ,1)

    music(3 ,1 ,0.75)
    music(4 ,1 ,1.25)
    music(2 ,1 ,0.75)
    music(1 ,1 ,1.25)

    music(1 ,1 ,3)
    # Kongbai
    #
    music(3 ,1 ,1)
    music(1 ,1 ,1)
    music(5 ,1 ,1)
    music(1 ,1 ,1)
    music(1 ,1 ,1)
    music(2 ,1 ,1)
    music(5 ,1 ,1)
    music(1 ,1 ,1)
    music(1 ,1 ,1)
    music(2 ,1 ,1)
    music(5 ,1 ,1)
    music(1 ,1 ,1)
    music(1 ,1 ,1)
    music(2 ,1 ,1)
    music(3 ,1 ,1)
    music(1 ,1 ,1)
    music(2 ,1 ,2)
    music(5 ,1 ,1)
    music(1 ,1 ,1)
    music(1 ,1 ,1)
    music(2 ,1 ,1)
    music(5 ,1 ,1)
    music(1 ,1 ,1)
    music(2 ,1 ,2)
    music(1 ,1 ,2)
    music(2 ,1 ,3)
    music(1 ,1 ,0.5)
    music(2 ,1 ,0.5)

    music(3 ,1 ,1)
    music(1 ,1 ,0.5)
    music(6 ,0 ,1.5)
    music(2 ,1 ,1)

    music(7 ,0 ,1)
    music(5 ,0 ,0.5)
    music(3 ,0 ,1.5)
    music(7 ,0 ,1)

    music(6 ,0 ,1)
    music(5 ,0 ,0.5)
    music(1 ,0 ,1.5)
    music(5 ,0 ,1)

    music(3 ,0 ,3)

    #
    music(2 ,0 ,0.5)
    music(3 ,0 ,0.5)

    music(4 ,0 ,2)
    #
    music(1 ,1 ,1)
    music(7 ,0 ,0.5)
    music(1 ,1 ,0.5)

    music(5 ,0 ,2)
    music(4 ,0 ,1)
    music(3 ,0 ,0.75)
    music(4 ,0 ,0.25)

    music(4 ,0 ,2)
    #
    music(1 ,1 ,1)
    music(7 ,0 ,0.5)
    music(6 ,0 ,0.5)

    music(5 ,0 ,3)
    #
    music(1 ,1 ,0.5)
    music(2 ,1 ,0.5)

    music(3 ,1 ,1)
    music(1 ,1 ,0.5)
    music(6 ,0 ,1.5)
    music(2 ,1 ,1)

    music(7 ,0 ,1)
    music(5 ,0 ,0.5)
    music(3 ,0 ,1.5)
    music(7 ,0 ,1)

    music(6 ,0 ,1)
    music(5 ,0 ,0.5)
    music(1 ,0 ,1.5)
    music(5 ,0 ,1)

    music(3 ,0 ,3)
    #
    music(2 ,0 ,0.5)
    music(3 ,0 ,0.5)

    music(4 ,0 ,2)
    music(5 ,0 ,1)
    music(4 ,0 ,0.5)
    music(5 ,0 ,0.5)

    music(3 ,0 ,1)
    music(5 ,0 ,1)
    music(1 ,1 ,1)
    music(3 ,1 ,1)

    music(2 ,1 ,0.5)
    music(2 ,1 ,1.5)
    music(2 ,1 ,0.75)
    music(1 ,1 ,1.25)

    music(1 ,1 ,4)
    #
    music(6 ,0 ,1.5)
    music(7 ,0 ,0.5)
    music(1 ,1 ,1)
    music(7 ,0 ,0.5)
    music(6 ,0 ,0.5)

    music(5 ,0 ,1)
    music(3 ,1 ,1)
    music(3 ,1 ,2)
    #

    music(2 ,1 ,1.5)
    music(3 ,1 ,0.5)
    music(4 ,1 ,1)
    music(3 ,1 ,0.5)
    music(2 ,1 ,0.5)

    music(1 ,1 ,1)
    music(2 ,1 ,1)
    music(5 ,0 ,2)
    #
    music(4 ,0 ,1.5)
    music(5 ,0 ,0.5)
    music(6 ,0 ,1)
    music(5 ,0 ,0.5)
    music(4 ,0 ,0.5)

    music(3 ,0 ,1)
    music(1 ,1 ,1)
    music(1 ,1 ,1)
    music(1 ,1 ,1)

    #
    music(7 ,0 ,2)
    music(6 ,0 ,1)
    music(7 ,0 ,1)

    music(1 ,1 ,1)
    # 加空白
    track.append(mido.Message('note_on', note=0, velocity=0, time=0))
    track.append(mido.Message('note_off', note=0, velocity=0, time=480 *1))
    music(2 ,1 ,0.75)
    music(3 ,1 ,0.25)
    music(2 ,1 ,0.75)
    music(1 ,1 ,0.25)

    music(6 ,0 ,0.5)
    music(1 ,1 ,1.5)
    music(3 ,1 ,0.75)
    music(5 ,1 ,1.25  )  # /

    music(2 ,1 ,0.5)
    music(1 ,1 ,1.5)
    #
    music(2 ,1 ,0.75)
    music(3 ,1 ,0.25)
    music(2 ,1 ,0.75)
    music(1 ,1 ,0.25)

    music(6 ,0 ,0.5)
    music(1 ,1 ,1.5)
    music(3 ,1 ,0.75)
    music(5 ,1 ,1.25)

    music(2 ,1 ,0.5)
    music(1 ,1 ,1.5)
    #
    music(2 ,1 ,0.75)
    music(3 ,1 ,0.25)
    music(2 ,1 ,0.75)
    music(1 ,1 ,0.25)

    music(6 ,0 ,0.5)
    music(1 ,1 ,1.5)
    music(3 ,1 ,0.75)
    music(5 ,1 ,1.25  )  # \

    music(5 ,1 ,0.125)
    music(6 ,1 ,0.375)
    music(5 ,1 ,1.5)

    music(5 ,1 ,0.5)
    music(1 ,2 ,1.5)

    music(7 ,1 ,0.5)
    music(5 ,1 ,1.5)
    music(3 ,1 ,0.5)
    music(5 ,1 ,1)
    music(2 ,1 ,0.5)

    music(2 ,1 ,2)
    #
    music(2 ,1 ,0.75)
    music(3 ,1 ,0.25)
    music(2 ,1 ,0.75)
    music(1 ,1 ,0.25)

    music(6 ,0 ,0.5)
    music(1 ,1 ,1.5)
    music(3 ,1 ,0.75)
    music(5 ,1 ,1.25)
    #
    music(2 ,1 ,0.5)
    music(1 ,1 ,1.5)
    music(1 ,1 ,0.75)
    music(1 ,1 ,0.25)
    music(2 ,1 ,0.75)
    music(3 ,1 ,0.25)

    music(4 ,1 ,0.75)
    music(3 ,1 ,1.25  )  # \
    music(3 ,1 ,0.125)
    music(2 ,1 ,0.875  )  # \
    music(7 ,0 ,1)

    music(1 ,1 ,3)
    #
    music(1 ,1 ,0.75)
    music(7 ,0 ,0.25)

    music(6 ,0 ,1)
    music(7 ,0 ,1)
    music(1 ,1 ,1)
    music(2 ,1 ,1)

    music(1 ,1 ,1)
    music(5 ,0 ,1)
    music(3 ,0 ,1  )  # \
    music(5 ,0 ,1)

    music(6 ,0 ,0.75)
    music(2 ,1 ,1.25)
    music(7 ,0 ,0.75)
    music(1 ,1 ,1.25)

    music(1 ,1 ,3)
    music(1 ,1 ,0.75)
    music(7 ,0 ,0.25)

    music(6 ,0 ,1)
    music(7 ,0 ,1)
    music(1 ,1 ,1)
    music(2 ,1 ,1)

    music(1 ,1 ,1)
    music(5 ,0 ,1)
    music(1 ,1 ,1  )  # \
    music(2 ,1 ,1)

    music(3 ,1 ,0.75)
    music(4 ,1 ,1.25)
    music(2 ,1 ,0.75)
    music(1 ,1 ,1.25)

    music(1 ,1 ,3)
    # Kongbai
    #
    music(1 ,1 ,2)
    music(1 ,1 ,1.75)
    music(4 ,0 ,0.25)
    music(1 ,1 ,2)
    music(7 ,0 ,2)

    music(1 ,1 ,2)
    music(5 ,1 ,2)

    music(6 ,1 ,2)
    music(5 ,1 ,2)

    music(2 ,1 ,2)
    music(4 ,1 ,2)

    music(3 ,1 ,4)

    music(1 ,1 ,2)
    music(3 ,1 ,2)

    music(4 ,1 ,2)
    music(3 ,1 ,2)

    music(2 ,1 ,2)
    music(7 ,0 ,2)

    music(1 ,1 ,4)

    music(1 ,1 ,2)
    music(5 ,1 ,2)

    music(6 ,1 ,2)
    music(5 ,1 ,2)

    music(2 ,1 ,2)
    music(4 ,1 ,1)
    music(3 ,1 ,1)

    music(3 ,1 ,4)

    music(1 ,1 ,2)
    music(3 ,1 ,2)

    music(4 ,1 ,2)
    music(3 ,1 ,2)

    music(2 ,1 ,2)
    music(7 ,0 ,2)

    music(1 ,1 ,2)
    # kongbai

    music(6 ,0 ,1)
    music(7 ,0 ,0.5)

    music(1 ,1 ,2)
    music(5 ,1 ,2)

    music(6 ,1 ,2)
    music(5 ,1 ,1)
    music(2 ,1 ,1)

    music(2 ,1 ,2)
    music(4 ,1 ,1)
    music(3 ,1 ,1)

    music(3 ,1 ,4)

    music(1 ,1 ,2)
    music(3 ,1 ,2)

    music(4 ,1 ,2)
    music(3 ,1 ,2)

    music(2 ,1 ,2)
    music(7 ,0 ,2)

    music(1 ,1 ,3)
    music(6 ,0 ,0.5)
    music(7 ,0 ,0.5)

    music(1 ,1 ,2)
    music(5 ,1 ,2)

    music(6 ,1 ,2)
    music(5 ,1 ,2)

    music(7 ,1 ,2)
    music(7 ,1 ,1)
    music(1 ,2 ,1)

    music(1 ,2 ,4)

    music(1 ,2 ,2)
    music(5 ,1 ,2)

    music(4 ,1 ,2)
    music(3 ,1 ,1)
    music(2 ,1 ,1)

    music(2 ,1 ,2)
    music(2 ,1 ,2)

    music(6 ,0 ,2)
    music(1 ,1 ,1)
    music(3 ,2 ,1)

    music(4 ,2 ,4)
    music(4 ,2 ,1)
    music(5 ,2 ,1)
    music(5 ,2 ,1)
    music(6 ,1 ,1)
    music(4 ,2 ,4)
    music(4 ,1 ,1)
    # kongbai
    music(2 ,1 ,0.75)
    music(3 ,1 ,0.25)
    music(2 ,1 ,0.75)
    music(1 ,1 ,0.25)

    music(6 ,0 ,0.5)
    music(1 ,1 ,1.5)
    music(3 ,1 ,0.75)
    music(5 ,1 ,1.25  )  # /

    music(2 ,1 ,0.5)
    music(1 ,1 ,1.5)
    #
    music(2 ,1 ,0.75)
    music(3 ,1 ,0.25)
    music(2 ,1 ,0.75)
    music(1 ,1 ,0.25)

    music(6 ,0 ,0.5)
    music(1 ,1 ,1.5)
    music(3 ,1 ,0.75)
    music(5 ,1 ,1.25)

    music(2 ,1 ,0.5)
    music(1 ,1 ,1.5)
    #
    music(2 ,1 ,0.75)
    music(3 ,1 ,0.25)
    music(2 ,1 ,0.75)
    music(1 ,1 ,0.25)

    music(6 ,0 ,0.5)
    music(1 ,1 ,1.5)
    music(3 ,1 ,0.75)
    music(5 ,1 ,1.25  )  # \

    music(5 ,1 ,0.125)
    music(6 ,1 ,0.375)
    music(5 ,1 ,1.5)

    music(5 ,1 ,0.5)
    music(1 ,2 ,1.5)

    music(7 ,1 ,0.5)
    music(5 ,1 ,1.5)
    music(3 ,1 ,0.5)
    music(5 ,1 ,1)
    music(2 ,1 ,0.5)

    music(2 ,1 ,2)
    #
    music(2 ,1 ,0.75)
    music(3 ,1 ,0.25)
    music(2 ,1 ,0.75)
    music(1 ,1 ,0.25)

    music(6 ,0 ,0.5)
    music(1 ,1 ,1.5)
    music(3 ,1 ,0.75)
    music(5 ,1 ,1.25)
    #
    music(2 ,1 ,0.5)
    music(1 ,1 ,1.5)
    music(1 ,1 ,0.75)
    music(1 ,1 ,0.25)
    music(2 ,1 ,0.75)
    music(3 ,1 ,0.25)

    music(6 ,1 ,0.75)
    music(3 ,1 ,1.25  )  # \
    music(3 ,1 ,0.125)
    music(2 ,1 ,0.875  )  # \
    music(7 ,0 ,1)

    music(1 ,1 ,3)
    #
    music(1 ,1 ,0.75)
    music(7 ,0 ,0.25)

    music(6 ,0 ,1)
    music(7 ,0 ,1)
    music(1 ,1 ,1)
    music(2 ,1 ,1)

    music(1 ,1 ,1)
    music(5 ,0 ,1)
    music(3 ,0 ,1  )  # \
    music(5 ,0 ,1)

    music(6 ,0 ,0.75)
    music(2 ,1 ,1.25)
    music(7 ,0 ,0.75)
    music(1 ,1 ,1.25)

    music(1 ,1 ,3)
    music(1 ,1 ,0.75)
    music(7 ,0 ,0.25)

    music(6 ,0 ,1)
    music(7 ,0 ,1)
    music(1 ,1 ,1)
    music(2 ,1 ,1)

    music(1 ,1 ,1)
    music(5 ,0 ,1)
    music(4 ,0 ,1)
    music(3 ,1 ,1)

    music(4 ,1 ,0.75)
    music(1 ,1 ,1.25)
    music(1 ,1 ,0.75)
    music(5 ,1 ,1.25)

    music(3 ,1 ,3)
    music(3 ,1 ,0.75)
    music(2 ,1 ,0.25)

    music(1 ,1 ,1)
    music(2 ,1 ,1)
    music(3 ,1 ,1)
    music(4 ,1 ,1)

    music(3 ,1 ,1)
    music(1 ,1 ,1)
    music(5 ,0 ,1)
    music(3 ,0 ,1)

    music(2 ,1 ,0.75)
    music(3 ,1 ,1.25)
    music(2 ,1 ,0.75)
    music(1 ,1 ,1.25)

    music(1 ,1 ,2)
    music(4 ,-2 ,0.25)
    music(1 ,-1 ,0.25)
    music(4 ,-1 ,0.25)
    music(5 ,-1 ,0.25)
    music(1 ,0 ,0.25)
    music(2 ,0 ,0.25)
    music(5 ,0 ,0.25)
    music(1 ,1 ,0.25)

    music(2 ,1 ,0.25)
    music(5 ,1 ,0.25)
    music(1 ,2 ,0.25)
    music(2 ,2 ,0.25)
    music(5 ,2 ,0.25)
    music(1 ,3 ,0.75)
    music(1 ,1 ,0.5)
    music(5 ,1 ,1.5)
    music(1 ,1 ,0.5)
    music(5 ,1 ,1.5)
    music(1 ,1 ,0.5)
    music(5 ,1 ,1.5)
    music(1 ,1 ,0.5)
    music(5 ,1 ,1.5)
    music(1 ,1 ,0.5)
    music(5 ,1 ,1.5)
    music(1 ,1 ,0.5)
    music(5 ,1 ,3.5)


def play_midi(file='a2.mid'):
    import pygame
    freq = 44100
    bitsize = -16
    channels = 2
    buffer = 1024
    pygame.mixer.init(freq, bitsize, channels, buffer)
    pygame.mixer.music.set_volume(1)
    clock = pygame.time.Clock()
    try:
       pygame.mixer.music.load(file)
    except:
       import traceback
       print(traceback.format_exc())
    pygame.mixer.music.play()
    pygame.mixer.music
    while pygame.mixer.music.get_busy():
       clock.tick(30)




# lemon_music()

import numpy as np



class Piano:
    def __init__(self):
        pass

    def play_now(self):
        mid.save('a2.mid')
        play_midi("a2.mid")

    def add_sound(self, num, beat=1):   # num from 0 to 20
        music(num % 7 + 1, num // 7 - 1, beat)

    def play(self, mus:np.array, mode='t'):
        if mus.shape[1] != 2:
            mus = mus.transpose([1, 0])
        mus = mus.tolist()
        for num, time in mus:
            if mode != 'time':
                time = idx2time[time]
            self.add_sound(int(num), time)
        self.play_now()


# p = Piano()
# p.play(np.ones([2, 100]))

# num = 0, 1, ... , 20
# time = 0:0.25, 1:0.5, 2:0.75, 3:1, 4:1.25, 5:1.5, 6:1.75, 7:2, 8:2.5, 9:3, 10:4

# lemon_music()
# print(data)


