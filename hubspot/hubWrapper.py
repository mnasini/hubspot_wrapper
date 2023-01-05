from . import session

class hubWrapper:
    def __init__(self):
        self.token=session.params['token']
        pass
    def info(self):
        path= 'https://api.hubapi.com/crm/v3/objects/contacts?limit=10&archived=false'
        session.headers.update({"Authorization": "Bearer {}".format(self.token)})
        response = session.get(path)
        return response.json()