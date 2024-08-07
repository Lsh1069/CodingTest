SELECT ID, 
    CASE
        WHEN 100 >= SIZE_OF_COLONY THEN 'LOW'
        WHEN 1000 >= SIZE_OF_COLONY AND SIZE_OF_COLONY > 100 THEN 'MEDIUM'
        ELSE 'HIGH'
    END AS SIZE
FROM ECOLI_DATA
ORDER BY ID