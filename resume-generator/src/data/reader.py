"""
Excel数据读取和解析模块
负责从Excel配置文件中读取合同、角色、人员信息
"""

import pandas as pd
from typing import List, Dict
from datetime import datetime
from .models import Contract, Role, Person, ResumeConfig
import logging

logger = logging.getLogger(__name__)


class ExcelDataReader:
    """Excel数据读取器"""
    
    def __init__(self, excel_path: str):
        self.excel_path = excel_path
        self.data_frames = {}
        self._load_excel()
    
    def _load_excel(self):
        """加载Excel文件的所有工作表"""
        try:
            excel_file = pd.ExcelFile(self.excel_path)
            for sheet_name in excel_file.sheet_names:
                self.data_frames[sheet_name] = pd.read_excel(self.excel_path, sheet_name=sheet_name)
            logger.info(f"成功加载Excel文件，包含工作表: {list(self.data_frames.keys())}")
        except Exception as e:
            logger.error(f"加载Excel文件失败: {e}")
            raise
    
    def read_contracts(self) -> List[Contract]:
        """读取合同信息"""
        if 'contracts' not in self.data_frames:
            raise ValueError("Excel文件中缺少'contracts'工作表")
        
        contracts_df = self.data_frames['contracts']
        contracts = []
        
        for _, row in contracts_df.iterrows():
            contract = Contract(
                id=str(row.get('id', '')),
                name=str(row.get('name', '')),
                client=str(row.get('client', '')),
                start_date=pd.to_datetime(row.get('start_date')),
                end_date=pd.to_datetime(row.get('end_date')),
                role_ids=[rid.strip() for rid in str(row.get('role_ids', '')).split(',') if rid.strip()]
            )
            contracts.append(contract)
        
        logger.info(f"读取到 {len(contracts)} 个合同")
        return contracts
    
    def read_roles(self) -> List[Role]:
        """读取角色信息"""
        if 'roles' not in self.data_frames:
            raise ValueError("Excel文件中缺少'roles'工作表")
        
        roles_df = self.data_frames['roles']
        roles = []
        
        for _, row in roles_df.iterrows():
            role = Role(
                id=str(row.get('id', '')),
                name=str(row.get('name', '')),
                description=str(row.get('description', '')),
                required_skills=[skill.strip() for skill in str(row.get('required_skills', '')).split(',') if skill.strip()],
                person_ids=[pid.strip() for pid in str(row.get('person_ids', '')).split(',') if pid.strip()]
            )
            roles.append(role)
        
        logger.info(f"读取到 {len(roles)} 个角色")
        return roles
    
    def read_persons(self) -> List[Person]:
        """读取人员信息"""
        if 'persons' not in self.data_frames:
            raise ValueError("Excel文件中缺少'persons'工作表")
        
        persons_df = self.data_frames['persons']
        persons = []
        
        for _, row in persons_df.iterrows():
            person = Person(
                id=str(row.get('id', '')),
                name=str(row.get('name', '')),
                email=str(row.get('email', '')),
                phone=str(row.get('phone', '')),
                education=str(row.get('education', '')),
                work_experience=str(row.get('work_experience', '')),
                skills=row.get('skills', ''),
                certifications=row.get('certifications', '')
            )
            persons.append(person)
        
        logger.info(f"读取到 {len(persons)} 个人员")
        return persons
    
    def read_config(self) -> ResumeConfig:
        """读取完整的简历生成配置"""
        if 'config' not in self.data_frames:
            raise ValueError("Excel文件中缺少'config'工作表")
        
        config_df = self.data_frames['config']
        if len(config_df) == 0:
            raise ValueError("'config'工作表为空")
        
        # 读取第一条配置记录
        config_row = config_df.iloc[0]
        
        # 读取各个数据表
        contracts = self.read_contracts()
        roles = self.read_roles()
        persons = self.read_persons()
        
        # 获取配置信息
        contract_id = str(config_row.get('contract_id', ''))
        template_path = str(config_row.get('template_path', ''))
        output_dir = str(config_row.get('output_dir', './output'))
        output_format = str(config_row.get('output_format', 'pdf')).lower()
        
        # 找到对应的合同
        contract = next((c for c in contracts if c.id == contract_id), None)
        if not contract:
            raise ValueError(f"找不到ID为'{contract_id}'的合同")
        
        config = ResumeConfig(
            contract=contract,
            roles=roles,
            persons=persons,
            template_path=template_path,
            output_dir=output_dir,
            output_format=output_format
        )
        
        logger.info(f"成功读取简历生成配置: 合同={contract.name}, 模板={template_path}")
        return config