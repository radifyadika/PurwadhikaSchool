select country.name as negara, GNP, city.name as nama_kota, city.Population, countrylanguage.Language
from country
join countrylanguage on country.Code = countrylanguage.CountryCode
join city on country.Code = city.CountryCode
where country.name ='Indonesia' and city.ID = country.Capital and countrylanguage.IsOfficial = 'T'

select *
from country
join countrylanguage on country.Code = countrylanguage.CountryCode