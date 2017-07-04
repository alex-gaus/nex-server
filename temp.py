#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""This functions gives the category 'person','location','organisation' or 'None' from the wikidata uri"""
import urllib.parse
import urllib.request
import requests
import xml
import dataset

session=requests.session()

uri="Q30"

person_query=dict(query="""
    ASK { wd:%(uri)s wdt:P31/wdt:P279* wd:Q5, wd:Q215627}
    """%locals())
response_person = session.get("https://query.wikidata.org/bigdata/namespace/wdq/sparql",params=person_query)
text_person=response_person.text
y_person=text_person.find("true")
if y_person > -1:
    print("Person")


location_query=dict(query="""
    ASK { wd:%(uri)s wdt:P31/wdt:P279* wd:Q1496967, wd:Q618123, wd:Q82794, wd:Q2221906, wd:Q5107 }
"""%locals())
response_location=session.get("https://query.wikidata.org/bigdata/namespace/wdq/sparql",params=location_query)
text_location=response_location.text
y_location=text_location.find("true")
if y_location > -1:
    print("Location")


organisation_query=dict(query="""
    ASK { wd:%(uri)s wdt:P31/wdt:P279* wd:Q43229}
"""%locals())
response_organisation = session.get("https://query.wikidata.org/bigdata/namespace/wdq/sparql",params=organisation_query)
text_organisation=response_organisation.text
y_organisation=text_organisation.find("true")
if y_organisation > -1:
    print("Organisation")
