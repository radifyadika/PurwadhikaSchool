select country.name as nama, GNP
from country
where Continent = 'Asia' and GNP > 
	(select avg(GNP)
	from country where Continent = 'Europe')
Order by 2 desc