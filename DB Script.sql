CREATE TABLE IF NOT EXISTS Users
(
  user_id SERIAL,
  login VARCHAR(32) NOT NULL,
  email VARCHAR(64) CHECK (email LIKE '%@%.%') NOT NULL,
  status VARCHAR(13) CHECK (status in ('Administrator', 'Default', 'Moderator', 'Editor')) NOT NULL,
  registration_date DATE NOT NULL,
  PRIMARY KEY (user_id)
);

CREATE TABLE IF NOT EXISTS Post
(
  content TEXT NOT NULL,
  type VARCHAR(12) CHECK (type in ('article', 'news', 'notification')) NOT NULL,
  creation_date DATE NOT NULL,
  title VARCHAR(128) NOT NULL,
  post_id SERIAL,
  user_id INT NOT NULL,
  PRIMARY KEY (post_id),
  FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE IF NOT EXISTS Comment
(
  comment_id SERIAL,
  date DATE NOT NULL,
  text TEXT NOT NULL,
  post_id INT NOT NULL,
  user_id INT NOT NULL,
  PRIMARY KEY (comment_id),
  FOREIGN KEY (post_id) REFERENCES Post(post_id),
  FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE IF NOT EXISTS Hub
(
  hub_id SERIAL,
  name VARCHAR(128) NOT NULL,
  PRIMARY KEY (hub_id)
);

CREATE TABLE IF NOT EXISTS Company
(
  company_id SERIAL,
  amount INT NOT NULL,
  site VARCHAR(128),
  representative_id INT NOT NULL,
  foundation_date DATE NOT NULL,
  description TEXT NOT NULL,
  name VARCHAR(128) NOT NULL,
  PRIMARY KEY (company_id)
);

CREATE TABLE IF NOT EXISTS Bookmark
(
  bookmark_id SERIAL,
  post_id INT,
  comment_id INT,
  PRIMARY KEY (bookmark_id),
  FOREIGN KEY (post_id) REFERENCES Post(post_id),
  FOREIGN KEY (comment_id) REFERENCES Comment(comment_id)
);

CREATE TABLE IF NOT EXISTS Users_has_Bookmark
(
  user_bookmark_id SERIAL,
  user_id INT NOT NULL,
  bookmark_id INT NOT NULL,
  PRIMARY KEY (user_bookmark_id),
  FOREIGN KEY (user_id) REFERENCES Users(user_id),
  FOREIGN KEY (bookmark_id) REFERENCES Bookmark(bookmark_id)
);

CREATE TABLE IF NOT EXISTS Post_is_in_Hub
(
  post_hub_id SERIAL,
  post_id INT NOT NULL,
  hub_id INT NOT NULL,
  PRIMARY KEY (post_hub_id),
  FOREIGN KEY (post_id) REFERENCES Post(post_id),
  FOREIGN KEY (hub_id) REFERENCES Hub(hub_id)
);

CREATE TABLE IF NOT EXISTS Users_is_in_Company
(
  user_company_id SERIAL,
  user_id INT NOT NULL,
  company_id INT NOT NULL,
  PRIMARY KEY (user_company_id),
  FOREIGN KEY (user_id) REFERENCES Users(user_id),
  FOREIGN KEY (company_id) REFERENCES Company(company_id)
);

CREATE TABLE IF NOT EXISTS Company_is_in_Hub
(
  company_hub_id SERIAL,
  company_id INT NOT NULL,
  hub_id INT NOT NULL,
  PRIMARY KEY (company_hub_id),
  FOREIGN KEY (company_id) REFERENCES Company(company_id),
  FOREIGN KEY (hub_id) REFERENCES Hub(hub_id)
);