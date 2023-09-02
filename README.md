简体中文 | [繁体中文](./README_TC.md)



！！！目前精力放在重构项目和自动寻路上！！！



# AutoStarRail

崩坏：星穹铁道自动化 |崩坏：星穹铁道体力消耗自动化 | 自定义清理体力 | 融合`Auto_Simulated_Universe`和`StarRailAssistant`以及清理体力于一体的整合包 | 模拟按键 | 图像识别



## 免责声明

本软件是一个外部工具旨在自动化崩坏星轨的游戏玩法。它被设计成仅通过现有用户界面与游戏交互,并遵守相关法律法规。该软件包旨在提供简化和用户通过功能与游戏交互,并且它不打算以任何方式破坏游戏平衡或提供任何不公平的优势。该软件包不会以任何方式修改任何游戏文件或游戏代码。

This software is open source, free of charge and for learning and exchange purposes only. The developer team has the final right to interpret this project. All problems arising from the use of this software are not related to this project and the developer team. If you encounter a merchant using this software to practice on your behalf and charging for it, it may be the cost of equipment and time, etc. The problems and consequences arising from this software have nothing to do with it.

本软件开源、免费，仅供学习交流使用。开发者团队拥有本项目的最终解释权。使用本软件产生的所有问题与本项目与开发者团队无关。若您遇到商家使用本软件进行代练并收费，可能是设备与时间等费用，产生的问题及后果与本软件无关。

请注意，根据MiHoYo的 [崩坏:星穹铁道的公平游戏宣言](https://sr.mihoyo.com/news/111246?nav=news&type=notice):

```
"严禁使用外挂、加速器、脚本或其他破坏游戏公平性的第三方工具。"
"一经发现，米哈游（下亦称“我们”）将视违规严重程度及违规次数，采取扣除违规收益、冻结游戏账号、永久封禁游戏账号等措施。"
```



## 注意事项

1. 识图为识别游戏画面，游戏不能被任何窗口覆盖

2. 不要修改项目根目录名称，项目搜索路径是向上搜索项目名称，若修改路径则导致项目陷入死循环等。。

3. 自定义体力支持 **拟造花萼**，**凝滞虚影**，**侵蚀隧道**，**历战余响**

4. 清理体力需要角色处于**主界面**(可以看到左上角地图，左上角任务，右边角色栏等)

5. 运行清理体力该功能后尽量不要操作了，断点恢复能力不是很好

6. 暂时不支持副本中死亡继续运行脚本，若中途死亡需要重新运行脚本

7. 路径中不要有中文路径！！！

   ⭐**如果喜欢，点个星星~**⭐

## 运行环境

Python 3.11.4

## 常见问题解答

- [常见问题解答](./doc/readme/CN/常见问题.md)

## 使用方法

- [使用方法](./doc/readme/CN/使用方法.md)

## GUI展示

- [GUI展示](./doc/readme/CN/gui展示.md)

## 参与开发

- 如何参与项目开发(还没想好咋写)
- [如何正确的提Issues？](https://www.bilibili.com/video/BV18T411z7R4/?spm_id_from=333.999.0.0&vd_source=ec620e4f4feee0d5f5bfc246495f7f84)

## ❓我为什么要做这么一个项目

  对于我来说星铁是一款非常有意思的游戏(指的是每次更新的地图，活动，剧情等)，我非常讨厌重复的刷刷刷这让我非常的烦躁，于是我在**github**上寻找相关的项目，当然我找到了，那就是**StarRailAssistant**和**Auto_Simulated_Universe**这两个项目非常有效的延缓我的烦躁，但这还远远不够，我希望每日任务、日常任务、清理体力等都不需要我自己来操作，我还希望每次锄大地都不需要自己录制一下模拟按键只要截下游戏地图然后对地图进行绘制就能实现角色根据路线走路于是我做了这个项目`AutoStarRail`。



## 未来目标

1. ~~GUI~~
2. ~~清理每日体力~~
3. ~~锄大地~~
4. ~~刷模拟宇宙~~
5. ~~领委托任务~~
6. 完成每日任务
7. 使用A-Star算法改进原模拟按键锄大地



