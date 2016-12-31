## 环境

* Ubuntu 16.04 STL
* python 2.7.12
* selenium
* Firefox
* geckodriver

## 配置

### selenium安装

```
sudo pip install selenium
```

### geckodriver安装

>>
>>下载 geckodriverckod 地址： mozilla/geckodriver
>>解压后将geckodriverckod 存放至 /usr/local/bin/ 路径下即可
>>```
>>sudo mv ～/Downloads/geckodriver /usr/local/bin/
>>```

作者：王阳阳
链接：https://www.zhihu.com/question/49568096/answer/131093426
来源：知乎

## Firefox-Default-Profile的路径

```
cd /home/yourname/.mozilla/firefox/
```

## 说明

大部分Discuz论坛签到插件都是本例中解析的这款，本例仅提供思路，因为不同的论坛在结构上会有细微的差别。但由于目标页仅仅是签到页这一页，所以可以直接从浏览器开发者工具中使用自动生成XPath。

示例脚本中包含红客联盟论坛和精易论坛，前者登陆不需验证码，可以使用`login`方法登陆，而不需配置FirefoxProfile。

如精易论坛此类登陆需要验证码的，需事先登陆(勾选自动登陆，cookie存活时间长)，然后配置本地FirefoxProfile，如示例中所写。

高人路过，还请不吝指点此处如何在程序中配置cookie，感激不尽！

