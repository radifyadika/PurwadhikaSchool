select category.name as kategori, 
	Count(distinct film_category.film_id) as JumlahMovie, 
    avg(film.rental_rate) as RataHargaSewa
from film
join film_category on film.film_id = film_category.film_id
join category on film_category.category_id = category.category_id
Group by 1
order by 2 DESC
