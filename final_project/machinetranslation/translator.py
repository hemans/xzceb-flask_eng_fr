"""
Provides English to French translation
"""
import os
import json
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

APIKEY = os.environ['APIKEY']

URL = os.environ['URL']

AUTHENTICATOR = IAMAuthenticator(APIKEY)

LANGUAGE_TRANSLATOR = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=AUTHENTICATOR
)

LANGUAGE_TRANSLATOR.set_service_url(URL)

def english_to_french(english_text):
    '''
    Function to translate english to french
    '''
    response = LANGUAGE_TRANSLATOR.translate(text=english_text, model_id='en-fr')
    french_text = response.get_result()
    return french_text['translations'][0]['translation']

def french_to_english(french_text):
    '''Function to translate french to english'''
    response = LANGUAGE_TRANSLATOR.translate(text=french_text, model_id='fr-en')
    english_text = response.get_result()
    return english_text['translations'][0]['translation']
