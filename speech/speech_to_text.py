from faster_whisper import WhisperModel


class speechtotext:

    def __init__(self, model_size="small"):

        self.model = WhisperModel(
            model_size,
            device="auto",
            compute_type="auto"
        )

    def transcribe(self, audio, language=None):

        if language:
            segments, info = self.model.transcribe(
                audio,
                language=language
            )
        else:
            segments, info = self.model.transcribe(
                audio
            )

        text = " ".join(
            segment.text.strip()
            for segment in segments
        )

        return text, info