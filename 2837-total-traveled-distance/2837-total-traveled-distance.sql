# Write your MySQL query statement below
SELECT u.user_id, u.name, IFNULL(sum(r.distance), 0) AS 'traveled distance'
from Users u
LEFT JOIN Rides r
ON u.user_id = r.user_id
GROUP BY
u.user_id, u.name
order by
u.user_id ASC;
