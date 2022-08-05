select distinct color
from {{ ref('diamonds_four_cs') }}
sort by color asc