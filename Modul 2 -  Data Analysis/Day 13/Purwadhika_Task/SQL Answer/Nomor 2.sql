-- Tampikan GNP negara Belanda (Netherlands), ibukota, beserta populasi dari
-- ibukotanya

select country.name as negara, GNP, city.name as nama_kota, city.Population
from country
join city on country.Code = city.CountryCode
where country.name ='Netherlands' and city.ID = country.Capital

select * from country
join city