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
        response_dict=response.json()["results"]
        return list(map(lambda x: x["email"],list(map(lambda x: x["properties"],response_dict))))

        
    def get_customer(self,customer_id,params):
        query_params = {'limit': '10', 'archieved':'false','idProperty':'email','properties':params}
        if params == "all":
           query_params = {'limit': '10', 'archieved':'false','idProperty':'email'} 
        path= 'https://api.hubapi.com/crm/v3/objects/contacts/{}'.format(customer_id)
        session.headers.update({"Authorization": "Bearer {}".format(self.token)})
        response = session.get(path,params=query_params)
        return response.json()
    def get_customer_batch(self):
        pass
    #to be implemented