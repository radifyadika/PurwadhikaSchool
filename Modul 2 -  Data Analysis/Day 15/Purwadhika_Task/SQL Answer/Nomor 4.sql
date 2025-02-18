select actor.actor_id, actor.first_name, actor.last_name, 
count(distinct film.film_id) as jumlah_Movie 
from film
join film_actor on film.film_id = film_actor.film_id
join actor on film_actor.actor_id = actor.actor_id
group by 1
order by 4 desc,1 desc
limit 10