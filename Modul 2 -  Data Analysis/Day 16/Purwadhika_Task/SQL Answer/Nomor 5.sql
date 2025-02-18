with Total_GNP as (
    select SUM(GNP) as total_gnp from country),
GNP_Percentage as (
    select name as Country_name, ROUND(GNP / (Select total_gnp from Total_GNP) * 100, 2) as GNP_Percentage,
	ROW_NUMBER() OVER (order by GNP desc) as Rank_GNP from country)
    
select
    GNP1.Country_name, GNP1.GNP_Percentage, SUM(GNP2.GNP_Percentage) as cumulative_GNP , GNP1.Rank_GNP,
    NTILE(4) OVER (ORDER BY GNP1.Rank_GNP) as Market_Priority_1234
from GNP_Percentage as GNP1
join GNP_Percentage as GNP2 ON GNP1.Rank_GNP >= GNP2.Rank_GNP
group by 1,2
having cumulative_GNP <= 81
order by 2 desc
