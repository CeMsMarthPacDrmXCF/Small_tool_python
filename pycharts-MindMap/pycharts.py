# 基本思维导图
from pyecharts import options as opts
from pyecharts.charts import Tree
from snapshot_selenium import snapshot
# 图片输出工具
from pyecharts.render import make_snapshot
import json
# Tree的data： 数组- dict（name-string, children-[]）。
# data = [
#     {
#         "children": [
#             {"name": "高等数学"},
#             {
#                 "children": [
#
#                     {"name": "线性空间"},
#                 ],
#                 "name": "线性代数",
#             },
#         ],
#         "name": "思维导图",
#     }
# ]
# 读取本地json格式文件
with open(r'.\demo_json.json', 'r',encoding='utf-8') as file_json:
    # with open方法会一次读取文件的所有内容。如果太大内存会爆炸。
    # print(type(file_json)) # io.TextIOWrapper 主要属性：name和encoding
    # trailing commma, 多余的逗号问题
    data = json.load(file_json,encoding='utf-8')

c = (
    Tree()
        .add("", data)
        .set_global_opts(title_opts=opts.TitleOpts(title="Tree-基本思维导图"))
    # .render("Mind_map.html")
)
make_snapshot(snapshot, c.render(), "Mind_map_demo.png")