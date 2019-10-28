# from googletrans import Translator
#
# translator = Translator(service_urls=[
#       'translate.google.com'
#     ])
#
# translator.translate('안녕하세요.')
#
# translator.translate('안녕하세요.', dest='ja')
#
# translator.translate('veritas lux mea', src='la')



# Imports the Google Cloud client library
from google.cloud import translate

# Instantiates a client
translate_client = translate.Client()

# The text to translate
text = u'Hello, world!'
# The target language
target = 'ru'

# Translates some text into Russian
translation = translate_client.translate(
    text,
    target_language=target)

print(u'Text: {}'.format(text))
print(u'Translation: {}'.format(translation['translatedText']))