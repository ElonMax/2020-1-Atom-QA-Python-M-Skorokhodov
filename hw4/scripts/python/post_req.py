#!/usr/bin/env python3
import os
import json


tracelog = os.path.join(os.path.abspath(''), '../../logs/access.log')
traceres = os.path.join(os.path.abspath(''), '../../results/file_python.log')
tracejson = os.path.join(os.path.abspath(''), '../../results/file_python.json')

try:
    log = open(tracelog)
    all_requests = list(log)
    log.close()

    file_python = open(traceres, 'a')
    post = len([i for i in all_requests if 'POST' in i])
    file_python.write('--Number of POST:\n' + str(post) + '\n\n')
    file_python.close()

    post_req_dict = {'--Number of post': post}
    file_json = open(tracejson, 'a')
    json.dump(post_req_dict, file_json)
    file_json.write('\n')
    file_json.close()

except FileNotFoundError:
    print('No logs found for post_req.py')
