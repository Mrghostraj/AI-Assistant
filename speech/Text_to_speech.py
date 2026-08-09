import subprocess
from piper import PiperVoice


class texttospeech:

    def __init__(self, english_voice, hindi_voice):

        self.voices = {
            "en": PiperVoice.load(english_voice),
            "hi": PiperVoice.load(hindi_voice)
        }

    def speak(self, text, language="en"):

        voice = self.voices.get(language, self.voices["en"])

        process = None

        for audio_chunk in voice.synthesize(text):

            if process is None:
                process = subprocess.Popen(
                    [
                        "ffplay",
                        "-nodisp",
                        "-autoexit",
                        "-loglevel",
                        "quiet",
                        "-f",
                        "s16le",
                        "-ar",
                        str(audio_chunk.sample_rate),
                        "-ac",
                        str(audio_chunk.sample_channels),
                        "-"
                    ],
                    stdin=subprocess.PIPE
                )

            process.stdin.write(audio_chunk.audio_int16_bytes)

        if process is not None:
            process.stdin.close()
            process.wait()

    