# searchsite  
Django search-only app for elasticsearch.  
This app is referencing the account.json test file to perform the search functionality:  
https://raw.githubusercontent.com/elastic/elasticsearch/master/docs/src/test/resources/accounts.json.  
To test it you can use the elasticsearch version 6.3.1 inside the esearch app folder or download your own.  
It uses django version 2.0.6.  
You will need to install the following python3 libraries to communicate with the elasticsearch RESTful API using es_call.py:    
$ pip install elasticsearch  
$ pip install elasticsearch-dsl  

more details on http://myitpie.com/2018/09/20/how-to-create-a-django-search-only-app-for-elasticsearch-part-1/  

