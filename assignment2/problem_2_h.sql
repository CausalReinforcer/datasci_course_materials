SELECT similarity
FROM (
    SELECT a.docid AS a_docid, b.docid AS b_docid, SUM(a.count * b.count) as similarity
    FROM frequency a, frequency b
    WHERE a.term = b.term
    GROUP BY a.docid, b.docid)
WHERE a_docid = '10080_txt_crude' AND b_docid = '17035_txt_earn';