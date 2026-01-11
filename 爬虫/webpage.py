import requests
from bs4 import BeautifulSoup


# 爬取网页
def get_info(url):
    try:
        response = requests.get(url)
        response.encoding = response.apparent_encoding
        return response
    except Exception as e:
        print(f'Error：\n{e}')
        return None


# 实验性功能
'''
get_all_tags(response, tag)
用于获取网页全部标签，用bs4库解析
'''
def get_all_tags(response, tag):
    if response and response.ok:
        search = BeautifulSoup(response.text, 'html.parser')
        tags = search.find_all(tag)
        return tags
    else:
        print('无法解析网页内容')
        return []



if __name__ == '__main__':
    # 示例操作
    response = get_info('https://python.org/')
    print(f'状态码：\n{response.status_code if response else "请求失败"}')

    if response and response.ok:
        tags = get_all_tags(response, 'p')
        print('获取到的标签：')
        for tag in tags:
            print(tag)

