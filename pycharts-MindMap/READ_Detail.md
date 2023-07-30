# 思维导图工作流
	由于现有的思维导图软件大多包含节点上限等限制，而且GUI界面交互进行节点的增删改查并不讨喜。而对于个人开发工作者，特别是有一点编程基础的人来说，json格式的上手和编辑并不难。所以本小白在上手json之后，借助已有的编辑器和python的pyecharts包进行思维导图的渲染，以便在日常的工作汇报当中可以制作一些简单的思维导图。同时也是自己做读书笔记的一种方式。所以就搭建了这样一个读取本地json文件，在python当中生成思维导图的工作流。
## 涉及到的工具
- Visual Studio Code。版本June 2023(version 1.80)
- VS code的扩展JSON Editor v0.3.0
- python 3.10
- python 包：pyecharts - version 2.0.3; snapshot_selenium- version 0.0.2; json

## 大致说明
pyecharts是一个包，其用法示例可以在文件pycharts.py中找到。这个包引用了本地同目录下的文件demo_json.json。
snapshot_selenium是图形的渲染引擎。本文使用chrome引擎，需要把chromedriver.exe（本文版本是114）放到同目录下。
