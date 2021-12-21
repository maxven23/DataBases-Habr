SELECT DISTINCT b.post_id, COUNT(*) OVER (PARTITION BY ub.bookmark_id) AS Number_of_users
FROM users
INNER JOIN users_has_bookmark ub
ON users.user_id = ub.user_id
INNER JOIN bookmark b on b.bookmark_id = ub.bookmark_id
WHERE b.comment_id IS NULL
GROUP BY ub.bookmark_id, login, b.post_id
ORDER BY Number_of_users DESC
LIMIT 5;