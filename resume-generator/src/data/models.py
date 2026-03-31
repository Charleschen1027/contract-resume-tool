"""
数据模型定义
定义合同、角色、人员等核心数据结构
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
from datetime import datetime


@dataclass
class Person:
    """人员信息"""
    id: str
    name: str
    email: str
    phone: str
    education: str
    work_experience: str
    skills: List[str]
    certifications: List[str]
    
    def __post_init__(self):
        # 确保skills和certifications是列表
        if isinstance(self.skills, str):
            self.skills = [s.strip() for s in self.skills.split(',')] if self.skills else []
        if isinstance(self.certifications, str):
            self.certifications = [c.strip() for c in self.certifications.split(',')] if self.certifications else []


@dataclass
class Role:
    """角色信息"""
    id: str
    name: str
    description: str
    required_skills: List[str]
    person_ids: List[str]  # 关联的人员ID列表


@dataclass
class Contract:
    """合同信息"""
    id: str
    name: str
    client: str
    start_date: datetime
    end_date: datetime
    role_ids: List[str]  # 关联的角色ID列表


@dataclass
class ResumeConfig:
    """简历生成配置"""
    contract: Contract
    roles: List[Role]
    persons: List[Person]
    template_path: str
    output_dir: str
    output_format: str  # 'pdf', 'word', 'both'
    
    def get_persons_for_role(self, role_id: str) -> List[Person]:
        """获取指定角色的所有人员"""
        role = next((r for r in self.roles if r.id == role_id), None)
        if not role:
            return []
        
        return [p for p in self.persons if p.id in role.person_ids]
    
    def get_roles_for_contract(self) -> List[Role]:
        """获取合同涉及的所有角色"""
        return [r for r in self.roles if r.id in self.contract.role_ids]