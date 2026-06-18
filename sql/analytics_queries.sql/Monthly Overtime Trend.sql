SELECT
    DATE_TRUNC('month', ot_date) AS month,
    SUM(ot_hours) AS total_ot
FROM overtime
GROUP BY month
ORDER BY month;