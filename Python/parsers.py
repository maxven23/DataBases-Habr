from bs4 import BeautifulSoup
import requests

def get_habr_companies(url):

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Safari/537.36"
    }

    all_companies_names = []
    all_companies_sites = []
    all_companies_links = []
    all_companies_dates = []
    all_companies_descs = []
    all_companies_count = []

    req = requests.get(url, headers)

    with open("site_page_1.html", "w", encoding="utf-8") as file:
        file.write(req.text)

    with open("site_page_1.html", encoding="utf-8") as src:
        soup = BeautifulSoup(src, "lxml")

    cmps = soup.find_all("a", class_="tm-company-snippet__title")
    for cmp in cmps:
        all_companies_sites.append("https://habr.com"+cmp.get("href"))
        all_companies_names.append(cmp.text.strip())

    for page_n in range(2, 6):
        req = requests.get(url+f"page{page_n}", headers)

        with open(f"site_page_{page_n}.html", "w", encoding="utf-8") as file:
            file.write(req.text)

        with open(f"site_page_{page_n}.html", encoding="utf-8") as src:
            soup = BeautifulSoup(src, "lxml")

        cmps = soup.find_all("a", class_="tm-company-snippet__title")
        for cmp in cmps:
            all_companies_sites.append("https://habr.com"+cmp.get("href"))
            all_companies_names.append(cmp.text.strip())


    iter = 1
    for site in all_companies_sites:
        req = requests.get(site, headers)

        with open(f"company_{iter}.html", "w", encoding="utf-8") as file:
            file.write(req.text)

        with open(f"company_{iter}.html", encoding="utf-8") as src:
            soup_s = BeautifulSoup(src, "lxml")


            try:
                all_companies_links.append(soup_s.find("a", class_="tm-company-basic-info__link").get("href"))
            except Exception as _ex:
                print("[INFO] Error occured while collecting data. No site exists", _ex)
                all_companies_links.append(site)


            try:
                all_companies_dates.append(soup_s.find("div", class_="tm-company-basic-info").find("dd").find("time").get("title")[:10])
            except Exception as _ex:
                print("[INFO] Error occured while collecting data. There is no precise information about foundation.", _ex)
                try:
                    all_companies_dates.append(soup_s.find("div", class_="tm-company-basic-info").find("span").text.strip()+"-01-01")
                except Exception as _ex1:
                    print("[INFO] Error occured while collecting data. There is no foundation date.", _ex1)
                    all_companies_dates.append("1900-01-01")


            try:
                all_companies_descs.append(soup_s.find("span", class_="tm-company-profile__content").text)
            except Exception as _ex:
                print("[INFO] Error occured while collecting data. There is no description for company.", _ex)
                all_companies_descs.append("Описания нет")


            try:
                count_text = (soup_s.find("dt", class_="tm-description-list__title tm-description-list__title_variant-base", text="Численность").find_next("dd").text.replace(" ", "").replace("человек", "").replace("свыше", "").replace("Неизвестно", "0").strip().replace("(толькоя)", ""))
                if (count_text.find("–") != -1):
                    count_text = count_text[count_text.find("–") + 1:]
                all_companies_count.append(int(count_text))
            except Exception as _ex:
                print("[INFO] Error occured while collecting data. There is no information about company' members amount.", _ex)
                all_companies_count.append(0)


            iter += 1



    return all_companies_names, all_companies_links, all_companies_descs, all_companies_dates, all_companies_count


company_info = get_habr_companies("https://habr.com/ru/companies/")


