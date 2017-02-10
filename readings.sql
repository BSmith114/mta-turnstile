CREATE VIEW counts 
AS
	SELECT 
		r.station
		,r.linename
		,r."date"
		,r."time"
		,r.exits
		,r.entries
		,ABS(r.exits - LAG(r.exits, 1, r.exits) OVER (PARTITION BY r.ca || r.unit || r.scp ORDER BY r."date" ASC, r."time" ASC)) as diff_exits
		,ABS(r.exits - first_value(exits) OVER (PARTITION BY r.ca || r.unit || r.scp ORDER BY r."date" ASC,r."time" ASC)) as cum_exits
		,ABS(r.entries - LAG(r.entries, 1, r.entries) OVER (PARTITION BY r.ca || r.unit || r.scp ORDER BY r."date" ASC,r."time" ASC)) diff_entries
		,ABS(r.entries - first_value(entries) OVER (PARTITION BY r.ca || r.unit || r.scp ORDER BY r."date" ASC,r."time" ASC)) as cum_entries
	FROM readings r
	WHERE date_part('second', r."time") = 0
		AND date_part('minute', r."time") = 0;
	

select 
	c.station
	,c.linename
	,c."date"
	,c."time"
	,sum(diff_entries)
	,sum(cum_entries)
from counts c
where 
	station = 'BEDFORD AV'
group by
	c.station
	,c.linename
	,c."date"
	,c."time"
order by
	c."date"
	,c."time"