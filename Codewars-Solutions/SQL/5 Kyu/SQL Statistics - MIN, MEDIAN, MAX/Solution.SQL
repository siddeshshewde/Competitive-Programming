SELECT
  MIN(score) AS min,
  PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY score) as median,
  MAX(score) AS max
FROM result;