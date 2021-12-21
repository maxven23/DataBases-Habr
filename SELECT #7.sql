WITH Counters AS (
    SELECT post.post_id, u.user_id,
           CASE
               WHEN post.post_id IS NULL THEN 0
               ELSE 1
           END AS CNT
    FROM post
    RIGHT JOIN users u ON u.user_id=post.user_id
), PostsAmount AS (
    SELECT post.post_id,
           u.user_id,
           u.login,
           u.email,
           SUM(CNT) AS Amount_of_posts
    FROM post
    RIGHT JOIN users u on post.user_id = u.user_id
    JOIN Counters ON Counters.user_id=u.user_id
    GROUP BY u.user_id, post.post_id
)
SELECT DISTINCT C.name, PA.login, PA.email, PA.Amount_of_posts
FROM PostsAmount AS PA
INNER JOIN company AS C
ON C.representative_id=PA.user_id
WHERE foundation_date>'01-01-2000' AND amount=10000
ORDER BY C.name;