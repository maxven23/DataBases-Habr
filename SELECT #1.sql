SELECT user_id, count(post_id) FROM post
GROUP BY user_id
ORDER BY count(post_id) DESC, user_id ASC;
