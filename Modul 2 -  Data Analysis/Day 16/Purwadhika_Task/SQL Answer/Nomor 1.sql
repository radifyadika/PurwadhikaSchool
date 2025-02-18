select Country.name as CountryName, Count(distinct language) as TotalLanguage from country
join countrylanguage on country.Code = countrylanguage.CountryCode
group by 1
having TotalLanguage >
	(select avg(language)
    from countrylanguage)
order by 2 desc, 1 desc
limit 10