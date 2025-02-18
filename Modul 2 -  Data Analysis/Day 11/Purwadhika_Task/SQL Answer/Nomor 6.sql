select distinct Continent, sum(Population) as Total_Populasi
from country
where continent not in ('Oceania', 'Antarctica')
group by 1