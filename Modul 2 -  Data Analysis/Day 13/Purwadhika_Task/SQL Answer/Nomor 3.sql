select country.name as negara, countrylanguage.Percentage
from country
join countrylanguage on country.Code = countrylanguage.CountryCode
where Language = 'Spanish'
order by 2 DESC
limit 10
