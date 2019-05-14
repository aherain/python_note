from snapshot_selenium import snapshot as driver

from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.render import make_snapshot


def bar_chart() -> Bar:
    c = (
        Bar()
        .add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
        .add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-测试渲染图片"))
    )
    return c

# 需要安装 snapshot_selenium 也需要下载chromedriver 配置对应的环境变量
make_snapshot(driver, bar_chart().render(), "bar.png")

#数据交锋，是谁在说谎呢
#预测未来，就是揣度上帝

# 嘘，听：数据在说谎
#掐指一算，花落知多少

#运行纲要
# 1, logon是我们鲜明的旗帜
# 2, 开明智慧是我们服务的要旨
# 3, 用户是核心，拉为主策略
# 4, 定义图文模板，打造专业风格
# 5, 组织成员建构
# 6, 无为及时淘汰
# 7, 建立数据爱好者生态圈，讨论，分享，产出源（需要有数据相关背景）
# 8, 利益分配，按效分配
# 你好2019，我需要努力挣钱，我还有很多不足之处
# 认真仔细很重要，学会爱也很重要

# 你对数字的准确辨识没有错，可你对数据的深度迷信就大错特错了
# 拆解数字，是解开真相的有效方法，看看下图你是不是怀疑自己的眼睛，如果
# 你还将信将疑，你可以运用数学的加减乘除核对一遍。
# 所以你还会选择那个看似美好数字背后却不美好的高延迟率的 西部航空吗？明白人都不会选择


















# uni_chains 需要添加一条新院线
# uni_name_chains 需要6全称和0简称的检测， 8中影检测
#
# bpm_zoneversion 院线的大版本
# bpm_zonechains 院线甲乙区










