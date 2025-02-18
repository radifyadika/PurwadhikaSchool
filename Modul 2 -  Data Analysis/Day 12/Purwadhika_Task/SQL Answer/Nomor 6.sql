select country.name as Negara , country.Population as Populasi, 
GNP , city.name as Ibu_Kota, city.Population As Populasi_Ibukota
from country
join city on country.Code = city.CountryCode
where region= 'Southeast Asia' and city.ID = country.Capital
Order by 1 ASC


-- select * from city
-- where CountryCode = 'BRN'
-- where region= 'Southeast Asia'
-- join city
-- where country.name = 'Indonesia' and District = 'Sumatera Utara'


