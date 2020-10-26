#!/usr/bin/env python3
import os
from collections import Counter
import json


tracelog = os.path.join(os.path.abspath(''), '../../logs/access.log')
traceres = os.path.join(os.path.abspath(''), '../../results/file_python.log')
tracejson = os.path.join(os.path.abspath(''), '../../results/file_python.json')

try:
    log = open(tracelog)
    all_requests = list(log)
    log.close()

    file_python = open(traceres, 'a')
    requests = [[all_requests[i].split(' ')[6], all_requests[i].split(' ')[8], all_requests[i].split(' ')[0]] for i in range(len(all_requests))]
    err_req = []
    for i in range(len(requests)):
        if '40' in requests[i][1] or '41' in requests[i][1]:
            err_req.append(str(requests[i]))
    res = Counter(err_req).most_common(10)

    file_python.write('--TOP client error:\n')
    for i in range(10):
        file_python.write(str(res[i]) + '\n')
    file_python.write('\n')
    file_python.close()

    client_dict = {'--TOP client error': {i+1: str(res[i]) for i in range(10)}}
    file_json = open(tracejson, 'a')
    json.dump(client_dict, file_json, indent=4)
    file_json.write('\n')
    file_json.close()

except FileNotFoundError:
    print('No logs found for top_client_error.py')
