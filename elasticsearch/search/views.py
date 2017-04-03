from django.shortcuts import render
from datetime import datetime
from elasticsearch import Elasticsearch
import json
es = Elasticsearch()

# Create your views here.

def index(request):
    render(request, 'search.html', {'object': ['bar','foo']})
    if request.method == 'GET':
        #todo searchbox get method
        search_query = request.GET.get('search_box', 'japanese resaurant')
        #todo query string
        res = es.search(index="testvenue", body={"query": {"query_string": {"query":search_query}}}) 
        ls = []
        #todo return random 10 results
        for hit in range(len(res['hits']['hits'])):
           ls.append(res['hits']['hits'][hit]['_source']['venue'])

        #todo empty element
        c = {'content':ls}
        return render(request, 'search.html', c)



