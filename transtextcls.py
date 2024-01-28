import openai
import os
from langchain.chat_models import AzureChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser
import azure.cognitiveservices.speech as speechsdk


class Transtext ():
    delimiter = "###"
    langauge_schema = ResponseSchema(name="Language",
                             description="Language detected\
                             from the provided text ")
    translated_text_schema = ResponseSchema(name="Translated Text",
                             description="Translated text into English")

    response_schemas = [langauge_schema, 
                    translated_text_schema]
    
    template_string = template_string_2 = """\
                        You are an AI assistant that helps people find information.\
                        Your mission is to translate the text provided to you into English.\
                        User text will be delimited by a {delimiter} delimiter.\
                        You need first to detect the language of the provided text ,\
                        then translate it into English.\
                        text: {end_user_text}

                        {format_instructions}
                        """
    

    def __init__(self, API_KEY,openai_api_version,RESOURCE_ENDPOINT,llm_model,imgtext):
        self.API_KEY = API_KEY
        print ("API key is ,",self.API_KEY)
        self.openai_api_version = openai_api_version
        print ("openai_api_version is ,",self.openai_api_version)
        self.RESOURCE_ENDPOINT = RESOURCE_ENDPOINT
        print ("RESOURCE_ENDPOINT is ,",self.RESOURCE_ENDPOINT)
        self.llm_model = llm_model
        print ("llm_model is ,",self.llm_model)
        self.imgtext = imgtext
        print ("imgtext is ,",self.imgtext)
        self.output_parser = StructuredOutputParser.from_response_schemas(self.response_schemas)
        self.format_instructions = self.output_parser.get_format_instructions()


    def setchatobject (self):
        chat = AzureChatOpenAI(
        temperature=0.0, 
        model=self.llm_model,
        openai_api_base=self.RESOURCE_ENDPOINT,
        openai_api_version=self.openai_api_version,
        deployment_name=self.llm_model,
        openai_api_key=self.API_KEY
        )
        return chat
    
    def getresponse (self):
    
        prompt = ChatPromptTemplate.from_template(template=self.template_string_2)
        messages = prompt.format_messages(end_user_text=self.imgtext,delimiter=self.delimiter, 
                                format_instructions=self.format_instructions)
        chat = self.setchatobject()
        response = chat(messages)
        output_dict = self.output_parser.parse(response.content)
        return output_dict.get ("Language"),output_dict.get ("Translated Text")

    
