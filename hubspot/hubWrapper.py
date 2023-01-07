from . import session
import csv
import datetime
class hubWrapper:
    def __init__(self):
        self.token=session.params['token']
        pass
    def get_all_ids(self,export=False):     
        query_params = {'limit': '10', 'archieved':'false','properties':'email'}
        path= 'https://api.hubapi.com/crm/v3/objects/contacts'
        session.headers.update({"Authorization": "Bearer {}".format(self.token)})
        response = session.get(path,params=query_params)
        response_dict=response.json()["results"]
        final=list(map(lambda x: x["email"],list(map(lambda x: x["properties"],response_dict))))
        if (export):
            
            with open('list_customer_emails_{}.csv'.format(datetime.datetime.now()), 'w', newline='') as output_file:
                csv_writer = csv.writer(output_file)
                csv_writer.writerow(["email"])
                for i in final:
                    csv_writer.writerow([i])

        return final

        
    def get_customer(self,customer_id,params,export=False):
        query_params = {'archieved':'false','idProperty':'email','properties':params}
        if params == "all":
           query_params = {'limit': '10', 'archieved':'false','idProperty':'email'} 
        path= 'https://api.hubapi.com/crm/v3/objects/contacts/{}'.format(customer_id)
        session.headers.update({"Authorization": "Bearer {}".format(self.token)})
        response = session.get(path,params=query_params).json()
        for i in response["properties"]:
                response[i]=response["properties"][i]
        response.pop("properties")
        if(export):
            
            keys = response.keys()

            with open('export_single_customer_{}.csv'.format(datetime.datetime.now()), 'w', newline='') as output_file:
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writeheader()
                dict_writer.writerow(response)
        return response
    def get_customer_batch(self,customer_list_id,params,export=False):
        result=list()
        query_params = {'archieved':'false','idProperty':'email','properties':params}
        session.headers.update({"Authorization": "Bearer {}".format(self.token)})
        for i in customer_list_id:
            path= 'https://api.hubapi.com/crm/v3/objects/contacts/{}'.format(i)
            response = session.get(path,params=query_params).json()
            for i in response["properties"]:
                response[i]=response["properties"][i]
            response.pop("properties")
                
            result.append(response)
        if(export):
            keys = result[0].keys()

            with open('export_customer_batch_{}.csv'.format(datetime.datetime.now()), 'w', newline='') as output_file:
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(result)   
        return result

        
