CREATE TABLE Users
(
  user_id SERIAL NOT NULL,
  login CHAR(32) NOT NULL,
  email CHAR(64) NOT NULL,
  status CHAR(16) NOT NULL,
  registration_date DATE NOT NULL,
  PRIMARY KEY (user_id)
);

CREATE TABLE Post
(
  content TEXT NOT NULL,
  type CHAR(16) NOT NULL,
  creation_date DATE NOT NULL,
  title CHAR(128) NOT NULL,
  post_id SERIAL NOT NULL,
  user_id INT NOT NULL,
  PRIMARY KEY (post_id),
  FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE Comment
(
  comment_id SERIAL NOT NULL,
  date DATE NOT NULL,
  text TEXT NOT NULL,
  post_id INT NOT NULL,
  user_id INT NOT NULL,
  PRIMARY KEY (comment_id),
  FOREIGN KEY (post_id) REFERENCES Post(post_id),
  FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE Hub
(
  hub_id SERIAL NOT NULL,
  name CHAR(128) NOT NULL,
  PRIMARY KEY (hub_id)
);

CREATE TABLE Company
(
  company_id SERIAL NOT NULL,
  amount INT NOT NULL,
  site CHAR(128),
  representative_id INT NOT NULL,
  foundation_date DATE NOT NULL,
  description TEXT NOT NULL,
  name CHAR(128) NOT NULL,
  PRIMARY KEY (company_id)
);

CREATE TABLE Bookmark
(
  bookmark_id SERIAL NOT NULL,
  post_id INT,
  comment_id INT,
  PRIMARY KEY (bookmark_id),
  FOREIGN KEY (post_id) REFERENCES Post(post_id),
  FOREIGN KEY (comment_id) REFERENCES Comment(comment_id)
);

CREATE TABLE Users_has_Bookmark
(
  user_bookmark_id SERIAL NOT NULL,
  user_id INT NOT NULL,
  bookmark_id INT NOT NULL,
  PRIMARY KEY (user_bookmark_id),
  FOREIGN KEY (user_id) REFERENCES Users(user_id),
  FOREIGN KEY (bookmark_id) REFERENCES Bookmark(bookmark_id)
);

CREATE TABLE Post_is_in_Hub
(
  post_hub_id SERIAL NOT NULL,
  post_id INT NOT NULL,
  hub_id INT NOT NULL,
  PRIMARY KEY (post_hub_id),
  FOREIGN KEY (post_id) REFERENCES Post(post_id),
  FOREIGN KEY (hub_id) REFERENCES Hub(hub_id)
);

CREATE TABLE Users_is_in_Company
(
  user_company_id SERIAL NOT NULL,
  user_id INT NOT NULL,
  company_id INT NOT NULL,
  PRIMARY KEY (user_company_id),
  FOREIGN KEY (user_id) REFERENCES Users(user_id),
  FOREIGN KEY (company_id) REFERENCES Company(company_id)
);

CREATE TABLE Company_is_in_Hub
(
  company_hub_id SERIAL NOT NULL,
  company_id INT NOT NULL,
  hub_id INT NOT NULL,
  PRIMARY KEY (company_hub_id),
  FOREIGN KEY (company_id) REFERENCES Company(company_id),
  FOREIGN KEY (hub_id) REFERENCES Hub(hub_id)
);