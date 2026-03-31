"""
合同简历生成工具 - Excel配置模板生成器
创建标准化的Excel配置文件模板
"""

import pandas as pd
import os
from datetime import datetime

def create_contract_template():
    """创建合同信息模板"""
    contract_template = {
        '字段名': [
            'id', 'name', 'contract_number', 'client', 'client_address', 
            'client_contact', 'client_phone', 'project_name', 'project_description',
            'start_date', 'end_date', 'contract_amount', 'payment_terms',
            'service_scope', 'deliverables', 'quality_requirements', 'acceptance_criteria'
        ],
        '说明': [
            '合同唯一标识符', '合同名称', '合同编号', '客户名称', '客户地址',
            '客户联系人', '客户联系电话', '项目名称', '项目描述',
            '合同开始日期', '合同结束日期', '合同金额', '付款条款',
            '服务范围', '交付物', '质量要求', '验收标准'
        ],
        '示例值': [
            'HT2024001', 'XX系统开发合同', 'CD2024-SW-001', 'XX科技有限公司', '北京市朝阳区XX路XX号',
            '张经理', '010-12345678', '企业管理系统开发', '开发一套完整的企业管理系统',
            '2024-01-01', '2024-12-31', '500000', '预付款30%，验收后付70%',
            '需求分析、系统设计、编码实现、测试部署', '系统源代码、技术文档、用户手册',
            '符合国家标准、性能稳定、安全可靠', '功能完整、性能达标、文档齐全'
        ],
        '数据类型': [
            '文本', '文本', '文本', '文本', '文本',
            '文本', '文本', '文本', '文本',
            '日期', '日期', '数字', '文本',
            '文本', '文本', '文本', '文本'
        ]
    }
    
    return pd.DataFrame(contract_template)

def create_role_template():
    """创建角色信息模板"""
    role_template = {
        '字段名': [
            'id', 'name', 'contract_id', 'description', 'responsibilities',
            'required_skills', 'experience_years', 'education_requirement',
            'person_count', 'salary_range', 'work_location'
        ],
        '说明': [
            '角色唯一标识符', '角色名称', '所属合同ID', '角色描述', '主要职责',
            '所需技能', '经验要求(年)', '学历要求', '人员数量',
            '薪资范围', '工作地点'
        ],
        '示例值': [
            'ROLE001', '高级Java开发工程师', 'HT2024001', '负责后端系统开发', '系统设计、编码实现、技术攻关',
            'Java,Spring Boot,MySQL,Redis', '3-5', '本科及以上', '2',
            '15K-25K', '北京'
        ],
        '数据类型': [
            '文本', '文本', '文本', '文本', '文本',
            '文本', '数字', '文本', '数字',
            '文本', '文本'
        ]
    }
    
    return pd.DataFrame(role_template)

def create_person_template():
    """创建人员信息模板"""
    person_template = {
        '字段名': [
            'id', 'name', 'role_id', 'id_card', 'gender', 'birth_date',
            'email', 'phone', 'emergency_contact', 'emergency_phone',
            'education', 'school', 'major', 'graduation_year',
            'work_experience', 'current_company', 'current_position',
            'skills', 'certifications', 'languages', 'expected_salary'
        ],
        '说明': [
            '人员唯一标识符', '姓名', '所属角色ID', '身份证号', '性别', '出生日期',
            '邮箱', '手机号', '紧急联系人', '紧急联系电话',
            '最高学历', '毕业院校', '专业', '毕业年份',
            '工作经历', '当前公司', '当前职位',
            '专业技能', '获得证书', '掌握语言', '期望薪资'
        ],
        '示例值': [
            'P001', '张三', 'ROLE001', '110101199001011234', '男', '1990-01-01',
            'zhangsan@email.com', '13800138000', '李四', '13800138001',
            '本科', '清华大学', '计算机科学与技术', '2015',
            '5年Java开发经验，熟悉Spring生态', 'XX科技有限公司', '高级工程师',
            'Java,Spring Boot,MySQL,Redis,Docker', 'Oracle认证专家,OCP', '中文(母语),英语(熟练)', '18000'
        ],
        '数据类型': [
            '文本', '文本', '文本', '文本', '文本', '日期',
            '文本', '文本', '文本', '文本',
            '文本', '文本', '文本', '数字',
            '文本', '文本', '文本',
            '文本', '文本', '文本', '数字'
        ]
    }
    
    return pd.DataFrame(person_template)

