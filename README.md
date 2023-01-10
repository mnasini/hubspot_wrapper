# wrapper for hubspot 
this code presents a python wrapper for some features of hubspot contacts api, as a personal point i would like to say that reading the hubspot documentation we see that a python wrapper for their apis has already been made by them, so for a professional point of view, is better to use their existing code, and integrate it with custom code if some specific features are required.

<b>this code however implements a wrapper from scratch.</b>


## instructions to use the wrapper
 for security reasons we are not hardcoding the credentials in the code, so as a first step is to insert your api key inside the file token.env

### Virtual environment and dependencies

    # install virtualenv
    python3.8 -m pip install virtualenv
    # create virtualenv
    virtualenv -p $(which python) venv
    # enter virtualenv
    source venv/bin/activate
    pip install -r requirements.txt
    #path setup to be run in your terminal
    export PYTHONPATH='.'
    # setup the environment variables (to avoid hardcoding credentials)
    export $(xargs < token.env)

### Importing the class


    from hubspot import hubWrapper
    
<b>important</b>: before importing the class on your project make sure that you put the folder : "hubspot" in the same parent folder of your project and that you have successfully setted up your token.env file, the file structure should be the same as the one of this repository (see a running example opening the tests folder (jupiter file))

### creation of the hubWrapper object


    wrapper=hubWrapper()
when creating the hubwrapper object the authentication will take place, and the auth token will be fetched from the environment variables, and it will be saved as a local sessions, to be reused by the program

### get all ids


    ids=wrapper.get_all_ids()
with this method we are fetching all the emails on the customers database, this is useful in case we want to see all the unique identifiers for our customers, it will return a list of emails.

To export this result we just have to send the parameter "export=true" :


    ids=wrapper.get_all_ids(True)
and a csv file with the emails will be exported.

### get single customer having the email

    customer=wrapper.get_customer(customer_id="email",params="all",history=False,export=False)

the parameters that we need to send are: 
* customer_id: unique identifier of a customer, his email
* params(as a list): the parameters that needs to get returned: 
     *  email: email of that user
     * firstname: the first name of the user 
     * lastname: last name of the users
     * "all" to indicate that we want all the parameters
* history: this is a boolean parameter that, if set to true, will return all the history (as lists) of the fetched values
* export, this is a boolean parameter, that, if set to true will save an export on a csv.


this method will return a  dictionary by of the result by default

### batch of customers 
    l=['email1', 'email2']
    customer=wrapper.get_customer_batch(l,params="all",history=False,export=False)
the parameters are quite similar to the explanation above for a single customer's method, the main difference is that now we are fetching data of multiple customers(customer_list_id), the returned value will be a list of dictionaries

n.b if you decide to export the results the resulting csv will have the name of the method used+ a timestamp of the time of the export

finally in the repository is possible to see a test file that will test all the method, the sample exports generated are present in the repository as well









