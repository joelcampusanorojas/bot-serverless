#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import http.client, urllib.parse, json, time
import json
import requests
import logging

def get_search(question):
    try:

        host = 'bot-serverless-search.search.windows.net'
        endpoint_key = '7C9CB5854474711F77CF30D385BEF4BC'
        api_version = '2020-06-30'
        path = '/indexes/cosmosdb-index/'

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
        url = path + 'docs?' + params

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
