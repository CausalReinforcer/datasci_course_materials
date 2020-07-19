SELECT count(*)
FROM (
    SELECT (count(*) = 2) AS contains_both
    FROM frequency
    WHERE term = 'transactions' OR term = 'world'
    GROUP BY docid
    HAVING contains_both = 1);