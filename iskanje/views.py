from django.shortcuts import render_to_response
from django.template.context import RequestContext
from iskanje.search import query_for_id, query_texts

def search(request):
	results = {}
	if request.method == "POST":
		if request.POST["query"]:
			results = _get_search_results(request.POST["query"])
			# TODO: check results for none and give error
	return render_to_response('search/search.html', RequestContext(request, results))

def _get_search_results(query):
	results = {}
	try:
		results["osebe"] = query_for_id(query, type="oseba")["documents"]
		results["stranke"] = query_for_id(query, type="stranka")["documents"]
		results["zasedanja"] = query_texts(query, "zasedanje", facet=True)["documents"]
		results["zapisi"] = query_texts(query, "zapis", highlight=True, facet=True)["documents"]
	except: # TODO: limit exception
		return None

	return results