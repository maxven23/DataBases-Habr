WITH comment_num AS (
    SELECT user_id, count(user_id) as CNT
    FROM comment
    GROUP BY user_id
)
SELECT u.user_id, u.login, CNT
FROM users as u
INNER JOIN comment_num
ON u.user_id=comment_num.user_id
ORDER BY comment_num.CNT DESC, u.user_id
LIMIT 1;
