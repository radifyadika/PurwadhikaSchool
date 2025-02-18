select city.name as nama_kota , country.name as negara, city.Population
from country
join city on country.Code = city.CountryCode
order by 3 Desc
limit 10