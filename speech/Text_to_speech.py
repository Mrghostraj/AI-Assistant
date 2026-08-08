from piper import PiperVoice
import wave 

class texttospeech:

    def __init__(self, voice_model):
        self.voice = PiperVoice.load(voice_model)

    def speak(self, text, output_file="response.wav"):
        with wave.open(output_file, "wb") as audio_file:
            self.voice.synthesize_wav(text, audio_file)

        return output_file

    