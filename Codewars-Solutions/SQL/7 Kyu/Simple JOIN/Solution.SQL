SELECT P.*, C.name AS company_name
FROM products P
JOIN companies C
  ON C.id = P.company_id