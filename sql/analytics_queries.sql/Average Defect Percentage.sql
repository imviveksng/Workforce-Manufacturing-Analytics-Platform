SELECT
    machine_id,
    ROUND(
        AVG(defect_percentage)::numeric, 
        2
    ) AS avg_defect_rate
FROM quality
GROUP BY machine_id
ORDER BY avg_defect_rate DESC;