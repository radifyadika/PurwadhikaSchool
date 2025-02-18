select distinct Continent, sum(Population) as Total_Populasi
from country
group by 1
having SUM(population) > 700000000