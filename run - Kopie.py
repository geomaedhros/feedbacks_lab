#! /usr/bin/env python3

import os
import requests
import ast

# List all .txt files under /data/feedback directory that contains the
# actual feedback to be displayed on the company's website.

# directory contents
# set path 
path = '/data/feedback'

feedback_dict = {}

# list "path" contents
for content in os.listdir(path):
    split_txt = os.path.splitext(content)
        # list only .txt files
    if split_txt[1] == ".txt":
        with open(os.path.join(path, content), "r") as feedback_file:

            # convert data to dictionary
            feedback_dict['title'] =    feedback_file.readline().strip("\n")
            feedback_dict['name'] =     feedback_file.readline().strip("\n")
            feedback_dict['date'] =     feedback_file.readline().strip("\n")
            feedback_dict['feedback'] = feedback_file.readline().strip("\n")

            post_req = requests.post('http://35.193.52.81/feedback/', data = feedback_dict)
            if post_req.raise_for_status() != None:
                print(post_req.raise_for_status())

