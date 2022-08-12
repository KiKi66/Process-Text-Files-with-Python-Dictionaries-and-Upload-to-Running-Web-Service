#!/usr/bin/env python3
import os
import requests

#feedback dir
path_fb = "/data/feedback/"

#create feedback dictionary and its key
fb = {}
key_fb = ["title", "name", "date", "feedback"]

#reading through all of the feedbacks and pushing them to the website
for file in os.listdir(path_fb):
  if file.endswith(".txt"):
    key_num = 0
    with open(path_fb + file) as fb_file:
      for line in fb_file:
        content = line.strip()
        fb[key_fb[key_num]] = content
        key_num += 1
      response = requests.post("http://35.226.238.194/feedback/", json=fb)

print(response.request.body)
print(response.status_code)
