import logging
import azure.functions as func
import os
import requests

from .luis import get_luis
from .search import get_search

def main(req: func.HttpRequest) -> func.HttpResponse:

    req_body = req.get_json()
    text = req_body.get('text').lower()
    luis_response = get_luis(text)
    search_response = get_search(text)
    #logging.info(luis_response)
    
    return func.HttpResponse(f"Hello, your said: {text}. The intent in LUIS is: {luis_response}. The search result is : {search_response}")

