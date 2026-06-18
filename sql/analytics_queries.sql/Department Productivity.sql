SELECT

    department,

    SUM(units_produced) AS total_production

FROM production

GROUP BY department;