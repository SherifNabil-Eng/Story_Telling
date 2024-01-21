
import azure.cognitiveservices.speech as speechsdk
class Texttospeech():

    def __init__(self, subscription, SPEECH_REGION):
        self.subscription = subscription
        self.SPEECH_REGION = SPEECH_REGION

    def text_to_speech(self,phrase, voice='ar-SA-ZariyahNeural'):
    #en-NG-AbeoNeural
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
        speech_config = speechsdk.SpeechConfig(
        subscription=self.subscription,
        region=self.SPEECH_REGION
    )
            
        audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

        # The language of the voice that speaks.
        speech_config.speech_synthesis_voice_name=voice

        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

        speech_synthesis_result = speech_synthesizer.speak_text_async(phrase).get()

        if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            return True
        elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
            return False