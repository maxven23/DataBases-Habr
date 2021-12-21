WITH hub_posts AS (
    SELECT post_id, count(post_id) as CNT
    FROM post_is_in_hub
    GROUP BY post_id
    ORDER BY CNT DESC, post_id ASC
    LIMIT 5
), hub_names AS (
    SELECT name, h.hub_id, p2.post_id
    FROM hub AS h
    INNER JOIN post_is_in_hub AS piih
    ON h.hub_id=piih.hub_id
    INNER JOIN post AS p2
    ON p2.post_id=piih.post_id
)
SELECT hub_names.name as Hub_name, p.post_id, CNT AS Quantity_of_hubs
FROM post as p
INNER JOIN hub_posts
ON p.post_id=hub_posts.post_id
INNER JOIN hub_names
ON hub_names.post_id=p.post_id
ORDER BY CNT DESC, p.post_id ASC, name ASC;
