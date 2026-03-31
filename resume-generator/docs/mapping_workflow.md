# 合同-人员-角色配置工作流程

## 📋 当前状态
工具已成功分析您上传的19个合同文件，并创建了人员-合同-角色映射模板。

## 🚀 配置步骤

### 第一步：配置人员-合同-角色映射
1. **打开映射文件**: `data/contract_role_mapping.xlsx`
2. **填写必要信息**:
   - `required_skills`: 每个角色所需的技能（用逗号分隔）
   - `experience_years`: 经验要求（如：3-5年）
   - `salary_range`: 薪资范围（如：15K-25K）
3. **确认配置**: 将`mapping_status`列中的"待配置"改为"已确认"
4. **保存文件**

### 第二步：生成详细配置文件
运行以下命令生成完整的简历配置文件：
```bash
python3 contract_mapper.py
```
选择生成详细配置文件的选项。

### 第三步：完善详细信息
1. **打开生成的详细配置文件**: `data/detailed_resume_config.xlsx`
2. **完善各工作表信息**:
   - `config`: 公司基本信息
   - `contracts`: 合同详细信息
   - `roles`: 角色具体要求
   - `persons`: 具体人员信息

### 第四步：生成简历
```bash
python3 src/main.py --config ./data/detailed_resume_config.xlsx
```

## 📊 映射文件结构说明

### 主要字段
- `contract_id`: 合同唯一标识
- `contract_name`: 合同名称
- `client_name`: 客户名称
- `role_name`: 角色名称
- `personnel_count`: 需要的人员数量
- `role_description`: 角色描述
- `required_skills`: 必需技能
- `experience_years`: 经验年限
- `salary_range`: 薪资范围
- `mapping_status`: 配置状态（待配置/已确认）

## 💡 使用建议

1. **优先处理重要合同**: 先配置最重要的几个合同
2. **合理设置角色**: 根据实际项目需求调整角色和人数
3. **技能要求具体化**: 详细列出每个角色的具体技能要求
4. **薪资范围合理**: 根据市场行情和公司标准设定

## 🔧 常见问题

**Q: 如何添加新的角色？**
A: 在映射文件中复制一行，修改角色信息即可

**Q: 如何修改人员数量？**
A: 直接修改`personnel_count`列的数值

**Q: 是否可以删除不需要的映射？**
A: 可以直接删除Excel中的相应行

**Q: 配置完成后如何验证？**
A: 运行工具生成详细配置，检查生成的数据是否正确

这个配置流程让用户可以灵活地建立合同、角色和人员之间的对应关系，满足不同项目的需求。