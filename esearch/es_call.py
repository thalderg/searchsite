from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q



def esearch(firstname="", gender=""):
	client = Elasticsearch()
	q = Q("bool", should=[Q("match", firstname=firstname), 
	Q("match", gender=gender)], minimum_should_match=1)
	s = Search(using=client, index="bank").query(q)[0:20]
	response = s.execute()
	#print("%d hits found." % response.hits.total)
	search = get_results(response)
	return search


def get_results(response):
	results = []
	for hit in response:
		result_tuple = (hit.firstname + ' ' + hit.lastname, hit.email, hit.gender, hit.address)
		results.append(result_tuple)
	return results

# to test the search on the "bank index"
if __name__ == '__main__':
    print("Opal guy details:\n", esearch(firstname = "opal"))
    print("the first 20 f gender details:\n", esearch(gender = "f"))	
