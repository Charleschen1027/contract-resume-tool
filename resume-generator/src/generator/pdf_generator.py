"""
PDF简历生成器
基于ReportLab库生成PDF格式简历
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from .base import DocumentGenerator
from ..data.models import Person
import logging
import os

logger = logging.getLogger(__name__)


class PDFGenerator(DocumentGenerator):
    """PDF简历生成器"""
    
    def _load_template(self):
        """加载PDF模板（这里简化处理）"""
        # 实际项目中可以从PDF模板文件加载样式
        self.page_size = letter
        self.margin = 0.75 * inch
        
        # 注册中文字体（如果需要）
        try:
            # 这里需要根据实际系统字体路径调整
            font_path = "/System/Library/Fonts/PingFang.ttc"  # macOS示例
            if os.path.exists(font_path):
                pdfmetrics.registerFont(TTFont('PingFang', font_path))
                self.font_name = 'PingFang'
            else:
                self.font_name = 'Helvetica'  # 默认字体
        except Exception as e:
            logger.warning(f"字体注册失败，使用默认字体: {e}")
            self.font_name = 'Helvetica'
    
    def generate(self, person: Person, output_path: str, **kwargs) -> bool:
        """
        生成PDF简历
        
        Args:
            person: 人员信息
            output_path: 输出文件路径
            **kwargs: 额外参数
            
        Returns:
            bool: 生成是否成功
        """
        try:
            # 确保输出目录存在
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            # 创建文档
            doc = SimpleDocTemplate(
                output_path,
                pagesize=self.page_size,
                leftMargin=self.margin,
                rightMargin=self.margin,
                topMargin=self.margin,
                bottomMargin=self.margin
            )
            
            # 准备内容
            story = self._create_content(person)
            
            # 构建文档
            doc.build(story)
            
            logger.info(f"成功生成PDF简历: {output_path}")
            return True
            
        except Exception as e:
            logger.error(f"生成PDF简历失败: {e}")
            return False
    
    def _create_content(self, person: Person) -> list:
        """创建PDF内容"""
        story = []
        styles = getSampleStyleSheet()
        
        # 标题样式
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            alignment=1,  # 居中
            fontName=self.font_name
        )
        
        # 正文样式
        normal_style = ParagraphStyle(
            'CustomNormal',
            parent=styles['Normal'],
            fontSize=12,
            spaceAfter=12,
            fontName=self.font_name
        )
        
        # 标题
        story.append(Paragraph(person.name, title_style))
        story.append(Spacer(1, 20))
        
        # 联系信息表格
        contact_data = [
            ['邮箱:', person.email],
            ['电话:', person.phone],
            ['学历:', person.education]
        ]
        
        contact_table = Table(contact_data, colWidths=[inch*1.5, inch*4])
        contact_table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), self.font_name),
            ('FONTSIZE', (0, 0), (-1, -1), 12),
            ('ALIGN', (0, 0), (0, -1), 'RIGHT'),
            ('ALIGN', (1, 0), (1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
        ]))
        
        story.append(contact_table)
        story.append(Spacer(1, 20))
        
        # 工作经历
        story.append(Paragraph('工作经历', styles['Heading2']))
        story.append(Paragraph(person.work_experience or '暂无工作经历信息', normal_style))
        story.append(Spacer(1, 15))
        
        # 技能
        if person.skills:
            story.append(Paragraph('专业技能', styles['Heading2']))
            skills_text = ', '.join(person.skills)
            story.append(Paragraph(skills_text, normal_style))
            story.append(Spacer(1, 15))
        
        # 证书
        if person.certifications:
            story.append(Paragraph('相关证书', styles['Heading2']))
            certs_text = ', '.join(person.certifications)
            story.append(Paragraph(certs_text, normal_style))
        
        return story