select actor.actor_id, actor.first_name, actor.last_name, count(film.film_id) as jumlah_Movie from film

join film_actor on film.film_id = film_actor.film_id
join actor on film_actor.actor_id = actor.actor_id
join film_category on film.film_id = film_category.film_id
join category on film_category.category_id = category.category_id

where category.name = 'Horror'
group by 1
order by 4 desc
limit 10
