select rating,
case
  when rating = 'G' then'General Audiences' when rating = 'PG' then 'Parental Guidance Suggested'
  when rating = 'PG-13' then 'Parental Guidance for Children Under 13' when rating = 'R' then 'Restricted'
  when rating = 'NC-17' then 'No Children Under 17 Admitted' 
  end as description,
Count(film_id) as movie_count
from film
group by 1
order by 1
