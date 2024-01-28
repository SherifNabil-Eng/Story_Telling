
import azure.cognitiveservices.speech as speechsdk
class Texttospeech():

    def __init__(self, subscription_original,subscription_translated, SPEECH_REGION,SPEECH_ENDPOINT_ID):
        self.subscription_original = subscription_original
        self.subscription_translated = subscription_translated

        self.SPEECH_REGION = SPEECH_REGION
        self.SPEECH_ENDPOINT_ID = SPEECH_ENDPOINT_ID

    #voice='ar-SA-ZariyahNeural'
    def text_to_speech(self,phrase, voice='Sherif_EnglishNeural',translated_flag=True):
    #en-NG-AbeoNeural
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
        if translated_flag:
            self.subscription = self.subscription_translated
        else:
            self.subscription = self.subscription_original
        speech_config = speechsdk.SpeechConfig(
        subscription=self.subscription,
        region=self.SPEECH_REGION
        )
        
        if translated_flag:
            speech_config.endpoint_id = self.SPEECH_ENDPOINT_ID    
        audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

        # The language of the voice that speaks.
        speech_config.speech_synthesis_voice_name=voice

        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

        speech_synthesis_result = speech_synthesizer.speak_text_async(phrase).get()

        if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            return True
        elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
            return False