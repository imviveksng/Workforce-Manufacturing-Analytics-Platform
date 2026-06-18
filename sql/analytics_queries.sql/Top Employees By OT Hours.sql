SELECT

    e.emp_id,
    e.emp_name,
    e.department,

    SUM(o.ot_hours) AS total_ot

FROM employees e

JOIN overtime o

ON e.emp_id = o.emp_id

GROUP BY

    e.emp_id,
    e.emp_name,
    e.department

ORDER BY total_ot DESC

LIMIT 10;