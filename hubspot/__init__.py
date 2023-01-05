import os
import requests
#get the token as environment variable
token = os.environ.get('token', None)
#check if a token is present(by default for the sake of the exercise i inserted it in the env file)
if token is None:
    raise Exception("invalid api key, see https://developers.hubspot.com/docs/api/crm/contacts for informations"
    )
session = requests.Session()
session.params = {}
#save the token in a session variable to be always available for each api call
session.params['token'] = token



from .hubWrapper import hubWrapper