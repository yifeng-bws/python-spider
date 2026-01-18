'''
这里目前是一个网页标签查询器
后面可能会用于爬取视频网站评论（比如中国的bilibili）
'''

import webpage


def main():
    url = input('输入查询的网页: ')
    response = webpage.get_info(url)
    print(f'状态码：{response.status_code if response else "请求失败"}')

    if response and response.ok:
        tag = input('查找网页中的哪个标签？: ')
        tags = webpage.get_all_tags(response, tag)
        print('可能会出现大量标签，建议直接保存到文件夹')
        user = input('选择输出方式\n1.分行输出\n2.直接输出（列表）\n3.保存到该文件夹(推荐)')
        if user == '1':
            for tag in tags:
                print(tag)
        elif user == '2':
            print(tags)
        elif user == '3':
            with open('tags.txt', 'w',encoding='utf-8') as file:
                for tag in tags:
                    file.write(str(tag) + '\n')
        else:
            print('选择无效，请重新运行并输入选项的数字')


if __name__ == '__main__':
    main()
