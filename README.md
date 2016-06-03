dict
========
编写程序时，快捷的查询，中英互译。方便函数的定义。


特点
========
* 可以简单的模糊查询：
    * "wor d"-->"word"；
    * "中  国"-->"中国"；
    * "wo1rd2#"-->"word"；

安装说明
=======

代码暂没有在python3上测试

* git https://github.com/sunhongtao/dict.git
* 直接 `python setup.py install`
* 手动安装：将 dict 目录放置于当前目录或者 site-packages 目录
* 通过 `import dict` 来引用
* 可以通过`dict.trans("翻译")`来实现翻译


代码示例：

```pycon
dict.trans("word")
n. 单词; 话语; 诺言; 消息 

vt. 措辞，用词; 用言语表达 

vi. 讲话 

dict.trans("中国")
名 China; the People's Republic of China; Sino-; PRC 
```
缺陷
=======
* 暂不能查看例句；
* 没有在python3上测试；
* 代码冗杂

欢迎大家继续更新
QQ：782666126
提出宝贵意见。
