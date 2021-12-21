WITH Counters AS (
    SELECT u.user_id, post.post_id,
           CASE
               WHEN post.post_id IS NULL THEN 0
               ELSE 1
           END AS CNT
    FROM post
    LEFT JOIN users u ON u.user_id=post.user_id
), PostsAmount AS (
    SELECT post.post_id,
           u.user_id,
           SUM(CNT)
    FROM post
    RIGHT JOIN users u on post.user_id = u.user_id
    JOIN Counters ON Counters.user_id=u.user_id
    GROUP BY u.user_id, post.post_id
    ORDER BY u.user_id
)
SELECT *
FROM Counters
-- INNER JOIN users
-- ON company.representative_id=users.user_id
-- INNER JOIN PostsAmount
-- ON PostsAmount.user_id=users.user_id
-- WHERE foundation_date>'01-01-2000' AND amount=10000;