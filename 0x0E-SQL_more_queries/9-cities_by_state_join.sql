-- List all cities in database hbtn_0d_usa
-- display cities.id - cities.name - states.name
SELECT cities.id, cities.name, states.name
FROM cities JOIN states
ON cities.state_id = states.id;
