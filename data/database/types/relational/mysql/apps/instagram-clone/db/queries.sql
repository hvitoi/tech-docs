-- Find 5 oldest users
SELECT * 
FROM users
ORDER BY created_at
LIMIT 5;

-- What day of the week do most users register on?
SELECT 
  DATE_FORMAT(created_at, '%W') as day_week,
  COUNT(id) as total
FROM users
GROUP BY day_week
ORDER BY total DESC;

-- Users who never posted a photo
SELECT *
FROM users
LEFT JOIN photos
  ON photos.user_id = users.id
WHERE photos.id IS NULL;

-- Most popular photo and the user who created it
SELECT 
  users.username as photo_owner,
  COUNT(*) AS total_likes
FROM photos
JOIN likes
  ON likes.photo_id = photos.id
JOIN users
  ON users.id = photos.user_id
GROUP BY likes.photo_id
ORDER BY total_likes DESC
LIMIT 5;


-- What is the avg number of photos by users
SELECT 
  (SELECT Count(*) FROM photos) /
  (SELECT Count(*) FROM users)
AS avg; 

-- Five most popular tags
SELECT tag_id, tag_name, COUNT(photo_id) AS total
FROM photo_tags
JOIN tags
  ON tags.id = photo_tags.tag_id
GROUP BY tag_id
ORDER BY total DESC
LIMIT 5;

-- Users on have liked every single photo on the site (bots)
SELECT username, 
       Count(*) AS num_likes 
FROM   users 
       INNER JOIN likes 
               ON users.id = likes.user_id 
GROUP  BY likes.user_id 
HAVING num_likes = (SELECT Count(*) 
                    FROM   photos); 