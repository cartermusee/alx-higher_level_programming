-- cities by states
SELECT id,name,name
FROM cities
JOIN states
ON cities.state_id = states.id
ORDER BY cities.id ASC
