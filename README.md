# StarWeb 监控系统 - RS485 数据

## 启动

- python -m flask run

## 所用技术

- 前端
  - NodeJS(语言&环境)+ Vue(框架) + ElementUI(界面) + Echarts(数据可视化) + Axios(前后端交互) + WebSocket(实时数据调取)
- 后端
  - Python(语言) + Flask(框架)
- 串口
  - pySerial / Serial
- 数据存储
  - 方案 1：Mysql 数据库 + SQLAlchemy + Pandas
  - 方案 2：csv + Pandas
- 版本管理
  - Git

## 开发所需软件

- PyCharm(后端开发) + VSCode(前端开发) + Dbeaver(数据库界面)

## 运行所需

- Python 及依赖
  - 镜像源
    - pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simpl
  - pip
    - python -m ensurepip
    - python -m pip install --upgrade pip
    - python -m pip install -U --force-reinstall pip
  - 虚拟环境
    - 设置系统变量 WORKON_HOME
    - pip install virtualenv
    - pip install virtualenvwrapper-win
    - pip install pipenv
    - workon #查看有哪些虚拟环境
    - mkvirtualenv 虚拟环境名称 #新增虚拟环境
    - deactivate #退出虚拟环境
    - rmvirtualenv #删除虚拟环境
    - workon 虚拟环境名称 #进入虚拟环境
  - 依赖库
    - pip install -r requirements.txt
- MySQL 数据库
- git
  - C:\Windows\System32\drivers\etc\hosts
  - 192.30.253.113 github.com
  - 151.101.185.194 github.global.ssl.fastly.net
  - ipconfig /flushdns
  - ssh-keygen
