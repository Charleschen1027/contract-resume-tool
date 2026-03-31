"""
人员姓名配置说明和完整流程演示
"""

import pandas as pd
from pathlib import Path

def show_complete_workflow():
    """展示完整的人员配置流程"""
    
    print("=== 人员姓名配置完整流程 ===\n")
    
    print("📋 阶段一：合同-角色映射配置")
    print("文件: data/contract_role_mapping.xlsx")
    print("目的: 确定每个合同需要哪些角色")
    print("包含字段:")
    print("  - contract_id: 合同ID")
    print("  - role_name: 角色名称") 
    print("  - personnel_count: 需要的人员数量")
    print("  - required_skills: 必需技能")
    print("  - experience_years: 经验要求")
    print("  - salary_range: 薪资范围")
    print("  ❌ 不包含具体人员姓名\n")
    
    print("📋 阶段二：详细人员信息配置")
    print("文件: data/detailed_resume_config.xlsx (由工具自动生成)")
    print("目的: 为每个角色配置具体的人员信息")
    print("包含字段:")
    print("  - id: 人员ID")
    print("  - name: ✅ 人员姓名 (需要用户填写)")
    print("  - role_id: 关联的角色ID")
    print("  - email: 邮箱")
    print("  - phone: 电话")
    print("  - education: 学历")
    print("  - work_experience: 工作经历")
    print("  - skills: 技能")
    print("  - certifications: 证书")
    print("  等详细个人信息字段\n")
    
    print("🎯 完整操作步骤:")
    print("1. 编辑 data/contract_role_mapping.xlsx")
    print("   - 填写技能要求、经验年限、薪资范围")
    print("   - 确认角色和人员数量")
    print("   - 将mapping_status改为'已确认'")
    print()
    print("2. 运行: python3 contract_mapper.py")
    print("   - 工具会生成 data/detailed_resume_config.xlsx")
    print()
    print("3. 编辑 data/detailed_resume_config.xlsx")
    print("   - 在persons工作表中填写具体的人员姓名和其他信息")
    print("   - 每个角色会根据personnel_count生成相应数量的人员模板")
    print()
    print("4. 运行简历生成: python3 src/main.py --config ./data/detailed_resume_config.xlsx")

def create_personnel_template_example():
    """创建人员配置模板示例"""
    
    # 模拟生成的详细配置中的人员表结构
    personnel_template = pd.DataFrame([
        {
            'id': 'P001',
            'name': '待填写_项目经理_1',  # 用户需要修改这里
            'role_id': 'ROLE_HT20260331001_项目经理',
            'email': '',  # 用户填写
            'phone': '',  # 用户填写
            'education': '',  # 用户填写
            'work_experience': '',  # 用户填写
            'skills': '项目管理,PMP认证,团队协调',  # 从角色要求继承
            'certifications': '',  # 用户填写
            'expected_salary': ''  # 用户填写
        },
        {
            'id': 'P002', 
            'name': '待填写_高级开发工程师_1',
            'role_id': 'ROLE_HT20260331001_高级开发工程师',
            'email': '',
            'phone': '',
            'education': '',
            'work_experience': '',
            'skills': 'Java,Spring Boot,MySQL,Redis',  # 从角色要求继承
            'certifications': '',
            'expected_salary': ''
        },
        {
            'id': 'P003',
            'name': '待填写_高级开发工程师_2', 
            'role_id': 'ROLE_HT20260331001_高级开发工程师',
            'email': '',
            'phone': '',
            'education': '',
            'work_experience': '',
            'skills': 'Java,Spring Boot,MySQL,Redis',  # 从角色要求继承
            'certifications': '',
            'expected_salary': ''
        }
    ])
    
    # 保存示例模板
    template_file = Path("./data/personnel_template_example.xlsx")
    personnel_template.to_excel(template_file, index=False)
    print(f"\n✅ 人员配置示例已创建: {template_file}")

def main():
    show_complete_workflow()
    create_personnel_template_example()
    
    print("\n💡 重点提醒:")
    print("• contract_role_mapping.xlsx 中配置的是角色需求")
    print("• detailed_resume_config.xlsx 中配置的是具体人员信息")
    print("• 人员姓名在第二阶段的详细配置中填写")
    print("• 每个角色会根据配置的数量自动生成相应数量的人员模板")

if __name__ == "__main__":
    main()