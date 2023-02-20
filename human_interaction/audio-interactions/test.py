import python_speech_features as sf
from scipy.io import wavfile

fs, audio = wavfile.read('./Voice-20230213-173542.wav')
mfcc_features = sf.mfcc(audio, fs) # mfcc 13-dimension features with multiple instance

print (mfcc_features.shape)

fbank_features = sf.logfbank(audio, fs) # fbank 26-dimension features with multiple instance

print (fbank_features.shape)

# here we only use the default parameters for extraction, please review the functions definition to see what the parameters are and their use
