SELECT u.login, u.user_id
FROM users u
WHERE user_id NOT IN (
    SELECT DISTINCT u1.user_id
    FROM users AS u1
    INNER JOIN post p
    ON u1.user_id = p.user_id
);