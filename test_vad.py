import numpy as np
from speech.vad import VoiceActivityDetector

vad = VoiceActivityDetector()

silence = np.zeros(512, dtype=np.float32)

probabilty = vad.is_speech(silence, sample_rate=16000)

print("Specch Probability:", probabilty)