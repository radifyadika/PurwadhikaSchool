with World_Population as
	(select sum(population) as Total_Population from country),
    
Index_country as
	(select ROW_NUMBER() OVER () AS RowIndex, name, GovernmentForm, Population, 
    (select Total_Population from World_Population) as World_Population,
    (Population / (select Total_Population from World_Population) * 100) as Pop_percentage from country)
    
select name, GovernmentForm, World_Population, Pop_percentage, RowIndex from Index_country
order by 4 desc
limit 10




