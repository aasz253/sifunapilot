import speech_recognition as sr
from typing import Optional


class STTEngine:
    def __init__(self) -> None:
        self.enabled = True
        self.recognizer = sr.Recognizer()

    def listen(self, timeout: int = 5, phrase_time_limit: int = 10) -> str:
        try:
            microphone = sr.Microphone()
            with microphone as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            try:
                text = self.recognizer.recognize_google(audio)
                return text
            except sr.UnknownValueError:
                return ""
            except sr.RequestError:
                return ""
        except Exception:
            return ""

    def listen_once(self, timeout: int = 5) -> str:
        return self.listen(timeout=timeout)


def get_stt() -> STTEngine:
    return STTEngine()
