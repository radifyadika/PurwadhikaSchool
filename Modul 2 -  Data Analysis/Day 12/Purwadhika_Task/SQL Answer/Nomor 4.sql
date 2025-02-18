select city.name as nama_kota , city.District as Provinsi, country.name as negara, city.Population
from country
join city on country.Code = city.CountryCode
where country.name = 'Indonesia'
Order by 3 Desc
limit 10