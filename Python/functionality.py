import random
import datetime
import parsers as p

from faker import Faker

#Faker.seed(0)
fake = Faker(locale="ru_RU")

N = 1000

#----------------------------------------

email_endings = ["gmail.com",
                 "mail.ru",
                 "ok.ru",
                 "bk.ru",
                 "list.ru",
                 "hotmail.com",
                 "mephi.ru",
                 "example.net",
                 "example.com",
                 "example.org",
                 "yandex.ru"
                ]

LENGTH = len(email_endings) - 1

emails = []
user_names = []
registration_dates = []

while len(emails) < N:
    fake_email = fake.email()
    fake_email = fake_email[:fake_email.find("@") + 1] + random.choice(email_endings)
    if fake_email not in emails:
        emails.append(fake_email)

while len(user_names) < N:
    fake_user_name = fake.user_name()
    if fake_user_name not in user_names:
        user_names.append(fake_user_name)

for i in range(N):
    registration_date = fake.date_between(start_date = "-6y", end_date = "now")
    registration_dates.append(registration_date)


users = []
for i in range(len(emails)):
    users.append({
        "login": user_names[i],
        "email": emails[i],
        "registration_date": registration_dates[i].strftime('%Y-%m-%d'),
        "status": "Default"
    })
    #print(str(i + 1) + ": " + str(users[i]))

#----------------------------------------

fake = Faker(locale="en")

type_list = ["news",
             "news",
             "news",
             "article",
             "article",
             "article",
             "article",
             "article",
             "article",
             "notification"
            ]

posts = []

types = [random.choice(type_list) for _ in range(N)]
user_ids = [random.randint(1, N) for _ in range(N)]
texts = [fake.text(max_nb_chars=1000) for _ in range(N)]
titles = [fake.sentence(nb_words=random.randint(3, 12)) for _ in range(N)]
creation_dates = [fake.date_between(start_date = datetime.datetime.strptime(users[user_ids[i] - 1]["registration_date"], '%Y-%m-%d').date(), end_date = "now") for i in range(N)]

for i in range(N):
    posts.append({
        "content": texts[i],
        "type": types[i],
        "creation_date": creation_dates[i],
        "title": titles[i],
        "user_id": user_ids[i]
    })


# for post in posts:
#     print(str(post))

#----------------------------------------

comments = []

comment_user_ids = [random.randint(1, N) for _ in range(100)]
comment_post_ids = [random.randint(1, N) for _ in range(100)]
comment_texts = [fake.text(max_nb_chars=127) for _ in range(100)]
comment_date = [fake.date_between(start_date=posts[comment_post_ids[i] - 1]["creation_date"], end_date = "now") for i in range(100)]

for i in range(100):
    comments.append({
        "date": comment_date[i],
        "text": comment_texts[i],
        "user_id": comment_user_ids[i],
        "post_id": comment_post_ids[i]
    })


# for comment in comments:
#     print(str(comment))

#----------------------------------------

hub_names = [
    "Scientific-popular",
    "Information security",
    "Programming",
    "IT-companies",
    "Python",
    "JavaScript",
    "C++",
    "C#",
    "C",
    "Ruby",
    "Java",
    "Pascal",
    "Health",
    "Algorithmes",
    "Machine learning",
    "Transport",
    "Games",
    "Web design",
    "Finance",
    "Biology",
    "Math",
    "Physics",
    "Chemistry",
    "Android",
    "Statistics"
]

hubs = []

for hub_name in hub_names:
    hubs.append({"name": hub_name})

# for hub in hubs:
#     print(hub)

#----------------------------------------

companies = []

company_info = p.company_info
company_names = company_info[0]
company_sites = company_info[1]
company_descriptions = company_info[2]
company_dates = company_info[3]
company_amounts = company_info[4]
company_rep_ids = [random.randint(1, N) for _ in range(100)]

for i in range(100):
    companies.append({
        "name": company_names[i],
        "site": company_sites[i],
        "description": company_descriptions[i],
        "foundation_date": company_dates[i],
        "amount": company_amounts[i],
        "representative_id": company_rep_ids[i]
    })

#----------------------------------------

bookmarks = []

post_ids = []
comment_ids = []
for i in range(50):
    bm_type = random.choice(["comment", "post"])
    if bm_type=="comment":
        comment_id = random.randint(1, 100)
        if comment_id not in comment_ids:
            comment_ids.append(comment_id)
            post_ids.append("NULL")
    elif bm_type=="post":
        post_id = random.randint(1, N)
        if post_id not in post_ids:
            post_ids.append(post_id)
            comment_ids.append("NULL")

for i in range(len(post_ids)):
    bookmarks.append({
        "post_id": post_ids[i],
        "comment_id": comment_ids[i]
    })

# for bookmark in bookmarks:
#     print(bookmark)

#----------------------------------------

users_has_bookmark = []

user_ids = [random.randint(1, N) for _ in range(200)]
bookmark_ids = [random.randint(1, len(bookmarks)) for _ in range(200)]

for i in range(200):
    users_has_bookmark.append({
        "user_id": user_ids[i],
        "bookmark_id": bookmark_ids[i]
    })

# for ub in users_has_bookmark:
#     print(ub)

#----------------------------------------

users_is_in_company = []

users_ids = [random.randint(1, N) for _ in range(200)]
company_ids = [random.randint(1, 100) for _ in range(200)]

for i in range(200):
    users_is_in_company.append({
        "user_id": users_ids[i],
        "company_id": company_ids[i]
    })

# for uinc in users_is_in_company:
#     print(uinc)

#----------------------------------------

post_is_in_hub = []

hub_ids = [random.randint(1, 25) for _ in range(1100)]
post_ids = [random.randint(1, N) for _ in range(1100)]

for i in range(1100):

    post_is_in_hub.append({
        "hub_id": hub_ids[i],
        "post_id": post_ids[i]
    })

# for ph in post_is_in_hub:
#     print(ph)

#----------------------------------------

company_is_in_hub = []

hub_ids = [random.randint(1, 25) for _ in range(50)]
company_ids = [random.randint(1, 100) for _ in range(50)]

for i in range(50):
    company_is_in_hub.append({
        "hub_id": hub_ids[i],
        "company_id": company_ids[i]
    })

# for ch in company_is_in_hub:
#     print(ch)

#----------------------------------------