def create_config_template():
    """创建配置信息模板"""
    config_template = {
        '字段名': [
            'contract_id', 'template_path', 'output_dir', 'output_format',
            'company_name', 'company_address', 'company_phone', 'logo_path'
        ],
        '说明': [
            '要生成简历的合同ID', '简历模板文件路径', '简历输出目录', '输出格式(pdf/word/both)',
            '公司名称', '公司地址', '公司电话', '公司Logo路径'
        ],
        '示例值': [
            'HT2024001', './templates/resume_template.docx', './output', 'both',
            'XX信息技术有限公司', '北京市海淀区XX路XX号', '010-12345678', './assets/logo.png'
        ],
        '数据类型': [
            '文本', '文本', '文本', '文本',
            '文本', '文本', '文本', '文本'
        ]
    }
    
    return pd.DataFrame(config_template)

def generate_excel_templates():
    """生成完整的Excel配置模板"""
    # 创建模板目录
    template_dir = "./templates/config_templates"
    os.makedirs(template_dir, exist_ok=True)
    
    # 生成各个模板
    templates = {
        'contract_template': create_contract_template(),
        'role_template': create_role_template(),
        'person_template': create_person_template(),
        'config_template': create_config_template()
    }
    
    # 保存为单独的Excel文件
    for name, df in templates.items():
        file_path = os.path.join(template_dir, f"{name}.xlsx")
        df.to_excel(file_path, index=False)
        print(f"✓ 已生成模板: {file_path}")
    
    # 生成综合模板（所有表格在一个文件中）
    combined_file = os.path.join(template_dir, "resume_config_template.xlsx")
    with pd.ExcelWriter(combined_file, engine='openpyxl') as writer:
        create_config_template().to_excel(writer, sheet_name='config', index=False)
        create_contract_template().to_excel(writer, sheet_name='contracts', index=False)
        create_role_template().to_excel(writer, sheet_name='roles', index=False)
        create_person_template().to_excel(writer, sheet_name='persons', index=False)
        
        # 添加说明工作表
        instructions = {
            '使用说明': [
                '1. 请在config工作表中填写配置信息',
                '2. 请在contracts工作表中填写合同信息',
                '3. 请在roles工作表中填写角色信息',
                '4. 请在persons工作表中填写人员信息',
                '5. 确保ID引用关系正确（角色的contract_id要对应合同的id）',
                '6. 保存文件后使用工具生成简历'
            ]
        }
        pd.DataFrame(instructions).to_excel(writer, sheet_name='使用说明', index=False)
    
    print(f"✓ 已生成综合模板: {combined_file}")
    print(f"\n模板文件已生成至: {os.path.abspath(template_dir)}")
    return combined_file

