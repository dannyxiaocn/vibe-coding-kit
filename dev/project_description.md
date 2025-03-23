# Vibe-coding-init-kit

## repo 设计
1. Global 和 Project 的，写入 windsurfrules/cursorrules 的 Global 和 Project Rule
	**Global**
	- 语言类设定：
		1. 与人交流语言
		2. 代码 comment 语言
	- 全局外部工具库
	**Project**
	- 项目文档记录：
		1. 项目内容
		2. TODO，目标，Progress 记录
		3. 代码文档说明
		4. 写代码的要求：
			- comment清晰
			- API化书写
			- 控制单文件代码行数
			- 写配套的测试文件 --- 并明确不许写虚假的测试
	- 局部外部工具库
2. 自动安装 MCP
3. CLI：
	- 自动查找/创建`.cursorrules`/`.windsurfrules`等文件，去更改
	- 增加zsh/bash里面的指令，可以来初始化
## 解决方案
Sustainable for maintainance: Vibe coding 导致代码可维护性差 --> 解决这个痛点
	- 代码维护包括：
		1. 需求改动
		2. 需求增加
		3. 上下游更换
	- 手段：
		1. API 化 function 且记录文档
		2. Multi-agent，应用一个 Refactor Agent 来执行更改

- [ ] 根据 Project description 一键生成 todo
- [ ] project 可以 override global 的 rules