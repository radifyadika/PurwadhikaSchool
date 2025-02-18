select film.title, category.name, film.length from film
join film_category on film.film_id = film_category.film_id
join category on film_category.category_id = category.category_id
where category.name = 'Comedy'
order by 3 ASC
limit 10
