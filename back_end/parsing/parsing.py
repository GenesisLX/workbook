import bs4.element
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.parse import urljoin
from .files_work import *
from .driver_work import *
# from driver_work import *
# from files_work import *



def add_title(topic, titleId, AnswerTypeId):
    dict = {}
    title = topic.find("u", class_="Link-U Link_wrap-U Link_pseudo-U Link_pseudoBlack-U")

    if title is None:
        # Не входящие в ОГЭ
        dict[topic.text.split("\xa0")[0]] = titleId, AnswerTypeId, topic.find("a").attrs["href"]
    else:
        # title
        dict[title.text] = titleId, AnswerTypeId

    return dict


def add_sub_title(topic, titleId, lenDict):
    # sub_title
    dict = {}
    NonDelete = 0
    sub_titles = topic.findAll("div", class_="ConstructorForm-TopicDesc")

    for index, sub_title in enumerate(sub_titles[2:]):
        # dict[sub_title.text.split("\xa0")[0]] = index + lenDict, titleId, NonDelete, "https://inf-oge.sdamgia.ru" + sub_title.find("a").attrs["href"]
        dict["https://inf-oge.sdamgia.ru" + sub_title.find("a").attrs["href"]] = index + lenDict, titleId, sub_title.text.split("\xa0")[0], NonDelete

    return dict


def parse_elements_from_main_page(response):
    """Парсит информацию (элементы кода) основной страницы"""

    AnswerTypeId = 1
    titleId = 1
    type_dict = {}
    title_dict = {}
    sub_title_dict = {}

    soup = BeautifulSoup(response, "html.parser")
    ConstructorFormTopic = soup.findAll("div", class_="ConstructorForm-Topic")

    for topic in ConstructorFormTopic:
        if "ConstructorForm-Topic_withTitle_default" in topic.attrs["class"]:
            continue
        if isinstance(topic.next_element, bs4.element.Tag):
            # add type
            if topic.next_element.name == "u":
                type_dict[" ".join(topic.text.split("\xa0"))] = AnswerTypeId
                AnswerTypeId += 1
            else:
                # add title and sub_title
                title_dict.update(add_title(topic, titleId, AnswerTypeId-1))
                sub_title_dict.update(add_sub_title(topic, titleId, len(sub_title_dict.keys())+1))
                titleId += 1
            continue

        # add type
        type_dict[topic.text] = AnswerTypeId
        AnswerTypeId += 1

    return type_dict, title_dict, sub_title_dict


def get_data_main_page(url):
    fileName = 'MainSiteResponse'

    response = return_response(url, fileName)
    type_dict, title_dict, sub_title_dict = parse_elements_from_main_page(response)
    return type_dict, title_dict, sub_title_dict


def parse_problem_and_ans_from_the_site(response):
    soup = BeautifulSoup(response, "html.parser")
    tasks_list = soup.findAll("div", class_='problem_container')
    all_problem = soup.findAll("div", class_='pbody')
    all_ans = soup.findAll("div", class_="solution")
    return all_problem, all_ans, tasks_list


def get_problems_and_ans_from_site(url_problem, fileName, lenDict, sub_themes_id=None, themes_id=None, check=False):
    dict = {}
    response = return_response(url_problem, fileName)
    all_problem, all_ans, tasks_list = parse_problem_and_ans_from_the_site(response)

    for task in tasks_list:
        for img in task.findAll("img"):
            img.attrs["src"] = "https://inf-oge.sdamgia.ru" + img.attrs["src"]
        for a in task.findAll("a"):
            a.attrs["href"] = "https://inf-oge.sdamgia.ru" + a.attrs["href"]




    # id в словаре, id на сайте, отношение к под-теме, отношение к теме, content, solve, ver_crit.

    for i, val in enumerate(tasks_list):
        soup = BeautifulSoup(str(val), "html.parser")
        pbodyDivTag = soup.findAll("div", class_="pbody")
        if len(pbodyDivTag) > 1:
            dict[i + lenDict] = pbodyDivTag[0].attrs["id"], sub_themes_id, themes_id, pbodyDivTag[0], soup.find("div", class_="solution"), pbodyDivTag[1]
        else:
            dict[i+lenDict] = pbodyDivTag[0].attrs["id"], sub_themes_id, themes_id, pbodyDivTag[0], soup.find("div", class_="solution"), None
    return dict


def get_data_page_of_tasks(title_dict, sub_title_dict):
    tasks_dict = {}
    key_dict = {}

    for key in sub_title_dict:
        fileName = sub_title_dict[key][2]
        if fileName not in key_dict:
            key_dict[fileName] = 0
            tasks_dict.update(get_problems_and_ans_from_site(key, fileName, len(tasks_dict.keys()) + 1, sub_title_dict[key][0]))
            # tasks_dict.update(get_problems_and_ans_from_site(key, fileName, len(tasks_dict.keys()) + 1, sub_title_dict[key][0]))

        else:
            key_dict[fileName] += 1
            tasks_dict.update(get_problems_and_ans_from_site(key, fileName + str(key_dict[fileName]), len(tasks_dict.keys()) + 1, sub_title_dict[key][0]))
            # tasks_dict.update(get_problems_and_ans_from_site(key, fileName + str(key_dict[fileName]), len(tasks_dict.keys()) + 1, sub_title_dict[key][0]))

    for key in title_dict:
        if len(title_dict[key]) > 2:
            tasks_dict.update(get_problems_and_ans_from_site(title_dict[key][2], key, len(tasks_dict.keys())+1, None, title_dict[key][0]))

    return tasks_dict