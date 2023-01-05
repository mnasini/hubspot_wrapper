import os
import requests

token = os.environ.get('HUBSPOT_TOKEN', None)

if token is None:
    raise Exception("invalid api key, see https://developers.hubspot.com/docs/api/crm/contacts for informations"
    )
session = requests.Session()
session.params = {}
session.params['token'] = token



from .hubWrapper import hubWrapper