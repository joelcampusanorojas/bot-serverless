########### Python 3.6 #############

#
# This quickstart shows how to predict the intent of an utterance by using the LUIS REST APIs.
#

import requests
import logging
import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

keyVaultName = "bot-serverless-vault"
KVUri = f"https://{keyVaultName}.vault.azure.net"


def luis(text):
    try:
        ##########
        # Values to modify.

        # YOUR-APP-ID: The App ID GUID found on the www.luis.ai Application Settings page.
        appId = get_vault('luis-app-id')
        # YOUR-PREDICTION-KEY: Your LUIS authoring key, 32 character value.
        prediction_key = get_vault('luis-key')

        # YOUR-PREDICTION-ENDPOINT: Replace with your authoring key endpoint.
        # For example, "https://westus.api.cognitive.microsoft.com/"
        prediction_endpoint = 'https://westus.api.cognitive.microsoft.com/'

        # The utterance you want to use.
        utterance = text
        ##########

        # The headers to use in this REST call.
        headers = {
        }

        # The URL parameters to use in this REST call.
        params ={
            'query': utterance,
            'timezoneOffset': '0',
            'verbose': 'true',
            'show-all-intents': 'true',
            'spellCheck': 'false',
            'staging': 'false',
            'subscription-key': prediction_key
        }

        # Make the REST call.
        response = requests.get(f'{prediction_endpoint}luis/prediction/v3.0/apps/{appId}/slots/production/predict', headers=headers, params=params)

        # Display the results on the console.
        print(response.json())
        return(response.json())

    except Exception as e:
        # Display the error string.
        print(f'{e}')


def get_vault(secretName):
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=KVUri, credential=credential) 
    retrieved_secret = client.get_secret(secretName)
    #logging.info(f"Retrieving your secret from {retrieved_secret.value}.")
    return(retrieved_secret.value)
