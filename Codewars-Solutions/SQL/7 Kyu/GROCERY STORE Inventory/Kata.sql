SELECT
	ID,
	NAME,
	STOCK
FROM
	PRODUCTS
WHERE
	STOCK < 3 and
	PRODUCENT = 'CompanyA'
ORDER BY 
  	ID