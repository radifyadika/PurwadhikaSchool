select name
from country
join countrylanguage on country.Code = countrylanguage.CountryCode
where Language = 'English' and IsOfficial = 'T' 
Order by Percentage Desc
limit 7



