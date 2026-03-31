"""
合同分析和配置工具
用于分析合同内容并建立人员-合同-角色对应关系
"""

import os
import pandas as pd
from pathlib import Path
from datetime import datetime
import re

class ContractAnalyzer:
    """合同分析器"""
    
    def __init__(self, contracts_dir="./contracts"):
        self.contracts_dir = Path(contracts_dir)
        self.contracts_data = []
        
    def analyze_contracts(self):
        """分析所有合同文件"""
        if not self.contracts_dir.exists():
            print(f"❌ 合同目录不存在: {self.contracts_dir}")
            return False
            
        contract_files = list(self.contracts_dir.glob("*.docx"))
        if not contract_files:
            print("❌ 未找到合同文件")
            return False
            
        print(f"🔍 找到 {len(contract_files)} 个合同文件")
        
        for contract_file in contract_files:
            contract_info = self._extract_contract_info(contract_file)
            if contract_info:
                self.contracts_data.append(contract_info)
                print(f"✓ 分析完成: {contract_file.name}")
            else:
                print(f"⚠️ 无法分析: {contract_file.name}")
        
        return len(self.contracts_data) > 0
    
    def _extract_contract_info(self, file_path):
        """从合同文件中提取基本信息"""
        # 从文件名提取信息（临时方案）
        filename = file_path.stem
        parts = filename.split('_')
        
        # 提取合同编号和名称
        contract_number = ""
        contract_name = ""
        
        # 常见的合同编号模式
        number_patterns = [
            r'[A-Z]{2,}\d{4}[A-Z]?\d{2,}',  # 如 CD2024SW001
            r'\d{4}[A-Z]{2}\d{2,}',         # 如 2024SW001
            r'[A-Z]+_\d+',                  # 如 HT_2024001
        ]
        
        for pattern in number_patterns:
            match = re.search(pattern, filename)
            if match:
                contract_number = match.group()
                break
        
        # 提取客户名称（从文件名）
        client_keywords = ['技术', '服务', '开发', '软件', '信息', '科技', '有限', '公司']
        client_name = ""
        for part in parts:
            if any(keyword in part for keyword in client_keywords) and len(part) > 2:
                client_name = part
                break
        
        # 如果没找到客户名，使用文件名的一部分
        if not client_name and len(parts) > 0:
            client_name = parts[0]
        
        return {
            'file_name': file_path.name,
            'contract_id': f"HT{datetime.now().strftime('%Y%m%d')}{len(self.contracts_data)+1:03d}",
            'contract_number': contract_number or f"HT{datetime.now().strftime('%Y%m%d')}{len(self.contracts_data)+1:03d}",
            'contract_name': filename.replace('_', ' '),
            'client_name': client_name,
            'file_path': str(file_path.relative_to(self.contracts_dir.parent)),
            'analysis_date': datetime.now().strftime('%Y-%m-%d')
        }
    
    def create_mapping_template(self):
        """创建人员-合同-角色映射配置模板"""
        if not self.contracts_data:
            print("❌ 没有合同数据可供映射")
            return None
            
        # 创建映射模板
        mapping_data = []
        
        for contract in self.contracts_data:
            # 为每个合同创建几个典型角色
            typical_roles = [
                {'role_name': '项目经理', 'personnel_count': 1, 'description': '负责项目整体管理和协调'},
                {'role_name': '高级开发工程师', 'personnel_count': 2, 'description': '负责核心代码开发'},
                {'role_name': '测试工程师', 'personnel_count': 1, 'description': '负责软件测试和质量保证'},
                {'role_name': 'UI/UX设计师', 'personnel_count': 1, 'description': '负责界面设计和用户体验'}
            ]
            
            for role in typical_roles:
                mapping_data.append({
                    'contract_id': contract['contract_id'],
                    'contract_name': contract['contract_name'],
                    'client_name': contract['client_name'],
                    'role_name': role['role_name'],
                    'personnel_count': role['personnel_count'],
                    'role_description': role['description'],
                    'required_skills': '',  # 需要用户填写
                    'experience_years': '',  # 需要用户填写
                    'salary_range': '',  # 需要用户填写
                    'mapping_status': '待配置'  # 待用户确认
                })
        
        # 创建DataFrame
        df = pd.DataFrame(mapping_data)
        
        # 保存到Excel文件
        output_dir = Path("./data")
        output_dir.mkdir(exist_ok=True)
        
        mapping_file = output_dir / "contract_role_mapping.xlsx"
        df.to_excel(mapping_file, index=False)
        
        print(f"✅ 映射模板已创建: {mapping_file}")
        print(f"📋 包含 {len(df)} 条映射记录")
        
        return mapping_file
    
    def generate_detailed_config(self, mapping_file):
        """根据映射配置生成详细的Excel配置文件"""
        if not mapping_file.exists():
            print("❌ 映射配置文件不存在")
            return None
            
        # 读取映射配置
        mapping_df = pd.read_excel(mapping_file)
        
        # 过滤已确认的映射
        confirmed_mapping = mapping_df[mapping_df['mapping_status'] == '已确认']
        
        if len(confirmed_mapping) == 0:
            print("⚠️ 没有确认的映射配置")
            return None
            
        # 生成详细的配置文件
        config_data = {
            'contracts': [],
            'roles': [],
            'persons': []
        }
        
        # 生成合同数据
        contract_ids = confirmed_mapping['contract_id'].unique()
        for contract_id in contract_ids:
            contract_mapping = confirmed_mapping[confirmed_mapping['contract_id'] == contract_id].iloc[0]
            
            contract_record = {
                'id': contract_id,
                'name': contract_mapping['contract_name'],
                'contract_number': contract_mapping['contract_id'],  # 使用ID作为合同编号
                'client': contract_mapping['client_name'],
                'client_address': '待填写',
                'client_contact': '待填写',
                'client_phone': '待填写',
                'project_name': contract_mapping['contract_name'].replace('合同', ''),
                'project_description': '待填写',
                'start_date': datetime.now().strftime('%Y-%m-%d'),
                'end_date': datetime.now().replace(year=datetime.now().year + 1).strftime('%Y-%m-%d'),
                'contract_amount': 0,
                'payment_terms': '待协商',
                'service_scope': '待确定',
                'deliverables': '待确定',
                'quality_requirements': '符合行业标准',
                'acceptance_criteria': '功能完整、性能达标'
            }
            config_data['contracts'].append(contract_record)
        
        # 生成角色数据
        for _, row in confirmed_mapping.iterrows():
            role_record = {
                'id': f"ROLE_{row['contract_id']}_{row['role_name'].replace('/', '_')}",
                'name': row['role_name'],
                'contract_id': row['contract_id'],
                'description': row['role_description'],
                'responsibilities': '待详细说明',
                'required_skills': row['required_skills'],
                'experience_years': row['experience_years'],
                'education_requirement': '本科及以上',
                'person_count': row['personnel_count'],
                'salary_range': row['salary_range'],
                'work_location': '待确定'
            }
            config_data['roles'].append(role_record)
        
        # 生成人员数据模板（每个角色生成相应数量的人员模板）
        person_id_counter = 1
        for _, role_row in confirmed_mapping.iterrows():
            role_id = f"ROLE_{role_row['contract_id']}_{role_row['role_name'].replace('/', '_')}"
            personnel_count = int(role_row['personnel_count'])
            
            for i in range(personnel_count):
                person_record = {
                    'id': f"P{person_id_counter:03d}",
                    'name': f"待填写_{role_row['role_name']}_{i+1}",
                    'role_id': role_id,
                    'id_card': '',
                    'gender': '',
                    'birth_date': '',
                    'email': '',
                    'phone': '',
                    'emergency_contact': '',
                    'emergency_phone': '',
                    'education': '',
                    'school': '',
                    'major': '',
                    'graduation_year': '',
                    'work_experience': '',
                    'current_company': '',
                    'current_position': '',
                    'skills': role_row['required_skills'],
                    'certifications': '',
                    'languages': '',
                    'expected_salary': ''
                }
                config_data['persons'].append(person_record)
                person_id_counter += 1
        
        # 保存到Excel文件
        output_file = Path("./data/detailed_resume_config.xlsx")
        
        with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
            # 配置表
            config_df = pd.DataFrame([{
                'contract_id': contract_ids[0] if len(contract_ids) > 0 else '',
                'template_path': './templates/resume_template.docx',
                'output_dir': './output',
                'output_format': 'both',
                'company_name': '待填写公司名称',
                'company_address': '待填写公司地址',
                'company_phone': '待填写公司电话',
                'logo_path': './assets/logo.png'
            }])
            config_df.to_excel(writer, sheet_name='config', index=False)
            
            # 合同表
            pd.DataFrame(config_data['contracts']).to_excel(writer, sheet_name='contracts', index=False)
            
            # 角色表
            pd.DataFrame(config_data['roles']).to_excel(writer, sheet_name='roles', index=False)
            
            # 人员表
            pd.DataFrame(config_data['persons']).to_excel(writer, sheet_name='persons', index=False)
            
            # 添加说明
            instructions = pd.DataFrame({
                '说明': [
                    '请按以下步骤操作:',
                    '1. 在config工作表中填写公司基本信息',
                    '2. 在contracts工作表中完善合同详细信息',
                    '3. 在roles工作表中细化角色要求',
                    '4. 在persons工作表中填写具体人员信息',
                    '5. 保存文件后使用简历生成工具'
                ]
            })
            instructions.to_excel(writer, sheet_name='使用说明', index=False)
        
        print(f"✅ 详细配置文件已生成: {output_file}")
        print(f"📊 包含 {len(config_data['contracts'])} 个合同")
        print(f"📊 包含 {len(config_data['roles'])} 个角色")
        print(f"📊 包含 {len(config_data['persons'])} 个人员模板")
        
        return output_file

def main():
    """主函数"""
    print("=== 合同分析和配置工具 ===\n")
    
    # 分析合同
    analyzer = ContractAnalyzer("../contracts")
    if not analyzer.analyze_contracts():
        return
    
    # 创建映射模板
    print("\n1. 创建人员-合同-角色映射模板...")
    mapping_file = analyzer.create_mapping_template()
    
    if mapping_file:
        print(f"\n💡 请按以下步骤操作:")
        print(f"1. 打开映射文件: {mapping_file}")
        print(f"2. 在 'required_skills', 'experience_years', 'salary_range' 列中填写具体信息")
        print(f"3. 将 'mapping_status' 列中的 '待配置' 改为 '已确认'")
        print(f"4. 保存文件后重新运行此工具的第二步")
        
        # 询问是否继续生成详细配置
        user_input = input("\n是否现在就生成详细配置文件? (y/n): ").strip().lower()
        if user_input == 'y':
            print("\n2. 生成详细配置文件...")
            analyzer.generate_detailed_config(mapping_file)

if __name__ == "__main__":
    main()