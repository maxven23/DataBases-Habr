import psycopg2
import functionality as gen
from config import host, user, password, db_name


try:
    # Connceting to db
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

    connection.autocommit = True

    # Cursor for DB operations
    # cursor = connection.cursor()
    with connection.cursor() as cursor:

        # Удаляем уже существующие таблицы
        REQUEST = """DROP SCHEMA public CASCADE;"""
        cursor.execute(REQUEST)
        REQUEST = """CREATE SCHEMA public;"""
        cursor.execute(REQUEST)
        REQUEST = """GRANT ALL ON SCHEMA public TO postgres;"""
        cursor.execute(REQUEST)
        REQUEST = """GRANT ALL ON SCHEMA public TO public;"""
        cursor.execute(REQUEST)

        # Создаём новые таблицы по SQL-файлу нашей БД
        REQUEST = """CREATE TABLE Users
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
);"""

        cursor.execute(REQUEST)

        # Заполняем таблицу users рандомными данными
        for user_ in gen.users:
            REQUEST = f"""INSERT INTO users(login, email, status, registration_date) VALUES ('{user_["login"]}', '{user_["email"]}', '{user_["status"]}', '{user_["registration_date"]}');"""
            # print(REQUEST)
            cursor.execute(REQUEST)

        # Заполняем таблицу post рандомными данными
        for post_ in gen.posts:
            REQUEST = f"""INSERT INTO post (content, type, creation_date, title, user_id) VALUES ('{post_["content"]}', '{post_["type"]}', '{post_["creation_date"]}', '{post_["title"]}', {post_["user_id"]});"""
            # print(REQUEST)
            cursor.execute(REQUEST)

        # Заполняем таблицу comment рандомными данными
        for comment_ in gen.comments:
            REQUEST = f"""INSERT INTO comment (date, text, user_id, post_id) VALUES ('{comment_["date"]}', '{comment_["text"]}', '{comment_["user_id"]}', {comment_["post_id"]});"""
            # print(REQUEST)
            cursor.execute(REQUEST)

        # Заполняем таблицу hub рандомными данными
        for hub_ in gen.hubs:
            REQUEST = f"""INSERT INTO hub (name) VALUES ('{hub_["name"]}');"""
            # print(REQUEST)
            cursor.execute(REQUEST)

        # Заполняем таблицу company рандомными данными
        for company_ in gen.companies:
            REQUEST = f"""INSERT INTO company (amount, description, foundation_date, representative_id, site, name) VALUES ({company_["amount"]}, '{company_["description"]}', '{company_["foundation_date"]}', {company_["representative_id"]}, '{company_["site"]}', '{company_["name"]}');"""
            # print(REQUEST)
            cursor.execute(REQUEST)

        # Заполняем таблицу bookmark рандомными данными
        for bookmark_ in gen.bookmarks:
            REQUEST = f"""INSERT INTO bookmark (post_id, comment_id) VALUES ({bookmark_["post_id"]}, {bookmark_["comment_id"]});"""
            # print(REQUEST)
            cursor.execute(REQUEST)

        # Заполняем таблицу users_has_bookmark рандомными данными
        for users_has_bookmark_ in gen.users_has_bookmark:
            REQUEST = f"""INSERT INTO users_has_bookmark (user_id, bookmark_id) VALUES ({users_has_bookmark_["user_id"]}, {users_has_bookmark_["bookmark_id"]});"""
            # print(REQUEST)
            cursor.execute(REQUEST)

        # Заполняем таблицу users_is_in_company рандомными данными
        for users_is_in_company_ in gen.users_is_in_company:
            REQUEST = f"""INSERT INTO users_is_in_company (user_id, company_id) VALUES ({users_is_in_company_["user_id"]}, {users_is_in_company_["company_id"]});"""
            # print(REQUEST)
            cursor.execute(REQUEST)

        # Заполняем таблицу post_is_in_hub рандомными данными
        for post_is_in_hub_ in gen.post_is_in_hub:
            REQUEST = f"""INSERT INTO post_is_in_hub (post_id, hub_id) VALUES ({post_is_in_hub_["post_id"]}, {post_is_in_hub_["hub_id"]});"""
            # print(REQUEST)
            cursor.execute(REQUEST)

        # Заполняем таблицу company_is_in_hub рандомными данными
        for company_is_in_hub_ in gen.company_is_in_hub:
            REQUEST = f"""INSERT INTO company_is_in_hub (company_id, hub_id) VALUES ({company_is_in_hub_["company_id"]}, {company_is_in_hub_["hub_id"]});"""
            # print(REQUEST)
            cursor.execute(REQUEST)


        REQUEST = ""
        # while REQUEST.lower() != "exit":
        #     REQUEST = input("Введите желаемый запрос (для выхода введите EXIT):\n")
        #     cursor.execute(REQUEST)
        #     print(cursor.fetchall())


except Exception as _ex:
    print("[INFO] Error occured while working with PostgreSQL", _ex)
finally:
    if connection:
        # cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")