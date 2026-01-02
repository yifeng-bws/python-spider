import webpage
import webbrowser
import time
def main():
    try:
        url = input('请输入查询的网页')
        response = webpage.get_info(url)

        print(f'状态码：{response}')
        with open("outcome.html", "w") as f:
            f.write(response.text)
        print('已执行，请等待')

        time.sleep(2)

        typ = input('是否打开该网页？')
        if typ == '是':
            webbrowser.open_new_tab(url)
    except Exception as e:
        print(f'产生异常，详细为\n{e}')

if __name__ == '__main__':
    main()
