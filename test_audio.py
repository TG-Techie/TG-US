import time
import audioio
import board
import digitalio

#button = digitalio.DigitalInOut(board.A1)

#button.switch_to_input(pull=digitalio.Pull.UP)

wave_file = open("system/audio_files/looping.wav", "rb")
wave = audioio.WaveFile(wave_file)
audio = audioio.AudioOut(board.A1)
audio.play(wave, loop = True)
while audio.playing:
    print('f')
'''while True:


    # This allows you to do other things while the audio plays!
    t = time.monotonic()
    while time.monotonic() - t < 6:
        pass

    audio.pause()
    print("Waiting for button press to continue!")
    while button.value:
        pass
    audio.resume()
    while audio.playing:
        pass
    print("Done!")'''