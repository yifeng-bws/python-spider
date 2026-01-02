import requests
from bs4 import BeautifulSoup


# 爬取网页
def get_info(url):
    try:
        response = requests.get(url)
        response.encoding = response.apparent_encoding
        return response
    except Exception as e:
        print(f'产生异常，详细为：\n{e}')


# 实验性功能
'''
get_all_tags(response, tag)
用于获取网页全部标签，用bs4库解析
'''


def get_all_tags(response, tag):
    search = BeautifulSoup(response.text, 'html.parser')
    tags = search.find_all(tag)
    return tags


# 实验性功能
'''
tags = tag_traversal(tags)
使用for循环遍历输出全部标签，分行输出
'''


def tag_traversal(tags):
    for tag in tags:
        print(tag)


if __name__ == '__main__':
    # 示例操作
    response = get_info('https://python.org/')
    print(f'状态码：\n{response}')

    if response:
        tags = get_all_tags(response, 'p')
        print(f'获取到的标签：\n{tags}')
        tag_traversal(tags)

        with open("response.html", "w") as f:
            f.write(response.text)
