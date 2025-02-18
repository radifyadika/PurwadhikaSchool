select count(Distinct country.region) as jumlah_region, country.Continent
from country
where continent like '%a' 
group by 2
having count(distinct country.region) >
	(select count(distinct country.region)
	from country where Continent = 'Asia')