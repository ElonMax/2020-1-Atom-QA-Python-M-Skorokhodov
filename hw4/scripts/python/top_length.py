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
    requests = [str([all_requests[i].split(' ')[6], all_requests[i].split(' ')[8]]) for i in range(len(all_requests))]
    data = Counter(requests)
    res = sorted(data, key=len, reverse=True)

    file_python.write('--TOP request`s length:\n')
    for i in range(10):
        file_python.write(str((res[i], data[res[i]])) + '\n')
    file_python.write('\n')

    length_dict = {'--TOP request`s length': {i+1: str((res[i], data[res[i]])) for i in range(10)}}
    file_json = open(tracejson, 'a')
    json.dump(length_dict, file_json, indent=4)
    file_json.write('\n')
    file_json.close()

    file_python.close()
except FileNotFoundError:
    print('No logs found for top_length.py')
