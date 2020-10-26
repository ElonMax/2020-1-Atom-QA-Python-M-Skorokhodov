#!/usr/bin/env python3
import json
import os
from collections import Counter


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
        if '50' in requests[i][1] or '51' in requests[i][1]:
            err_req.append(str(requests[i]))
    data = Counter(err_req)
    res = sorted(data, key=len, reverse=True)

    file_python.write('--TOP server error:\n')
    for i in range(10):
        file_python.write(str((res[i], data[res[i]])) + '\n')
    file_python.write('\n')

    server_dict = {'--TOP server error': {i+1: str((res[i], data[res[i]])) for i in range(10)}}
    file_json = open(tracejson, 'a')
    json.dump(server_dict, file_json, indent=4)
    file_json.write('\n')
    file_json.close()

    file_python.close()
except FileNotFoundError:
    print('No logs found for top_server_error.py')
