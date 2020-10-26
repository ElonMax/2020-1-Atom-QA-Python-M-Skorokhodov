#!/usr/bin/env python3
import os
import json


tracelog = os.path.join(os.path.abspath(''), '../../logs/access.log')
traceres = os.path.join(os.path.abspath(''), '../../results/file_python.log')
tracejson = os.path.join(os.path.abspath(''), '../../results/file_python.json')

try:
    log = open(tracelog)
    all_requests = len(list(log))
    log.close()

    file_python = open(traceres, 'a')
    file_python.write('--Number of requests:\n' + str(all_requests) + '\n\n')
    file_python.close()

    all_req_dict = {'--Number of requests': all_requests}
    file_json = open(tracejson, 'a')
    json.dump(all_req_dict, file_json)
    file_json.write('\n')
    file_json.close()

except FileNotFoundError:
    print('No logs found for all_req.py')
