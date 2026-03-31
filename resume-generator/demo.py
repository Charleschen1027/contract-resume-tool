"""
简化版简历生成器
用于快速验证核心功能
"""

import pandas as pd
import os
from datetime import datetime
from dataclasses import dataclass
from typing import List
import logging

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class Person:
    """简化版人员信息"""
    name: str
    email: str
    phone: str
    education: str
    work_experience: str
    skills: str
    certifications: str

def create_sample_data():
    """创建示例数据"""
    # 创建示例Excel文件
    data_dir = "./data"
    os.makedirs(data_dir, exist_ok=True)
    
    # 人员数据
    persons_data = {
        'id': ['P001', 'P002'],
        'name': ['张三', '李四'],
        'email': ['zhangsan@example.com', 'lisi@example.com'],
        'phone': ['13800138000', '13800138001'],
        'education': ['本科', '硕士'],
        'work_experience': ['3年前端开发经验', '5年后端开发经验'],
        'skills': ['JavaScript,React,Vue.js', 'Python,Django,MySQL'],
        'certifications': ['前端工程师认证', '后端工程师认证']
    }
    
    persons_df = pd.DataFrame(persons_data)
    
    # 角色数据
    roles_data = {
        'id': ['ROLE001', 'ROLE002'],
        'name': ['前端开发工程师', '后端开发工程师'],
        'description': ['负责前端页面开发', '负责后端服务开发'],
        'required_skills': ['JavaScript,React', 'Python,Django'],
        'person_ids': ['P001', 'P002']
    }
    
    roles_df = pd.DataFrame(roles_data)
    
    # 合同数据
    contracts_data = {
        'id': ['HT2024001'],
        'name': ['软件开发项目'],
        'client': ['XX科技有限公司'],
        'start_date': ['2024-01-01'],
        'end_date': ['2024-12-31'],
        'role_ids': ['ROLE001,ROLE002']
    }
    
    contracts_df = pd.DataFrame(contracts_data)
    
    # 配置数据
    config_data = {
        'contract_id': ['HT2024001'],
        'template_path': ['./templates/sample_template.txt'],
        'output_dir': ['./output'],
        'output_format': ['txt']
    }
    
    config_df = pd.DataFrame(config_data)
    
    # 保存到Excel文件
    excel_path = os.path.join(data_dir, "sample_config.xlsx")
    with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
        config_df.to_excel(writer, sheet_name='config', index=False)
        contracts_df.to_excel(writer, sheet_name='contracts', index=False)
        roles_df.to_excel(writer, sheet_name='roles', index=False)
        persons_df.to_excel(writer, sheet_name='persons', index=False)
    
    logger.info(f"示例数据已创建: {excel_path}")
    return excel_path

def read_config(excel_path: str):
    """读取配置"""
    logger.info("读取配置文件...")
    
    # 读取各个工作表
    config_df = pd.read_excel(excel_path, sheet_name='config')
    persons_df = pd.read_excel(excel_path, sheet_name='persons')
    roles_df = pd.read_excel(excel_path, sheet_name='roles')
    contracts_df = pd.read_excel(excel_path, sheet_name='contracts')
    
    # 读取配置
    config = config_df.iloc[0]
    output_dir = config['output_dir']
    
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)
    
    # 转换人员数据
    persons = []
    for _, row in persons_df.iterrows():
        person = Person(
            name=row['name'],
            email=row['email'],
            phone=row['phone'],
            education=row['education'],
            work_experience=row['work_experience'],
            skills=row['skills'],
            certifications=row['certifications']
        )
        persons.append(person)
    
    logger.info(f"读取到 {len(persons)} 个人员信息")
    return persons, output_dir

def generate_simple_resume(person: Person, output_path: str):
    """生成简单的文本格式简历"""
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("=" * 50 + "\n")
            f.write(f"个人简历\n")
            f.write("=" * 50 + "\n\n")
            
            f.write(f"姓名: {person.name}\n")
            f.write(f"邮箱: {person.email}\n")
            f.write(f"电话: {person.phone}\n")
            f.write(f"学历: {person.education}\n\n")
            
            f.write("工作经历:\n")
            f.write("-" * 20 + "\n")
            f.write(f"{person.work_experience}\n\n")
            
            if person.skills:
                f.write("专业技能:\n")
                f.write("-" * 20 + "\n")
                f.write(f"{person.skills}\n\n")
            
            if person.certifications:
                f.write("相关证书:\n")
                f.write("-" * 20 + "\n")
                f.write(f"{person.certifications}\n\n")
            
            f.write(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        logger.info(f"简历已生成: {output_path}")
        return True
    except Exception as e:
        logger.error(f"生成简历失败: {e}")
        return False

def main():
    """主函数"""
    print("=== 简历生成工具演示 ===\n")
    
    # 创建示例数据
    excel_path = create_sample_data()
    
    # 读取配置
    persons, output_dir = read_config(excel_path)
    
    # 生成简历
    success_count = 0
    for person in persons:
        filename = f"{person.name}_简历.txt"
        output_path = os.path.join(output_dir, filename)
        
        if generate_simple_resume(person, output_path):
            success_count += 1
    
    # 输出结果
    print(f"\n生成完成!")
    print(f"总计: {len(persons)} 份简历")
    print(f"成功: {success_count} 份")
    print(f"输出目录: {os.path.abspath(output_dir)}")

if __name__ == "__main__":
    main()