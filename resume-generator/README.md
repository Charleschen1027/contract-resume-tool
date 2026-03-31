# 简历生成工具

## 项目概述
一个基于配置表的批量简历生成工具，支持从Excel配置文件读取合同、人员、角色信息，结合PDF模板批量生成个性化简历。

## 功能特点
- 📊 支持Excel配置文件读取
- 📄 支持PDF/Word格式简历生成
- ⚡ 批量处理，支持进度显示
- 🎯 灵活的模板系统
- 📋 详细的日志记录
- 🔧 易于扩展的模块化设计

## 技术栈
- Python 3.8+
- pandas (Excel处理)
- python-docx (Word生成)
- reportlab (PDF生成)
- Jinja2 (模板引擎)

## 目录结构
```
resume-generator/
├── src/              # 源代码目录
│   ├── core/         # 核心业务逻辑
│   ├── data/         # 数据处理模块
│   ├── generator/    # 文档生成模块
│   ├── utils/        # 工具函数
│   └── ui/           # 用户界面
├── templates/        # 简历模板文件
├── data/            # 配置数据文件
├── output/          # 生成的简历文件
├── tests/           # 测试文件
└── docs/            # 文档
```

## 快速开始
1. 安装依赖：`pip install -r requirements.txt`
2. 准备配置文件和模板
3. 运行生成器：`python src/main.py`

## 配置说明
详见 `config.yaml` 配置文件说明