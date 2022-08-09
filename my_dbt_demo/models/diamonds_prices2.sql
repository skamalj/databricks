select color, avg(price) as price
from dbt.diamonds
group by color
order by price desc