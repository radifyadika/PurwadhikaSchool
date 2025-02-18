select country.continent, COUNT(country.continent) as jumlah_negara
from country
group by 1
having COUNT(country.continent) > (
	select COUNT(country.continent)
	from country
	where country.continent ='North America')

