import base64
import csv
import json
import os
import requests
import sys
import pprint

from jinja2 import Environment, FileSystemLoader, select_autoescape

# Init Jinja
jinja = Environment(
    loader=FileSystemLoader(["."]),
    autoescape=select_autoescape()
)
template = jinja.get_template('input/site.j2')
print(template.render())
