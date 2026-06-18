SELECT
    machine_id,
    SUM(units_produced) AS total_units
FROM production
GROUP BY machine_id
ORDER BY total_units DESC;