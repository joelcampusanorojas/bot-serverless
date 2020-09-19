import logging
import azure.functions as func

import requests

from .luis import luis

from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

#from azure.identity import DefaultAzureCredential
#from azure.keyvault.secrets import SecretClient
keyVaultName = "bot-serverless-vault"
KVUri = f"https://{keyVaultName}.vault.azure.net"

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    '''
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=KVUri, credential=credential) 
    secretName = "luis-app-id"
    print(client)
    retrieved_secret = client.get_secret(secretName)
    logging.info(f"Retrieving your secret from {retrieved_secret}.")
    '''
    req_body = req.get_json()
    text = req_body.get('text').lower()
    '''
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
    '''
    #print(luis(text))
    logging.info(luis(text))

    return func.HttpResponse(f"Hello, your said: {text}.")
