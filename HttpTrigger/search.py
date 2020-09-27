#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import http.client, urllib.parse, json, time
import json
import requests
import logging

from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
keyVaultName = "bot-serverless-vault"
KVUri = f"https://{keyVaultName}.vault.azure.net"

def get_search(question):
    try:

        host = get_vault('search-host')
        endpoint_key = get_vault('search-key')
        api_version = get_vault('search-api-version')
        index = get_vault('search-index')

        question = question.lower()
        
        answer = ''
        #score = 0

        headers = {
            'api-key': endpoint_key,
            'Content-Type': 'application/json',
        }

        content = {
        "api-version": api_version,
        "queryType": "simple",
        "search": question,
        "$top": 1,
        "orderby": "Rating desc"
        }

        payload = ''
        params = urllib.parse.urlencode(content)
        url = index + 'docs?' + params

        conn = http.client.HTTPSConnection(host)
        conn.request("GET", url, payload, headers)
        response = conn.getresponse()
        
        
        answer = ''
        if(response.status == 200):
            result_json = response.read()
            result_json = json.loads(result_json)
            value = result_json["value"]
            
            if(len(value) > 0):
                value = value[0]
                #score = value["@search.score"]
                #question = value["questions"]
                answer = value["answer"]

        answer = str(answer)
        return (answer)

    except Exception as e:
        # Display the error string.
        print(f'{e}')


def get_vault(secretName):
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=KVUri, credential=credential) 
    retrieved_secret = client.get_secret(secretName)
    return(retrieved_secret.value)
