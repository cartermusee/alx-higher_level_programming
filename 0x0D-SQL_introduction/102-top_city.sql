-- temperature limit
SELECT city,AVG(value) AS `avg_temp`
FROM temperatures LIMIT 3
GROUP BY city
ORDER BY `avg_temp` DESC;
