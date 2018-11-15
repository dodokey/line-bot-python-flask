import requests
from bs4 import BeautifulSoup
import random


def findhahapoint(point):
    result = {}
    url = "https://www.ptt.cc/bbs/joke/index.html"
    while True:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        posts = soup.find_all("div", class_="r-ent")
        for post in posts:
            try:
                commend = int(post.find("span").string)
            except:
                commend = 0
            if commend > point:
                result['title'] = post.select("a")[0].text
                result['url'] = "https://www.ptt.cc" + \
                    post.select("a")[0]["href"]
                return result
        # sel = soup.select("div.title a")  # 標題
        u = soup.select("div.btn-group.btn-group-paging a")  # a標籤
        url = "https://www.ptt.cc" + u[1]["href"]  # 上一頁的網址


def checkformat(soup, class_tag, data, index, url):
    content = soup.select(class_tag)[index].text
    return content


def getInnerText(url):
    response = requests.get(url)
    # 將原始碼做整理
    soup = BeautifulSoup(response.text, 'lxml')
    date = checkformat(soup, '.article-meta-value', 'date', 3, url)
    # content 文章內文
    content = soup.find(id="main-content").text
    target_content = u'※ 發信站: 批踢踢實業坊(ptt.cc),'
    # 去除掉 target_content
    content = content.split(target_content)
    content = content[0].split(date)
    # 去除掉文末 --
    main_content = content[1].replace('--', '')
    # 印出內文
    return main_content


def guess():
    result = {}
    url = "https://www.ptt.cc/bbs/joke/index.html"
    lottery = random.randint(0, 20)
    count = 0
    while True:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        posts = soup.find_all("div", class_="r-ent")
        for post in posts[::-1]:
            try:
                title = post.select("a")[0].text
                if (title[0:3] == '[猜謎') and (len(title[4:]) > 0):
                    count += 1
                    if count == lottery:
                        url = "https://www.ptt.cc" + \
                            post.select("a")[0]["href"]
                        # ans = getInnerText(url).replace('\n', '')
                        result['Q'] = title[4:]
                        result['A'] = getInnerText(url)
                        return result
            except:
                pass
        # sel = soup.select("div.title a")  # 標題
        u = soup.select("div.btn-group.btn-group-paging a")  # a標籤
        # print("本頁的URL為"+url)
        url = "https://www.ptt.cc" + u[1]["href"]  # 上一頁的網址


if __name__ == '__main__':
    print(guess())
