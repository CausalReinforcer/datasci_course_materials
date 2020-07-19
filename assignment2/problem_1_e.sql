SELECT count(*)
FROM (
    SELECT docid, count(*) as total_terms
    FROM frequency
    GROUP BY docid
    HAVING total_terms > 300
    );
