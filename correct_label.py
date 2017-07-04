#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import dataset
"""

db='sqlite:///nex-analysis.db'
database = dataset.connect(db)
entities=list(database.query("select label, entity_id, uri from entity where label='Leiden'"))
print(len(entities))
entity_db=database["entity"]
for item in entities:
    label=item["label"]
    print(label)
    entity_id=item["entity_id"]
    print(entity_id)
    uri=item["uri"]
    print(uri)
    if label== "Leiden" and uri=="":
        print("marker")
        entity_db.update(dict(
                        label=entity_id,
                        entity_id=entity_id
                    ),["entity_id"])
                """

db='sqlite:///nex-analysis.db'
database = dataset.connect(db)
entities=list(database.query("select uri, labelfromsurface, entity_id from entity where labelfromsurface=1"))
entity_db=database["entity"]
for item in entities:
    uri=item["uri"]
    entity_id=item["entity_id"]
    print(entity_id)
    labelfromsurface=item["labelfromsurface"]
    print(labelfromsurface)
    if labelfromsurface==1 and uri!="":
        print("marker")
        entity_db.update(dict(
                      labelfromsurface=0,
                        entity_id=entity_id
                    ),["entity_id"])