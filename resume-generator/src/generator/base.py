"""
文档生成器基类
定义文档生成的通用接口
"""

from abc import ABC, abstractmethod
from typing import Dict, Any
import sys
from pathlib import Path

# 添加src目录到路径
src_path = Path(__file__).parent.parent
sys.path.insert(0, str(src_path))

import logging

# 延迟导入Person，在使用时导入
Person = None

logger = logging.getLogger(__name__)


class DocumentGenerator(ABC):
    """文档生成器抽象基类"""
    
    def __init__(self, template_path: str):
        self.template_path = template_path
        self._load_template()
    
    @abstractmethod
    def _load_template(self):
        """加载模板文件"""
        pass
    
    @abstractmethod
    def generate(self, person: Person, output_path: str, **kwargs) -> bool:
        """
        生成文档
        
        Args:
            person: 人员信息
            output_path: 输出文件路径
            **kwargs: 额外参数
            
        Returns:
            bool: 生成是否成功
        """
        pass
    
    def _prepare_data(self, person: Person) -> Dict[str, Any]:
        """准备模板数据"""
        return {
            'name': person.name,
            'email': person.email,
            'phone': person.phone,
            'education': person.education,
            'work_experience': person.work_experience,
            'skills': ', '.join(person.skills) if person.skills else '',
            'certifications': ', '.join(person.certifications) if person.certifications else '',
            'generated_date': self._get_current_date()
        }
    
    def _get_current_date(self) -> str:
        """获取当前日期字符串"""
        from datetime import datetime
        return datetime.now().strftime('%Y-%m-%d')