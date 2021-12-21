WITH Date_Diff1 AS (
    SELECT p1.user_id, p1.post_id, p2.post_id, COUNT(p1.user_id) as Posts_Amount, DATE_PART('day', p2.creation_date::timestamp - p1.creation_date::timestamp) as DP
    FROM post p1
    INNER JOIN post p2
    ON p1.user_id=p2.user_id AND p1.post_id <> p2.post_id
    WHERE DATE_PART('day', p2.creation_date::timestamp - p1.creation_date::timestamp) > 0
    GROUP BY p1.user_id, p1.post_id, p2.post_id, DATE_PART('day', p2.creation_date::timestamp - p1.creation_date::timestamp)
    ORDER BY user_id
)
SELECT dd1.user_id, AVG(dd1.DP) AS Average_amount_of_days_between_Posts, dd1.Posts_Amount
FROM Date_Diff1 AS dd1
INNER JOIN Date_Diff1 AS dd2
ON dd1.user_id=dd2.user_id
GROUP BY dd1.user_id, dd1.Posts_Amount
ORDER BY user_id;

-- WITH Date_Diff1 AS (
--     SELECT p1.user_id, p2.post_id, p2.creation_date, p1.post_id, p1.creation_date, DATE_PART('day', p2.creation_date::timestamp - p1.creation_date::timestamp) as DP
--     FROM post p1
--     INNER JOIN post p2
--     ON p1.user_id=p2.user_id AND p1.post_id <> p2.post_id
--     WHERE DATE_PART('day', p2.creation_date::timestamp - p1.creation_date::timestamp) > 0
--     GROUP BY p2.creation_date, p1.creation_date, p2.post_id, p1.post_id, p1.user_id, DATE_PART('day', p2.creation_date::timestamp - p1.creation_date::timestamp)
--     ORDER BY user_id, p2.creation_date, p1.creation_date
-- )
-- SELECT *
-- FROM Date_Diff1 AS dd1
-- -- INNER JOIN Date_Diff1 AS dd2
-- -- ON dd1.user_id=dd2.user_id
-- -- GROUP BY dd1.user_id, dd1.DP
-- ORDER BY dd1.user_id;