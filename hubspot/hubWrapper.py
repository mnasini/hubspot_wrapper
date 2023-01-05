from . import session

class hubWrapper:
    def __init__(self):
        self.token=session.params['token']
        pass
    def get_all_ids(self):     #add params list (to be apended for custom getter)
        query_params = {'limit': '10', 'archieved':'false','properties':'email'}
        path= 'https://api.hubapi.com/crm/v3/objects/contacts'
        session.headers.update({"Authorization": "Bearer {}".format(self.token)})
        response = session.get(path,params=query_params)
        return response.json()