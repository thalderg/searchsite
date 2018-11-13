# searchsite  
Django search-only app for elasticsearch.  
This app is referencing the account.json test file to perform the search functionalities, you can download it from here:  
https://raw.githubusercontent.com/elastic/elasticsearch/master/docs/src/test/resources/accounts.json.  
To test it you can use the elasticsearch version 6.3.1 inside the esearch app folder or download your own version.  
It uses django version 2.0.6.  
You will need to install the following python3 libraries to communicate with the elasticsearch RESTful API using es_call.py:    
$ pip install elasticsearch  
$ pip install elasticsearch-dsl  

more details on:  
http://myitpie.com/how-to-create-a-django-search-only-app-for-elasticsearch-part-1/  
http://myitpie.com/how-to-create-a-django-search-only-app-for-elasticsearch-part-2/ 
