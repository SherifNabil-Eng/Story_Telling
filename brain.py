import os
import openai
from dotenv.main import load_dotenv
from imagetotextcls import Imagetotext
from transtextcls import Transtext
import json
from texttospeech import Texttospeech

class Brain:

    GPT4V_ENDPOINT = ""
    GPT4V_KEY = ""
    #IMAGE_PATH = ""
    IMAGE=bytearray("", 'ascii')
    API_KEY = ""
    openai_api_version=""
    API_KEY=""
    RESOURCE_ENDPOINT=""
    llm_model=""
    subscription=""
    SPEECH_REGION=""
    originaltext=""
    originallanguage=""
    translatedtext=""
    
# Setting the environment variables for GPT4 vision
    def setenvvarimgtotext (self):
            
        load_dotenv()
        self.GPT4V_ENDPOINT = os.getenv("GPT4V_ENDPOINT","").strip()
        self.GPT4V_KEY = os.getenv("GPT4V_KEY","").strip()

        # Configuration
        #self.IMAGE_PATH = "Page1.jpg"
        return

        #return GPT4V_ENDPOINT,GPT4V_KEY,IMAGE_PATH

# Setting the environment variables for GPT4 32K to detect the language and translate 

    def setenvvartranstext (self):
        load_dotenv()
        openai.api_type = "azure"
        openai.api_version = os.getenv("OPENAI_API_VERSION")
        self.openai_api_version = openai.api_version

        self.API_KEY = os.getenv("OPENAI_API_KEY","").strip()
        assert self.API_KEY, "ERROR: Azure OpenAI Key is missing"
        openai.api_key = self.API_KEY

        self.RESOURCE_ENDPOINT = os.getenv("OPENAI_API_BASE","").strip()
        assert self.RESOURCE_ENDPOINT, "ERROR: Azure OpenAI Endpoint is missing"
        assert "openai.azure.com" in self.RESOURCE_ENDPOINT.lower(), "ERROR: Azure OpenAI Endpoint should be in the form: \n\n\t<your unique endpoint identifier>.openai.azure.com"
        openai.api_base = self.RESOURCE_ENDPOINT

        self.llm_model = os.getenv("OPENAI_CHAT_MODEL","").strip()

        return

    def setenvtexttospeech (self):
        load_dotenv()
        self.subscription = os.getenv("SPEECH_KEY","").strip()
        self.SPEECH_REGION = os.getenv("SPEECH_REGION","").strip()
        assert self.subscription, "ERROR: Azure Speech subscription key is missing"
        assert self.SPEECH_REGION, "ERROR: Azure Speech region is missing"
        return 

# initialize the class with the environment variables
    def __init__(self,IMAGE):

        self.IMAGE = IMAGE
        self.setenvvartranstext()
        self.setenvvarimgtotext()
        self.setenvtexttospeech()
    
        return

# get the text from the image
    def getimgtext(self):
        
        #GPT4V_ENDPOINT,GPT4V_KEY,IMAGE_PATH = setenvvarimgtotext ()
        img_text = Imagetotext(self.GPT4V_ENDPOINT,self.GPT4V_KEY,self.IMAGE)
        print ("inside getimgtext")
        self.originaltext = img_text.imagetotextfn()
        print ("original text is \n",self.originaltext)
        return 

# translate the text and get the translated text and the original language    
    def gettranslatedtext(self):
        # detect the language and translate
        #API_KEY,openai_api_version,RESOURCE_ENDPOINT,llm_model = setenvvartranstext ()
        #imgtext ="""Willkommen im Kindergarten\
        #            „Guten Morgen!“, ruft Moritz. Die anderen Kinder der Krabbelkäfergruppe sind schon alle da.\
        #            Sie hängen ihre Jacken auf und ziehen die Hausschuhe an. Sie ist heute zum ersten Mal im Kindergarten.\
        #            Wo soll sie denn jetzt hin? Da kommt Sarah. Sie kann Lise alles zeigen. Das wird ein aufregender Tag!"""
        transtext = Transtext(self.API_KEY,self.openai_api_version,self.RESOURCE_ENDPOINT,self.llm_model,self.originaltext)
        self.originallanguage , self.translatedtext = transtext.getresponse()
        print ("oiginal language is {} and translated text is \n {}".format (self.originallanguage , self.translatedtext))
        return 

    # detect the language and translate
    #API_KEY,openai_api_version,RESOURCE_ENDPOINT,llm_model = setenvvartranstext ()
    #imgtext ="""Willkommen im Kindergarten\
    #            „Guten Morgen!“, ruft Moritz. Die anderen Kinder der Krabbelkäfergruppe sind schon alle da.\
    #            Sie hängen ihre Jacken auf und ziehen die Hausschuhe an. Sie ist heute zum ersten Mal im Kindergarten.\
    #            Wo soll sie denn jetzt hin? Da kommt Sarah. Sie kann Lise alles zeigen. Das wird ein aufregender Tag!"""
    #transtext = Transtext(API_KEY,openai_api_version,RESOURCE_ENDPOINT,llm_model,imgtext)
    #Language , Translatedtext = transtext.getresponse()

    #print ("Original text is \n {}".format (imgtext))
    #print ("\n Langauge is {} and \n the translated text is \n {} ".format (Language , Translatedtext))

# text to speech
    def texttospeechfn(self):
        #
        #subscription,SPEECH_REGION = setenvtexttospeech ()
        self.texttospeech = Texttospeech(self.subscription,self.SPEECH_REGION)
        #original text voice 
        self.texttospeech.text_to_speech(self.originaltext, voice='de-DE-KatjaNeural')

        #translated text voice
        self.texttospeech.text_to_speech(self.translatedtext, voice='en-US-RyanMultilingualNeural')
        return

# out put to a text file
    def outputfile(self):
        #output to a text file
        self.output_file = open("Translated.txt", "w")
        self.Content = "Original text: \n "+ self.originaltext+"\n\n Language is "+self.originallanguage+"\n\n Translated text is: \n "+self.translatedtext
        self.output_file.write(self.Content)
        self.output_file.close()


