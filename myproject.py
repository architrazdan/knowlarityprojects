from flask import Flask
from flask import request
import json
import requests
application = Flask(__name__)
import logging
import sys
import traceback
from flask import Response
import urllib2

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler

handler = logging.FileHandler('arya.log')
handler.setLevel(logging.INFO)

# create a logging format

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger

logger.addHandler(handler)

@application.route("/", methods=['GET','POST'])
def hello():
    logger.info("test loggin")
    logger.info(request.data)
    logger.info(request.form)
    logger.info(request.values)
    logger.info(request.args)
    logger.info(request.query_string)
    if request.data:
        query_value = json.loads(request.data)['text']
        if query_value:
            query_value = query_value
            query_dict = {"query": query_value} if query_value else {"query":"holiday?"}
            headers = {'Content-Type': 'application/json'}
            response = requests.post('http://console.arya.ai/api/v2/faq/query?access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE0ODk5MjA4OTQ0ODJ9.CidrYnV1NtJ7hrrjbNIROQ_2WqM2dPGOn1YLWqA9jMI&m_key=new_bot_module&app=bot_new_new',data=query_dict).content
            val = json.loads(response)
	    val = val['answer']
            final_response = Response(val, mimetype='text/plain')
            return final_response
    else:
        return "{response:error}"

if __name__ == "__main__":
    application.run(host='0.0.0.0', port='8000')
                                                                                                                                                                                                          
                                                    
