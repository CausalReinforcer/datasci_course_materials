WITH extended AS (
    SELECT *
    FROM frequency
        UNION
    SELECT 'q' AS docid, 'washington' AS term, 1 AS count
        UNION
    SELECT 'q' AS docid, 'taxes' AS term, 1 AS count
        UNION 
    SELECT 'q' AS docid, 'treasury' AS term, 1 AS count
),
similarities AS (
    SELECT a.docid AS a_docid, b.docid AS b_docid, SUM(a.count * b.count) AS similarity
    FROM extended a, extended b
    WHERE a.term = b.term AND a.docid = 'q'
    GROUP BY a.docid, b.docid
)

SELECT similarity
FROM similarities
ORDER BY similarity DESC
LIMIT 1;