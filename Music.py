__author__ = 'nvishwakarma'

import json
import requests

BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"






def query_by_name(url, parms, name):
    parms["query"] = "artist:" + name
    return query_site(url, parms)


def main():
    results = query