# 简历生成工具 FAQ

## 🎯 关于人员姓名配置

### Q: 人员姓名到底在哪里配置？
**A**: 人员姓名在**第二阶段**的详细配置文件中配置：

1. **第一阶段** (`data/contract_role_mapping.xlsx`)：
   - ❌ **不配置人员姓名**
   - ✅ 配置角色需求（技能、经验、人数等）

2. **第二阶段** (`data/detailed_resume_config.xlsx`)：
   - ✅ **配置人员姓名**
   - ✅ 配置详细个人信息

### Q: 具体操作步骤是什么？
**A**: 
```bash
# 步骤1: 配置角色需求
编辑 data/contract_role_mapping.xlsx
填写 required_skills, experience_years, salary_range
将 mapping_status 改为 "已确认"

# 步骤2: 生成详细配置  
python3 contract_mapper.py

# 步骤3: 配置具体人员信息 ⭐
编辑 data/detailed_resume_config.xlsx
在 persons 工作表中填写 name 列（人员姓名）

# 步骤4: 生成简历
python3 src/main.py --config ./data/detailed_resume_config.xlsx
```

### Q: 为什么分成两个阶段？
**A**: 这样设计的好处：
- **解耦设计**: 角色需求与具体人员分离
- **灵活配置**: 可以先确定需求，再安排人员
- **批量处理**: 同一角色可配置多人
- **易于维护**: 需求变更不影响人员配置

## 📋 配置文件详解

### contract_role_mapping.xlsx（第一阶段）
```
contract_id | role_name | personnel_count | required_skills | experience_years | salary_range | mapping_status
HT2026001   | 项目经理    | 1              | 项目管理,PMP     | 5-8年           | 20K-30K     | 已确认
HT2026001   | 开发工程师  | 3              | Java,Spring     | 3-5年           | 15K-25K     | 已确认
```

### detailed_resume_config.xlsx（第二阶段）
```
persons工作表:
id   | name    | role_id              | email        | phone      | skills
P001 | 张三     | ROLE_HT2026001_项目经理 | zhang@xxx.com | 138xxxxxxx | 项目管理,PMP
P002 | 李四     | ROLE_HT2026001_开发工程师 | li@xxx.com   | 139xxxxxxx | Java,Spring
P003 | 王五     | ROLE_HT2026001_开发工程师 | wang@xxx.com | 137xxxxxxx | Java,Spring
```

## 🔧 常见操作场景

### 场景1: 为现有角色添加新人员
1. 在`detailed_resume_config.xlsx`的`persons`表中添加新行
2. 填写人员姓名和详细信息
3. 确保`role_id`与对应角色匹配

### 场景2: 修改角色的人员数量
1. 修改`contract_role_mapping.xlsx`中的`personnel_count`
2. 重新运行`python3 contract_mapper.py`生成新配置
3. 在新生成的配置中填写人员信息

### 场景3: 一人兼任多角色
1. 在`persons`表中为同一人员创建多行
2. 每行使用不同的`role_id`
3. 填写相应的技能和经验信息

## ⚠️ 注意事项

1. **文件顺序很重要**: 必须先完成第一阶段才能进行第二阶段
2. **ID关联**: `role_id`必须与`roles`表中的`id`匹配
3. **数据一致性**: 确保人员技能与角色要求相符
4. **备份重要**: 配置过程中建议备份重要文件

## 🆘 问题排查

**问题**: 找不到人员姓名配置位置
**解决**: 检查是否已完成第一阶段并生成了详细配置文件

**问题**: 生成的简历中人员信息不完整
**解决**: 确认在`detailed_resume_config.xlsx`的`persons`表中填写了完整信息

**问题**: 角色和人员不匹配
**解决**: 检查`role_id`关联是否正确，确保人员技能符合角色要求

记住：**人员姓名配置在第二阶段的详细配置文件中！**