# 简历生成工具配置说明

## Excel配置文件结构

Excel配置文件需要包含以下几个工作表：

### 1. config (配置表)
| 字段名 | 说明 | 示例值 |
|--------|------|--------|
| contract_id | 合同ID | HT2024001 |
| template_path | 模板文件路径 | ./templates/resume_template.pdf |
| output_dir | 输出目录 | ./output |
| output_format | 输出格式 | pdf/word/both |

### 2. contracts (合同表)
| 字段名 | 说明 | 示例值 |
|--------|------|--------|
| id | 合同ID | HT2024001 |
| name | 合同名称 | XX项目开发合同 |
| client | 客户名称 | XX科技有限公司 |
| start_date | 开始日期 | 2024-01-01 |
| end_date | 结束日期 | 2024-12-31 |
| role_ids | 关联角色ID列表 | ROLE001,ROLE002 |

### 3. roles (角色表)
| 字段名 | 说明 | 示例值 |
|--------|------|--------|
| id | 角色ID | ROLE001 |
| name | 角色名称 | 前端开发工程师 |
| description | 角色描述 | 负责前端页面开发 |
| required_skills | 所需技能 | JavaScript,React,Vue.js |
| person_ids | 关联人员ID列表 | P001,P002,P003 |

### 4. persons (人员表)
| 字段名 | 说明 | 示例值 |
|--------|------|--------|
| id | 人员ID | P001 |
| name | 姓名 | 张三 |
| email | 邮箱 | zhangsan@example.com |
| phone | 电话 | 13800138000 |
| education | 学历 | 本科 |
| work_experience | 工作经历 | 3年前端开发经验 |
| skills | 技能 | JavaScript,React,Vue.js |
| certifications | 证书 | 前端工程师认证 |

## 使用示例

1. 准备好符合上述结构的Excel文件
2. 准备好简历模板文件
3. 运行命令：
   ```bash
   python src/main.py --config ./data/config.xlsx
   ```

## 注意事项

- 日期格式应为 YYYY-MM-DD
- 多个ID用逗号分隔
- 确保各表之间的ID引用关系正确
- 模板文件路径支持相对路径和绝对路径