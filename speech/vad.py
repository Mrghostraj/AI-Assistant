import torch 
from silero_vad import load_silero_vad

class VoiceActivityDetector:

    def __init__(self):
        self.model = load_silero_vad()

    def is_speech(self, audio_chunk, sample_rate=16000):
        audio_tensor =  torch.from_numpy(audio_chunk)

        speech_probabilty = self.model(audio_tensor, sample_rate)

        return speech_probabilty.item()
    