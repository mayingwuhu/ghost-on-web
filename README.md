# ghost-on-web
Virtual weibo bot
data_clean: 数据清洗
dataset:爬下来的原始数据
paddleTest：paddle的ernie-gen模型测试



## 目标

**粉圈生成器**

输入主题（tag） 输出微博

同时做“虚拟用户”的效果测试：用微博小号，拿着生成的微博去回复一些明星关键词下的微博（包括粉丝，黑子，路人等等，不要有人工选择性 ) ，看看别人会回复什么



## 目前任务

**数据爬取**-已有若干xz粉的微博

**数据清洗**-需要去掉@ 提取出#tag# 去掉url 分割转发内容，最终格式应该是[tag-相应微博].

如果原始数据包含多个tag，那么可以形成多条数据，不同tag对应通一条微博

**训练**-已初步测试ernie-gen，待验证清洗后效果

**虚拟用户测试**-需要可用的微博小号，不要绑我们自己的手机号，以免出意外

**部署模型**

**整理发布**



### 3.22更新

项目“僵尸虾生成器”共享链接(有效期三天)：https://aistudio.baidu.com/studio/project/partial/verify/1673999/87adf66134354ccba0b3971be2eb5ee4

**数据爬取，数据清洗，训练：**

已测试数据清洗和重新训练， 比之前效果好， 但是过拟合仍然严重

其实原本数据集内有很多不错的内容，但是由于过拟合严重，基本生成不出来。

<u>需要进一步处理数据</u>。或许可以多复制几份这一块的内容（人为把内容稍加修改），加上打榜内容，合成一个大点的数据集，随机shuffle打乱再训练




**虚拟用户测试**-已有一个小号，待测试

**部署模型，整理发布**-周四前完成并传b站，aistudio自带部署功能，正在看，有空的话真像整个好玩的网站


### 3.24更新

演示视频：https://www.bilibili.com/video/BV1CK4y127ua

CSDN：https://blog.csdn.net/weixin_39742497/article/details/115129404

aistudio notebook：https://aistudio.baidu.com/aistudio/projectdetail/1673999
