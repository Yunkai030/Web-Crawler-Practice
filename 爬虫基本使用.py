import urllib.request
# (1) 定义一个url
urlbili = 'https://www.bilibili.com'
urlbaidu = 'https://www.baidu.com'

# (2) send request to the server
response = urllib.request.urlopen(urlbili)
response_baidu = urllib.request.urlopen(urlbaidu)


# (3) get content
content = response_baidu.read().decode('UTF-8')

#(4) print the content (the content that return in binary form)
# from binary to
print(content)


