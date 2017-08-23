DROP VIEW if exists differences_view;
CREATE VIEW differences_view as 
	select
		erster.surface as surface, 
		entity_1.label as label_1, 
		entity_1.uri as uri_1, 
		tools_1.tool as tool_1, 
		entity_2.label as label_2, 
		entity_2.uri as uri_2, 
		tools_2.tool as tool_2, 
		(erster.start ||"_"|| erster.end) as id, 
		substr(dpa_text.dpa_id,20) as dpa_id 
	from 
		found_entities as erster,
		found_entities as zweiter,
		entity as entity_1,
		entity as entity_2,
		tools as tools_1,
		tools as tools_2,
		dpa_text
	where 
		erster.tool_id=tools_1.rowid and
		zweiter.tool_id=tools_2.rowid and
		erster.dpa_id=dpa_text.rowid and
		erster.entity_id=entity_1.rowid and 
		zweiter.entity_id=entity_2.rowid and 
		erster.entity_id != zweiter.entity_id and
		erster.tool_id > zweiter.tool_id and
		erster.start = zweiter.start and 
		erster.end = zweiter.end and
		erster.dpa_id = zweiter.dpa_id and
		uri_1 != "" and 
		uri_2 != "" 
	order by 
		dpa_id, erster.tool_id;
