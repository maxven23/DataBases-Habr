WITH Post_Texts AS (
    SELECT COALESCE(((CHAR_LENGTH(LOWER(content)) - CHAR_LENGTH(REPLACE(LOWER(content), ' it ', '  ')))
    / CHAR_LENGTH('it')) + ((CHAR_LENGTH(content) - CHAR_LENGTH(REPLACE(content, 'It ', ' ')))
    / CHAR_LENGTH('It')) + ((CHAR_LENGTH(content) - CHAR_LENGTH(REPLACE(content, ' it.', ' .')))
    / CHAR_LENGTH('it')) + ((CHAR_LENGTH(content) - CHAR_LENGTH(REPLACE(content, ' it,', ' ,')))
    / CHAR_LENGTH('it')), 0) AS num,
           post_id,
           u.user_id,
           content
    FROM post
    RIGHT JOIN users u on post.user_id = u.user_id
    GROUP BY u.user_id, post_id
    ORDER BY num DESC, post_id ASC, u.user_id ASC
), Comment_Texts AS (
    SELECT COALESCE(((CHAR_LENGTH(LOWER(text)) - CHAR_LENGTH(REPLACE(LOWER(text), ' it ', '  ')))
    / CHAR_LENGTH('it')) + ((CHAR_LENGTH(text) - CHAR_LENGTH(REPLACE(text, 'It ', ' ')))
    / CHAR_LENGTH('It')) + ((CHAR_LENGTH(text) - CHAR_LENGTH(REPLACE(text, ' it.', ' .')))
    / CHAR_LENGTH('it')) + ((CHAR_LENGTH(text) - CHAR_LENGTH(REPLACE(text, ' it,', ' ,')))
    / CHAR_LENGTH('it')), 0) AS num,
           comment_id,
           u.user_id,
           text
    FROM comment
    RIGHT JOIN users u on comment.user_id = u.user_id
    GROUP BY u.user_id, comment_id
    ORDER BY num DESC, comment_id ASC
), Sum_of_forbidden_words AS (
    SELECT (COALESCE(SUM(PT.num), 0) + COALESCE(SUM(CT.num), 0)) AS num,
           CT.user_id,
           CASE
               WHEN PT.num<>0 AND CT.num=0 THEN 'In Posts'
               WHEN PT.num=0 AND CT.num<>0 THEN 'In Comments'
               WHEN PT.num<>0 AND CT.num<>0 THEN 'In Posts and Comments'
               ELSE 'Nowhere'
           END AS where_is
    FROM Post_Texts AS PT
    INNER JOIN Comment_Texts CT ON PT.user_id=CT.user_id
    GROUP BY CT.user_id, PT.content, CT.text, PT.num, CT.num
    ORDER BY num DESC
)
SELECT DISTINCT *
FROM Sum_of_forbidden_words Sofw
ORDER BY Sofw.num DESC, Sofw.user_id;