import scipy.io.wavfile as wav
from python_speech_features import mfcc
import speech_recognition as sr

# Load the .wav file
rate, signal = wav.read('./Voice-20230220-165610.wav')

# Extract the Mel-frequency cepstral coefficients (MFCCs) from the signal
mfcc_feat = mfcc(signal, rate)

# Convert the MFCCs to audio data using the inverse transform
audio_data = mfcc_feat.T

# Convert the audio data to a format that can be recognized by SpeechRecognition
audio = sr.AudioData(audio_data.tobytes(), sample_rate=rate, sample_width=2)

# Use SpeechRecognition to recognize the speech in the audio signal
r = sr.Recognizer()
text = r.recognize_google(audio)

# Print the recognized text
print(text)




