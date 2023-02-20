import time
import speech_recognition as sr
time_now = time.strftime("%Y%m%d-%H%M%S")
r = sr.Recognizer() # turn on your microphone
mic = sr.Microphone()
with mic as source:
  r.adjust_for_ambient_noise(source) # denoise
  print('Started Recording')
  audio = r.record(source, 10) # record 2 seconds from the microphone
  # or you can use r.listen(source) to keep listening to microphone until timeout (no voice)
  with open(f"Voice-{time_now}.wav", "wb") as f:
    # save your voice in wav for further processing
    f.write(audio.get_wav_data(convert_rate=16000))
    print('Voice Saved')
