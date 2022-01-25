from email import header


encoding="utf-8"


# from selenium import webdriver

# url="https://data.7m.com.cn/goaldata/jt/4175217.shtml"

# driver = webdriver.Chrome()
# driver.get(url)

# r=driver.page_source

# print(r)

root="""
        Host: txt-api.7m.com.cn
        Connection: keep-alive
        sec-ch-ua: " Not;A Brand";v="99", "Microsoft Edge";v="97", "Chromium";v="97"
        sec-ch-ua-mobile: ?0
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62
        sec-ch-ua-platform: "Windows"
        Accept: */*
        Sec-Fetch-Site: same-site
        Sec-Fetch-Mode: no-cors
        Sec-Fetch-Dest: script
        Referer: https://data.7m.com.cn/
        Accept-Encoding: gzip, deflate, br
        Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
"""
def get_headers(root):
    hh=root.split('\n')
    rel={}
    for h in hh:
        if h=='':
            hh.remove(h)
        else:
            rel[h.strip().split(':')[0].strip()]=h.strip().split(':')[1].strip()

    return rel




print(get_headers(root))