import logging
import azure.functions as func
import os
import requests

from .luis import luis

def main(req: func.HttpRequest) -> func.HttpResponse:

    req_body = req.get_json()
    text = req_body.get('text').lower()
    luis_response = luis(text)
    #logging.info(luis_response)
    
    return func.HttpResponse(f"Hello, your said: {text}. The intent in LUIS is: {luis_response}.")

