select name as Negara, GNP
from country
join countrylanguage on country.Code = countrylanguage.CountryCode
where Language = 'English' and IsOfficial = 'T' and Percentage > 50
Order by 2 Desc
limit 5