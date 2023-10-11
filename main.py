# import os
# credential_path = "/Users/shubhammojidra/Desktop/operatorai/auth.json"
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
#
#
# def translate_text(target, text):
#     """Translates text into the target language.
#
#     Target must be an ISO 639-1 language code.
#     See https://g.co/cloud/translate/v2/translate-reference#supported_languages
#     """
#     import six
#     from google.cloud import translate_v2 as translate
#
#     translate_client = translate.Client()
#
#     if isinstance(text, six.binary_type):
#         text = text.decode("utf-8")
#
#     # Text can also be a sequence of strings, in which case this method
#     # will return a sequence of results for each text.
#     result = translate_client.translate(text, target_language=target)
#
#     print(u"Text: {}".format(result["input"]))
#     print(u"Translation: {}".format(result["translatedText"]))
#     print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))
#     return result["translatedText"]
#
# translation = translate_text("en-US", "डोंबिवली मधील दोन कंपन्यांना मध्यरात्री लागली आग")
#
# from transformers import AutoTokenizer, AutoModelForTokenClassification
# from transformers import pipeline
# tokenizer = AutoTokenizer.from_pretrained("Davlan/distilbert-base-multilingual-cased-ner-hrl")
# model = AutoModelForTokenClassification.from_pretrained("Davlan/distilbert-base-multilingual-cased-ner-hrl")
# nlp = pipeline("ner", model=model, tokenizer=tokenizer)
# example = translation
# ner_results = nlp(example)
# print(ner_results)
#
# array = []
# for i in range(0, len(ner_results)):
#   if ner_results[i]['entity']=='B-LOC' or ner_results[i]['entity']=='I-LOC':
#     array.append((ner_results[i]['word']))
# print(array)
#
# nlp_string = ""
# for i in range(0,len(array)):
#   nlp_string=nlp_string + array[i]
# print(nlp_string)
#
# nlp_newstr = nlp_string.replace('#','')
# print(nlp_string)
#
#
# from transformers import pipeline
# def classipy(text):
#         classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
#         sequence_to_classify = text
#         candidate_labels = ['medical','fire','crime-in-progress','other']
#         return classifier(sequence_to_classify, candidate_labels)
# classipy_result = classipy(translation)
# class_result = (classipy_result['labels'][0])
#
# def priority(text):
#         classifier1 = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
#         sequence_to_classify = text
#         candidate_labels = ['priority-low','priority-medium','priority-high']
#         return classifier1(sequence_to_classify, candidate_labels)
# priority_result = priority(translation)
# priority = (priority_result['labels'][0])
#
#
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from firebase_admin import firestore

cred = credentials.Certificate("/Users/shubhammojidra/Desktop/operatorai/sankatrakshakai-firebase-adminsdk-145w3-6366ed8c8c.json")
firebase_admin = firebase_admin.initialize_app(cred, {'databaseURL': 'https://sankatrakshakai-default-rtdb.firebaseio.com'})

import os
credential_path = "/Users/shubhammojidra/Desktop/operatorai/auth.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

def transcribe_file(speech_file, lang_code):
    """Transcribe the given audio file."""
    # from google.cloud import speech
    from google.cloud import speech_v1p1beta1 as speech
    import io

    client = speech.SpeechClient()

    with io.open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.MP3,
        sample_rate_hertz=16000,
        language_code=lang_code,
    )

    response = client.recognize(config=config, audio=audio)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        return result.alternatives[0].transcript

text = transcribe_file("anwesha_marathi.mp3","mr-IN")



def translate_text(target, text):
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    import six
    from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)

    print(u"Text: {}".format(result["input"]))
    print(u"Translation: {}".format(result["translatedText"]))
    print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))
    return result["translatedText"]

translation = translate_text("en-US",text)

from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
tokenizer = AutoTokenizer.from_pretrained("Davlan/distilbert-base-multilingual-cased-ner-hrl")
model = AutoModelForTokenClassification.from_pretrained("Davlan/distilbert-base-multilingual-cased-ner-hrl")
nlp = pipeline("ner", model=model, tokenizer=tokenizer)
example = translation
ner_results = nlp(example)
print(ner_results)

array = []
for i in range(0, len(ner_results)):
  if ner_results[i]['entity']=='B-LOC' or ner_results[i]['entity']=='I-LOC':
    array.append((ner_results[i]['word']))
print(array)

nlp_string = ""
for i in range(0,len(array)):
  nlp_string=nlp_string + array[i]
print(nlp_string)

nlp_newstr = nlp_string.replace('#','')
print(nlp_newstr)



from transformers import pipeline
def classipy(text):
        classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
        sequence_to_classify = text
        candidate_labels = ['medical','fire','crime-in-progress','other']
        return classifier(sequence_to_classify, candidate_labels)
classipy_result = classipy(translation)
class_result = (classipy_result['labels'][0])
print(class_result)

def priority(text):
        classifier1 = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
        sequence_to_classify = text
        candidate_labels = ['priority-low','priority-medium','priority-high']
        return classifier1(sequence_to_classify, candidate_labels)
priority_result = priority(translation)
priority = (priority_result['labels'][0])
print(priority)


dict = {
    "Translation": translation,
    "Location": nlp_newstr,
    "Priority": priority,
    "Emergency": class_result
    }
