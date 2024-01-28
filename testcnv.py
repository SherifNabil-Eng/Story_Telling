'''
  For more samples please visit https://github.com/Azure-Samples/cognitive-services-speech-sdk 
'''

import azure.cognitiveservices.speech as speechsdk

# Creates an instance of a speech config with specified subscription key and service region.
speech_key = "8e746d7f33a84ee29bbe62a4e64a38a8"
service_region = "eastus"

speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
speech_config.endpoint_id = "9c35d910-cdd9-4894-9fe3-d13f10031ddc"
speech_config.speech_synthesis_voice_name = "Sherif_EnglishNeural"
speech_config.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat.Audio24Khz160KBitRateMonoMp3)

# = "Hi, this is my custom voice."
text ="Well, what is Felix doing there? He is flying - whoosh - in his balloon around the world. There is so much to see; big cities and villages, mountains, fields and forests. Felix spotted a ship in the river. Where does he want to go next? Well, that's in Felix's letter."
file_name = "sample.wav"

# using the default speaker as audio output.
file_config = speechsdk.audio.AudioOutputConfig(filename=file_name)
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=file_config)

result = speech_synthesizer.speak_text_async(text).get()
# Check result
if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized for text [{}], and the audio was saved to [{}]".format(text, file_name))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details))