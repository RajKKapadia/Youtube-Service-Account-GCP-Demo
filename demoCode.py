from google.cloud import translate_v2 as translate

import os, json

from dotenv import load_dotenv
load_dotenv()

CREDENTIALS = json.loads(os.environ.get('CREDENTIALS'))

if os.path.exists('credentials.json'):
    pass
else:
    with open('credentials.json', 'w') as credFile:
        json.dump(CREDENTIALS, credFile)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'credentials.json'

translateClient = translate.Client()

# Detect the language
detectedRes = translateClient.detect_language('muraho nshuti')

print(detectedRes)

# Translate language
transRes = translateClient.translate('muraho nshuti', 'en')

print(transRes)