SELECT A.id as order_id, B.name as name, (CASE WHEN EXISTS(SELECT *	FROM points C WHERE C.member_id = B.id) THEN '1' ELSE '0' END) AS is_point
FROM orders A, members B
WHERE A.member_id = B.id
ORDER BY A.id;
