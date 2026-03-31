"""
简历生成核心协调器
负责协调整个简历生成流程
"""

from typing import List
from tqdm import tqdm
import os
import logging
from ..data.models import ResumeConfig, Person
from ..data.reader import ExcelDataReader
from .pdf_generator import PDFGenerator
from .word_generator import WordGenerator
from ..utils.logger import setup_logger

logger = logging.getLogger(__name__)


class ResumeGenerator:
    """简历生成器主类"""
    
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.config = None
        self.pdf_generator = None
        self.word_generator = None
        self._setup()
    
    def _setup(self):
        """初始化生成器"""
        # 设置日志
        setup_logger()
        
        # 读取配置
        reader = ExcelDataReader(self.config_path)
        self.config = reader.read_config()
        
        # 初始化生成器
        if self.config.output_format in ['pdf', 'both']:
            self.pdf_generator = PDFGenerator(self.config.template_path)
        
        if self.config.output_format in ['word', 'both']:
            self.word_generator = WordGenerator(self.config.template_path)
        
        # 确保输出目录存在
        os.makedirs(self.config.output_dir, exist_ok=True)
        
        logger.info("简历生成器初始化完成")
    
    def generate_all(self) -> dict:
        """
        批量生成所有简历
        
        Returns:
            dict: 生成结果统计
        """
        results = {
            'total': 0,
            'success': 0,
            'failed': 0,
            'details': []
        }
        
        # 获取需要生成的简历列表
        resume_tasks = self._prepare_resume_tasks()
        results['total'] = len(resume_tasks)
        
        logger.info(f"开始生成 {len(resume_tasks)} 份简历")
        
        # 使用进度条显示生成进度
        for task in tqdm(resume_tasks, desc="生成简历", unit="份"):
            success = self._generate_single_resume(task)
            if success:
                results['success'] += 1
            else:
                results['failed'] += 1
            
            results['details'].append({
                'person_name': task['person'].name,
                'role_name': task['role'].name,
                'success': success,
                'output_files': task.get('output_files', [])
            })
        
        # 输出统计信息
        self._print_summary(results)
        return results
    
    def _prepare_resume_tasks(self) -> List[dict]:
        """准备简历生成任务列表"""
        tasks = []
        
        # 获取合同涉及的所有角色
        roles = self.config.get_roles_for_contract()
        
        for role in roles:
            # 获取该角色的所有人员
            persons = self.config.get_persons_for_role(role.id)
            
            for person in persons:
                # 生成文件名
                filename_base = f"{person.name}_{role.name}"
                
                task = {
                    'person': person,
                    'role': role,
                    'filename_base': filename_base,
                    'output_files': []
                }
                
                tasks.append(task)
        
        logger.info(f"准备了 {len(tasks)} 个简历生成任务")
        return tasks
    
    def _generate_single_resume(self, task: dict) -> bool:
        """生成单份简历"""
        person = task['person']
        filename_base = task['filename_base']
        success = True
        
        try:
            # 生成PDF
            if self.pdf_generator:
                pdf_path = os.path.join(self.config.output_dir, f"{filename_base}.pdf")
                if self.pdf_generator.generate(person, pdf_path):
                    task['output_files'].append(pdf_path)
                else:
                    success = False
                    logger.error(f"PDF生成失败: {person.name}")
            
            # 生成Word
            if self.word_generator:
                word_path = os.path.join(self.config.output_dir, f"{filename_base}.docx")
                if self.word_generator.generate(person, word_path):
                    task['output_files'].append(word_path)
                else:
                    success = False
                    logger.error(f"Word生成失败: {person.name}")
            
            if success:
                logger.info(f"成功生成简历: {person.name} ({filename_base})")
            
        except Exception as e:
            logger.error(f"生成简历时发生错误 {person.name}: {e}")
            success = False
        
        return success
    
    def _print_summary(self, results: dict):
        """打印生成结果摘要"""
        print("\n" + "="*50)
        print("简历生成完成!")
        print("="*50)
        print(f"总计: {results['total']} 份")
        print(f"成功: {results['success']} 份")
        print(f"失败: {results['failed']} 份")
        print("="*50)
        
        if results['failed'] > 0:
            print("\n失败的简历:")
            for detail in results['details']:
                if not detail['success']:
                    print(f"  - {detail['person_name']} ({detail['role_name']})")
        
        print(f"\n生成的文件保存在: {os.path.abspath(self.config.output_dir)}")