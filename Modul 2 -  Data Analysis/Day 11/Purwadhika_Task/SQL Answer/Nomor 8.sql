select distinct Region, round(avg(GNP)) as Rata2_GNP
from country
group by 1
order by 2 DESC
limit 5
