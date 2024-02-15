--  lists all cities contained in the database hbtn_0d_usa
SELECT cities.name, cities.id, states.name FROM cities
JOIN states ON cities.state_id = state.id
ORDER BY cities.id
