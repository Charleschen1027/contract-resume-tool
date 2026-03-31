# 简历生成工具使用指南

## 📋 概述
本工具可根据Excel配置文件批量生成个性化简历，支持PDF和Word格式输出。

## 📁 模板文件说明

### 1. 综合配置模板
**文件**: `templates/config_templates/resume_config_template.xlsx`

包含四个工作表：
- **config**: 全局配置信息
- **contracts**: 合同信息
- **roles**: 角色信息  
- **persons**: 人员信息

### 2. 示例配置文件
**文件**: `templates/sample_configs/sample_filled_config.xlsx`

已填充示例数据的配置文件，可直接参考使用。

## 📊 配置表格字段说明

### config 工作表（全局配置）
| 字段名 | 说明 | 示例值 |
|--------|------|--------|
| contract_id | 要生成简历的合同ID | HT2024001 |
| template_path | 简历模板文件路径 | ./templates/resume_template.docx |
| output_dir | 简历输出目录 | ./output |
| output_format | 输出格式 | pdf/word/both |
| company_name | 公司名称 | XX信息技术有限公司 |
| company_address | 公司地址 | 北京市海淀区XX路XX号 |
| company_phone | 公司电话 | 010-12345678 |
| logo_path | 公司Logo路径 | ./assets/logo.png |

### contracts 工作表（合同信息）
| 字段名 | 说明 | 示例值 |
|--------|------|--------|
| id | 合同唯一标识符 | HT2024001 |
| name | 合同名称 | XX系统开发合同 |
| contract_number | 合同编号 | CD2024-SW-001 |
| client | 客户名称 | XX科技有限公司 |
| client_address | 客户地址 | 北京市朝阳区XX路XX号 |
| client_contact | 客户联系人 | 张经理 |
| client_phone | 客户联系电话 | 010-12345678 |
| project_name | 项目名称 | 企业管理系统开发 |
| project_description | 项目描述 | 开发一套完整的企业管理系统 |
| start_date | 合同开始日期 | 2024-01-01 |
| end_date | 合同结束日期 | 2024-12-31 |
| contract_amount | 合同金额 | 500000 |
| payment_terms | 付款条款 | 预付款30%，验收后付70% |
| service_scope | 服务范围 | 需求分析、系统设计、编码实现、测试部署 |
| deliverables | 交付物 | 系统源代码、技术文档、用户手册 |
| quality_requirements | 质量要求 | 符合国家标准、性能稳定、安全可靠 |
| acceptance_criteria | 验收标准 | 功能完整、性能达标、文档齐全 |

### roles 工作表（角色信息）
| 字段名 | 说明 | 示例值 |
|--------|------|--------|
| id | 角色唯一标识符 | ROLE001 |
| name | 角色名称 | 高级Java开发工程师 |
| contract_id | 所属合同ID | HT2024001 |
| description | 角色描述 | 负责后端系统开发 |
| responsibilities | 主要职责 | 系统设计、编码实现、技术攻关 |
| required_skills | 所需技能 | Java,Spring Boot,MySQL,Redis |
| experience_years | 经验要求(年) | 3-5 |
| education_requirement | 学历要求 | 本科及以上 |
| person_count | 人员数量 | 2 |
| salary_range | 薪资范围 | 15K-25K |
| work_location | 工作地点 | 北京 |

### persons 工作表（人员信息）
| 字段名 | 说明 | 示例值 |
|--------|------|--------|
| id | 人员唯一标识符 | P001 |
| name | 姓名 | 张三 |
| role_id | 所属角色ID | ROLE001 |
| id_card | 身份证号 | 110101199001011234 |
| gender | 性别 | 男 |
| birth_date | 出生日期 | 1990-01-01 |
| email | 邮箱 | zhangsan@email.com |
| phone | 手机号 | 13800138000 |
| emergency_contact | 紧急联系人 | 李四 |
| emergency_phone | 紧急联系电话 | 13800138001 |
| education | 最高学历 | 本科 |
| school | 毕业院校 | 清华大学 |
| major | 专业 | 计算机科学与技术 |
| graduation_year | 毕业年份 | 2015 |
| work_experience | 工作经历 | 5年Java开发经验，熟悉Spring生态 |
| current_company | 当前公司 | XX科技有限公司 |
| current_position | 当前职位 | 高级工程师 |
| skills | 专业技能 | Java,Spring Boot,MySQL,Redis,Docker |
| certifications | 获得证书 | Oracle认证专家,OCP |
| languages | 掌握语言 | 中文(母语),英语(熟练) |
| expected_salary | 期望薪资 | 18000 |

## 🚀 使用步骤

### 1. 准备工作
```bash
# 进入项目目录
cd resume-generator

# 安装依赖（如未安装）
pip3 install -r requirements.txt
```

### 2. 选择模板
- **新手用户**: 使用 `templates/sample_configs/sample_filled_config.xlsx`
- **有经验用户**: 使用 `templates/config_templates/resume_config_template.xlsx`

### 3. 填写配置
1. 复制选中的模板文件到 `data/` 目录
2. 按照字段说明填写实际业务数据
3. 确保ID引用关系正确：
   - roles.contract_id → contracts.id
   - persons.role_id → roles.id

### 4. 运行生成器
```bash
# 基本使用
python3 src/main.py --config ./data/your_config.xlsx

# 指定输出目录
python3 src/main.py --config ./data/your_config.xlsx --output ./my_output

# 详细输出模式
python3 src/main.py --config ./data/your_config.xlsx --verbose
```

### 5. 查看结果
生成的简历文件将保存在指定的输出目录中，文件命名格式为：`姓名_角色.扩展名`

## ⚠️ 注意事项

1. **数据验证**: 确保必填字段不为空
2. **ID唯一性**: 各表中的id字段必须唯一
3. **引用关系**: 确保外键引用的有效性
4. **日期格式**: 使用YYYY-MM-DD格式
5. **多值字段**: 技能、证书等多值字段用逗号分隔
6. **文件路径**: 模板路径支持相对路径和绝对路径

## 🔧 高级配置

### 自定义简历模板
1. 准备Word或PDF模板文件
2. 在模板中使用占位符（如{{name}}, {{email}}等）
3. 在config表中指定模板路径

### 批量处理多个合同
1. 在Excel中准备多个合同的数据
2. 分别为每个合同生成配置文件
3. 依次运行生成器处理

## 📞 技术支持

如遇问题，请检查：
1. 日志文件位置：`logs/resume_generator.log`
2. 输出目录权限
3. 依赖包是否完整安装
4. Excel文件格式是否正确

## 📎 附录

### 常见问题
Q: 生成的简历格式不正确怎么办？
A: 检查模板文件路径和格式是否正确

Q: 某些字段没有显示在简历中？
A: 检查模板中是否包含相应的占位符

Q: 如何添加自定义字段？
A: 在Excel模板中添加字段，并在生成器代码中相应修改