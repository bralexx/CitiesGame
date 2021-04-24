from flask import Flask, jsonify, request, redirect
import logging

import json

all_cities = json.load(open("cities/world-cities_json.json", 'r'))

dictionary = {}
for city in all_cities:
    if city['name'][0] in dictionary:
        dictionary[city['name'][0]] += [{city['name'], city['country']}]
    else:
        dictionary.update({city['name'][0]:[{city['name'], city['country']}]})
print(dictionary)