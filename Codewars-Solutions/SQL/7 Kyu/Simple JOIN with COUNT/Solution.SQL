Select P.*, COUNT(T) AS toy_count
FROM people P
JOIN toys T
  ON T.people_id = P.id
GROUP BY P.id;