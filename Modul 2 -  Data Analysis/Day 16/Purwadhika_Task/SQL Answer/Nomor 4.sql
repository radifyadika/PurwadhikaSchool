select Continent, sum(city.population) as Total_Capital_Population, 
	avg(country.GNP) as Average_GNP,
	RANK() OVER (order by SUM(city.Population) desc) as Rank_Population,
    RANK() OVER (order by avg(country.GNP) desc) as Rank_GNP 
    from country 
join city on country.Capital = city.ID
group by 1
order by 4

-- Berdasarkanquery, fokus utama pemasaran produk perusahaan sebaiknya diarahkan ke Eropa dan Asia, diikuti oleh Amerika Utara.

-- Eropa: Kombinasi dari rata-rata GNP tinggi dan populasi ibu kota besar membuatnya menjadi target utama.
-- Asia: Populasi ibu kota yang sangat besar dan rata-rata GNP yang cukup tinggi menjadikannya pasar yang sangat potensial.
-- Amerika Utara: Meskipun populasinya lebih kecil, GNP rata-rata tertinggi menunjukkan daya beli yang kuat.
