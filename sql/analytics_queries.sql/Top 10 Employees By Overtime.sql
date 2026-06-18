SELECT
    emp_id,
    SUM(ot_hours) AS total_ot
FROM overtime
GROUP BY emp_id
ORDER BY total_ot DESC
LIMIT 10;