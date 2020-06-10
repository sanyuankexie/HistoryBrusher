# HistoryBrusher
The Brusher to practise



# 历史题库自动随机出题



## 安装必要环境：



需要使用的用`numpy`和`pandas`

安装过的同学可以略过了

下载方式：在官方下载完`python`并安装后找到对应的安装目录（python要3.x版本）

 

比如：`D:\Python37`

然后选择：`D:\Python37\Scripts`复制这个目录

键盘上按 ctrl+R，在弹输入cmd

输入`cd D:\Python37\Scripts`

若没有显示跳转则加一个D:

![img](imgs\clip_image002.jpg)

输入pip install pandas -i https://pypi.douban.com/simple/

![img](imgs\clip_image004.jpg)

开始安装pandas

等待他显示successful即可（如果没有安装成功可以试试去掉-i及后面的部分，实在不行私聊我）

输入 pip install numpy -i https://pypi.douban.com/simple/

![img](imgs\clip_image006.jpg)

开始安装numpy

等待他显示successful即可

 

## 打开方式：

 

有IDE（python的开放平台如pycharm或者vscode等等）的同学，在对应的IDE中运行即可，没有IDE的同学可以使用cmd进行使用

 

开始+R 输入cmd 回车进入命令行

然后用CD跳转到我们py文件所在的目录，

然后输入python bigin.py

![img](imgs\clip_image008.jpg)

就可以进入我们的答题界面了

==**选项必须输入大写A,B,C,D **==

同时设置了错题次数限制，在错6次之后自动输出正确答案，并进入下一题

 

 

## 补充题库：

打开py文件所在目录,将新的题库放到我们的目录中（默认csv格式），选择bigin.py文件，右键，打开方式，选择记事本打开，在这个中括号中添加

![img](imgs\clip_image010.jpg)

添加方式：这行最右边的中括号前输入==**文件名称**==

实现对题库的增加

​    