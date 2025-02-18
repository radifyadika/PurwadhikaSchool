select category.name as kategori, count(film.film_id) as jumlah_movie from film
join film_actor on film.film_id = film_actor.film_id
join actor on film_actor.actor_id = actor.actor_id
join film_category on film.film_id = film_category.film_id
join category on film_category.category_id = category.category_id
where actor.first_name = 'GINA' and actor.last_name = 'DEGENERES'
group by 1

