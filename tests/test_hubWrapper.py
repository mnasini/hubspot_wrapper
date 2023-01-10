from hubspot import hubWrapper


a=hubWrapper()
#getting all ids
print(a.get_all_ids(True))
#get single customer (and export it):
print(a.get_customer(customer_id="",params="all",history=False,export=True))
#get batch of customers (with only email as parameters)
l=['email1', 'email2']
print(a.get_customer_batch(customer_list_id=l,params=["email"],history=True,export=True))



