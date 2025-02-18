select Continent, Region, Count(city.name) as number_of_city, 
	ROW_NUMBER() OVER (PARTITION BY continent)  AS Row_Group from country
join city on country.Code = city.CountryCode
where continent in ('Asia', 'Europe')
group by 1,2
order by 1,4