def create_sample_filled_template():
    """创建已填充示例数据的模板"""
    template_dir = "./templates/sample_configs"
    os.makedirs(template_dir, exist_ok=True)
    
    # 创建示例数据
    sample_data = {}
    
    # 示例合同数据
    sample_contracts = pd.DataFrame({
        'id': ['HT2024001', 'HT2024002'],
        'name': ['企业管理系统开发合同', '移动应用开发合同'],
        'contract_number': ['CD2024-SW-001', 'CD2024-YD-001'],
        'client': ['XX科技有限公司', 'YY互联网公司'],
        'client_address': ['北京市朝阳区XX路XX号', '上海市浦东新区XX路XX号'],
        'client_contact': ['张经理', '李总监'],
        'client_phone': ['010-12345678', '021-87654321'],
        'project_name': ['企业管理系统', '移动办公应用'],
        'project_description': ['开发一套完整的企业管理系统', '开发移动端办公应用'],
        'start_date': ['2024-01-01', '2024-03-01'],
        'end_date': ['2024-12-31', '2024-09-30'],
        'contract_amount': [500000, 300000],
        'payment_terms': ['预付款30%，验收后付70%', '分期付款'],
        'service_scope': ['全栈开发服务', '移动端开发'],
        'deliverables': ['源代码、文档、培训', 'APP、后台系统'],
        'quality_requirements': ['符合国家标准', '高性能、高可用'],
        'acceptance_criteria': ['功能完整、性能达标', '用户体验良好']
    })
    
    # 示例角色数据
    sample_roles = pd.DataFrame({
        'id': ['ROLE001', 'ROLE002', 'ROLE003', 'ROLE004'],
        'name': ['高级Java开发工程师', '前端开发工程师', 'UI设计师', '测试工程师'],
        'contract_id': ['HT2024001', 'HT2024001', 'HT2024002', 'HT2024002'],
        'description': ['负责后端系统架构设计', '负责前端页面开发', '负责界面设计', '负责质量保证'],
        'responsibilities': ['系统设计、编码实现', '前端开发、交互优化', '界面设计、用户体验', '测试用例设计、缺陷跟踪'],
        'required_skills': ['Java,Spring Boot,MySQL', 'JavaScript,React,Vue.js', 'Photoshop,Figma,Sketch', '自动化测试,性能测试'],
        'experience_years': [3, 2, 3, 2],
        'education_requirement': ['本科及以上', '本科及以上', '本科及以上', '本科及以上'],
        'person_count': [2, 2, 1, 1],
        'salary_range': ['15K-25K', '12K-20K', '10K-18K', '8K-15K'],
        'work_location': ['北京', '北京', '上海', '上海']
    })
    
    # 示例人员数据
    sample_persons = pd.DataFrame({
        'id': ['P001', 'P002', 'P003', 'P004', 'P005', 'P006'],
        'name': ['张三', '李四', '王五', '赵六', '钱七', '孙八'],
        'role_id': ['ROLE001', 'ROLE001', 'ROLE002', 'ROLE002', 'ROLE003', 'ROLE004'],
        'id_card': ['110101199001011234', '110101199102022345', '110101199203033456', '110101199304044567', '110101199405055678', '110101199506066789'],
        'gender': ['男', '男', '女', '男', '女', '男'],
        'birth_date': ['1990-01-01', '1991-02-02', '1992-03-03', '1993-04-04', '1994-05-05', '1995-06-06'],
        'email': ['zhangsan@email.com', 'lisi@email.com', 'wangwu@email.com', 'zhaoliu@email.com', 'qianqi@email.com', 'sunba@email.com'],
        'phone': ['13800138000', '13800138001', '13800138002', '13800138003', '13800138004', '13800138005'],
        'emergency_contact': ['父亲', '母亲', '配偶', '朋友', '家人', '同事'],
        'emergency_phone': ['13800138006', '13800138007', '13800138008', '13800138009', '13800138010', '13800138011'],
        'education': ['本科', '硕士', '本科', '本科', '硕士', '本科'],
        'school': ['清华大学', '北京大学', '北京航空航天大学', '北京理工大学', '中央美术学院', '北京邮电大学'],
        'major': ['计算机科学与技术', '软件工程', '电子信息工程', '通信工程', '视觉传达设计', '计算机科学与技术'],
        'graduation_year': [2015, 2018, 2016, 2017, 2019, 2020],
        'work_experience': ['5年Java开发经验', '3年Java开发经验', '4年前端开发经验', '3年前端开发经验', '5年UI设计经验', '3年测试经验'],
        'current_company': ['ABC科技', 'DEF软件', 'GHI网络', 'JKL信息', 'MNO设计', 'PQR测试'],
        'current_position': ['高级工程师', '工程师', '高级前端', '前端', '设计主管', '测试主管'],
        'skills': ['Java,Spring Boot,MySQL,Redis', 'Java,微服务,分布式', 'JavaScript,React,Vue.js,CSS3', 'JavaScript,小程序,移动端', 'Photoshop,Figma,用户体验', '自动化测试,性能测试,JMeter'],
        'certifications': ['OCP认证,软考高级', '软考中级', '前端认证', '移动开发认证', 'Adobe认证,设计奖项', 'ISTQB认证'],
        'languages': ['中文(母语),英语(熟练)', '中文(母语),英语(良好)', '中文(母语),英语(熟练)', '中文(母语),英语(良好)', '中文(母语),英语(流利)', '中文(母语),英语(熟练)'],
        'expected_salary': [18000, 15000, 16000, 13000, 14000, 12000]
    })
    
    # 示例配置数据
    sample_config = pd.DataFrame({
        'contract_id': ['HT2024001'],
        'template_path': ['./templates/resume_template.docx'],
        'output_dir': ['./output'],
        'output_format': ['both'],
        'company_name': ['XX信息技术有限公司'],
        'company_address': ['北京市海淀区XX路XX号'],
        'company_phone': ['010-12345678'],
        'logo_path': ['./assets/logo.png']
    })
    
    # 保存示例配置
    sample_file = os.path.join(template_dir, "sample_filled_config.xlsx")
    with pd.ExcelWriter(sample_file, engine='openpyxl') as writer:
        sample_config.to_excel(writer, sheet_name='config', index=False)
        sample_contracts.to_excel(writer, sheet_name='contracts', index=False)
        sample_roles.to_excel(writer, sheet_name='roles', index=False)
        sample_persons.to_excel(writer, sheet_name='persons', index=False)
    
    print(f"✓ 已生成示例配置: {sample_file}")
    return sample_file

if __name__ == "__main__":
    print("=== 简历生成工具配置模板生成器 ===\n")
    
    # 生成空白模板
    print("1. 生成空白配置模板...")
    template_file = generate_excel_templates()
    
    # 生成示例数据模板
    print("\n2. 生成示例数据模板...")
    sample_file = create_sample_filled_template()
    
    print(f"\n=== 模板生成完成 ===")
    print(f"空白模板: {template_file}")
    print(f"示例模板: {sample_file}")
    print(f"\n用户只需:")
    print("1. 复制相应模板文件")
    print("2. 填写实际业务数据")
    print("3. 运行简历生成工具")