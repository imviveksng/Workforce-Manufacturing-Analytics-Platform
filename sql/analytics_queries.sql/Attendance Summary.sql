SELECT
    status,
    COUNT(*) AS total_records
FROM attendance
GROUP BY status;