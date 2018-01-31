# ServerOB (Building)

## 设计目的 ##

构建一个自动化监控平台，监控系统并以邮件或微信的方式向管理员及时推送提醒信息。

## 设计理念 ##

- 自动化运维工具容易给人一种难以上手的感觉；
- 虽然ansible已经设计得非常简洁，但在配置上仍旧有些麻烦；

---

- 提供一个最简单的web页面用于交互与输入配置，以替代简陋的终端；
- 主机管理上基于ansible，所有操作均在管理主机上完成，服务端完全不需要多余配置；
- 在告警方面，分别提供两种较官方与较便捷的方式：邮件与微信，便于及时提醒管理员；
- 使用插件架构进行全模块的开发，提供良好的后期扩展。
- 基于linux主机，python2.7

## 架构 ##

- web交互层
	- 提供一个方便操作的交互界面
	- 功能
	    - 登录与身份验证
		- 被管主机状态检测
		- 一些配置的修改
		- 传递参数给管理主机
		- 执行ansible命令
	- 模块 (flask + bootstrap)
		- 身份校验(安全)
		- 主机状态检测
		- 与服务层的通信
    - 数据
        - sqlite3 / mysql
        
- 服务层
	- 承接前端的请求与被管主机的状态
	- 功能
		- 根据前端传递的信息通过ssh向被管主机发送请求
		- 处理被管主机返回的信息并做相应处理
	- 模块
		- 监控模块
			- 监控频率
			- 监控提醒方式
			- 推送对象
		- 定时任务模块
			- 定时器
			- 任务列表
		- 命令执行模块
			- ansible
			- 终端命令
			- python