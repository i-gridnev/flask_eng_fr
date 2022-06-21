'''
    Translation module with ibm cloud Language Translator Service
'''
import os

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


def get_translator():
    ''' Return an instance of Translator '''
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )
    language_translator.set_service_url(url)
    return language_translator


def english_to_french(english_text):
    ''' Translate text from English to French '''
    translator = get_translator()
    french_text = translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    return french_text['translations'][0]['translation']


def french_to_english(french_text):
    ''' Translate text from French to English '''
    translator = get_translator()
    english_text = translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    return english_text['translations'][0]['translation']
