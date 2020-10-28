from array import array
import pyaudio
import wave

def record_audio(config, WAVE_OUTPUT_FILE):
    #--------- SETTING PARAMS FOR OUR AUDIO FILE ------------#
    FORMAT = pyaudio.paInt16    # format of wave
    CHANNELS = config.get_config("AUDIO", "CHANNELS")
    RATE = config.get_config("AUDIO", "RATE")
    CHUNK = config.get_config("AUDIO", "CHUNK")
    THRESHOLD = config.get_config("AUDIO", "THRESHOLD")
    SILENCE_TIME_CHECKER = config.get_config("AUDIO", "SILENCE_TIME_CHECKER")
    #--------------------------------------------------------#

    # creating PyAudio object
    audio = pyaudio.PyAudio()

    # open a new stream for microphone
    # It creates a PortAudio Stream Wrapper class object
    stream = audio.open(format=FORMAT,channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)


    #----------------- start of recording -------------------#
    print("Listening...")

    # list to save all audio frames
    frames = []

    # verify how many times just passed some seconds
    iterator_count = 0
    iterator_stop = False

    while True:
        for i in range(int(RATE / CHUNK * SILENCE_TIME_CHECKER)):
            if iterator_count > get_ammount_interations(SILENCE_TIME_CHECKER):
                iterator_stop = True
                break

            # read audio stream from microphone
            data = stream.read(CHUNK)

            if max(array('h', data)) < THRESHOLD and iterator_count > 2:
                print(i, "SILENCIO POR MUITO TEMPO PARANDO GRAVACAO")
                iterator_stop = True
                break

            # append audio data to frames list
            frames.append(data)

        if iterator_stop is True:
            break

        iterator_count += 1

    #------------------ end of recording --------------------#   
    print("Finished recording.")
      
    stream.stop_stream()    # stop the stream object
    stream.close()          # close the stream object
    audio.terminate()       # terminate PortAudio

    #------------------ saving audio ------------------------#

    # create wave file object
    waveFile = wave.open(WAVE_OUTPUT_FILE, 'wb')

    # settings for wave file object
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))

    # closing the wave file object
    waveFile.close()
    return WAVE_OUTPUT_FILE


def read_audio(WAVE_FILE):
    # function to read audio(wav) file
    WAVE_FILE.seek(0)
    audio = WAVE_FILE.read()
    return audio

def get_ammount_interations(time):
    # audio limit of wit.ai is 20 seconds, so I use 18 to make sure
    # that I will receive some response
    return int(18 / time)
