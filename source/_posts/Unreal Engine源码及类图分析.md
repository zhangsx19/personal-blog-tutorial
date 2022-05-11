---
title: Unreal Engine源码及类图分析
date: 2022-04-10 16:26:17
categories:
- CS
- security
tags:
- security
toc: true
---
**Unreal Engine源码及类图分析**
<!-- more -->
# 一、目录
```
Engine——包含构成引擎的所有源代码、内容等。
Templates——创建新项目 时可用的项目模板集合。
GenerateProjectFiles.bat——用于创建在Visual Studio中使用引擎和游戏所需的UE4解决方案和项目文件。请参阅自动项目文件生成 以了解详细信息。
UE4Games.uprojectdirs——这是帮助文件，用于告知UnrealBuildTool默认情况下查找项目的位置。
我们主要关注Engine文件夹里面内容.打开Engine文件夹,源码放在Source文件夹中
Source:主要分为5大内容，有Developer，Editor，Programs，Runtime，ThirdParty，游戏引擎核心代码放在Runtime中
Runtime中，相当于main的启动过程，和初始窗口和显卡部分
```