#import os
import requests
import base64
#from dotenv.main import load_dotenv

class Imagetotext():

    def __init__(self , GPT4V_ENDPOINT, GPT4V_KEY,IMAGE ): #IMAGE_PATH):
        #self.GPT4V_ENDPOINT ,self.GPT4V_KEY, self.IMAGE_PATH = GPT4V_ENDPOINT, GPT4V_KEY, IMAGE #IMAGE_PATH
        self.GPT4V_ENDPOINT ,self.GPT4V_KEY, self.IMAGE = GPT4V_ENDPOINT, GPT4V_KEY, IMAGE
    
    def imagetotextfn (self):

        #encoded_image = base64.b64encode(open(self.IMAGE_PATH, 'rb').read()).decode('ascii')
        encoded_image = base64.b64encode(self.IMAGE).decode('ascii')
        print ("got the image")
        headers = { 
            "Content-Type": "application/json",
            "api-key": self.GPT4V_KEY,
        }
        # Payload for the request
        payload = {
            "messages": [
                    {
                        "role": "system",
                        "content": [
                            {
                                "type": "text",
                                "text": "You are an AI assistant that helps people find information. Please extract the text from the image provided.Please respond only with the text inside the image nothing else"
                            }
                        ]
                    },
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "image_url",
                                "image_url": {
                                "url": f"data:image/jpeg;base64,{encoded_image}" }
                            },
                            {
                        "type": "text",
                        "text": "Here is the image"
                            }
                        ]
                    }
                ],
            "temperature": 0.7,
            "top_p": 0.95,
            "max_tokens": 800
        }
        try:
            print ("inside try of the imagetotextfn")
            response = requests.post(self.GPT4V_ENDPOINT, headers=headers, json=payload)
            response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
            print ("response is \n",response.json())
        except requests.RequestException as e:
            raise SystemExit(f"Failed to make the request. Error: {e}")
        return ( response.json()["choices"][0]['message']['content'])
       
            


