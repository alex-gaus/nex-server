import dataset
def top_entities(dpa_id):
    dpa_id = dpa_id.replace("v-","/")
    #dpa_id="urn:newsml:dpa.com:20090101:170319-99-722478/2"
    db='sqlite:///nex-analysis.db'
    database = dataset.connect(db)
    dpa_id_id=list(database.query("select rowid from dpa_text where dpa_id=:dpa_id",dpa_id=dpa_id))[0]["rowid"]
    top_entities_list=list(database.query("""
        select label 
        from top_entities 
        where dpa_id=:dpa_id_id 
        order by score desc
        """,
        dpa_id_id=dpa_id_id))
    counter=1
    top_entities_final=[]
    for item in top_entities_list:
        item="".join([str(counter),". ",str(item["label"])])
        top_entities_final.append(item)
        counter=counter+1
    return(top_entities_final)
