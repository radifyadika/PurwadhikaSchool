-- Tampilkan daftar negara-negara Asia yang memiliki angka harapan hidup lebih dari rata-rata 
-- angka harapan hidup negara-negara Eropa.

select country.name as nama, country.Continent as Benua , 
country.LifeExpectancy as AngkaHarapanHidup, GNP
from country
where Continent = 'Asia' and country.LifeExpectancy > 
	(select avg(LifeExpectancy) as avg_europe_lifeexpectancy
	from country where Continent = 'Europe')
Order by 3 desc
