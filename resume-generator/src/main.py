"""
简历生成工具主程序
命令行界面入口
"""

import click
import os
import sys
from pathlib import Path

# 添加src目录到Python路径
src_path = Path(__file__).parent.parent
sys.path.insert(0, str(src_path))

# 导入模块
import logging
from core.generator import ResumeGenerator
from utils.logger import setup_logger, get_logger

logger = get_logger(__name__)


@click.command()
@click.option('--config', '-c', required=True, help='Excel配置文件路径')
@click.option('--output', '-o', help='输出目录（可选，优先使用配置文件中的设置）')
@click.option('--format', '-f', type=click.Choice(['pdf', 'word', 'both']), 
              help='输出格式（可选，优先使用配置文件中的设置）')
@click.option('--verbose', '-v', is_flag=True, help='详细输出模式')
@click.version_option(version='1.0.0')
def main(config, output, format, verbose):
    """
    简历生成工具
    
    基于Excel配置文件批量生成个性化简历
    """
    try:
        # 设置日志
        log_level = logging.DEBUG if verbose else logging.INFO
        log_file = 'logs/resume_generator.log' if verbose else None
        setup_logger(log_level, log_file)
        
        logger.info("开始简历生成工具")
        logger.info(f"配置文件: {config}")
        
        # 验证配置文件是否存在
        if not os.path.exists(config):
            logger.error(f"配置文件不存在: {config}")
            click.echo(f"错误: 配置文件 '{config}' 不存在", err=True)
            sys.exit(1)
        
        # 创建生成器并执行
        generator = ResumeGenerator(config)
        
        # 如果指定了命令行参数，覆盖配置文件设置
        if output:
            generator.config.output_dir = output
        if format:
            generator.config.output_format = format
        
        # 执行生成
        results = generator.generate_all()
        
        # 根据结果决定退出码
        if results['failed'] > 0:
            sys.exit(1)
        else:
            sys.exit(0)
            
    except Exception as e:
        logger.error(f"程序执行出错: {e}", exc_info=True)
        click.echo(f"错误: {e}", err=True)
        sys.exit(1)


if __name__ == '__main__':
    # 添加src目录到Python路径
    src_path = Path(__file__).parent.parent
    sys.path.insert(0, str(src_path))
    
    # 导入logging模块（在main函数外部导入会导致循环导入）
    import logging
    main()