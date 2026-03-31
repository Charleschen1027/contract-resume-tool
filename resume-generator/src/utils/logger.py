"""
日志配置工具
统一的日志配置和管理
"""

import logging
import logging.handlers
import os
from datetime import datetime


def setup_logger(log_level=logging.INFO, log_file=None):
    """
    设置日志配置
    
    Args:
        log_level: 日志级别
        log_file: 日志文件路径，如果为None则只输出到控制台
    """
    # 创建logger
    logger = logging.getLogger()
    logger.setLevel(log_level)
    
    # 避免重复添加handler
    if logger.handlers:
        return
    
    # 创建格式器
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # 控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # 文件处理器（如果指定了日志文件）
    if log_file:
        # 确保日志目录存在
        log_dir = os.path.dirname(log_file)
        if log_dir:
            os.makedirs(log_dir, exist_ok=True)
        
        # 使用RotatingFileHandler避免日志文件过大
        file_handler = logging.handlers.RotatingFileHandler(
            log_file,
            maxBytes=10*1024*1024,  # 10MB
            backupCount=5,
            encoding='utf-8'
        )
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    logger.info("日志系统初始化完成")


def get_logger(name: str) -> logging.Logger:
    """
    获取指定名称的logger
    
    Args:
        name: logger名称
        
    Returns:
        logging.Logger: 配置好的logger实例
    """
    return logging.getLogger(name)


# 预定义的日志级别快捷方法
def log_debug(message: str, logger_name: str = None):
    """记录debug级别日志"""
    logger = get_logger(logger_name or __name__)
    logger.debug(message)


def log_info(message: str, logger_name: str = None):
    """记录info级别日志"""
    logger = get_logger(logger_name or __name__)
    logger.info(message)


def log_warning(message: str, logger_name: str = None):
    """记录warning级别日志"""
    logger = get_logger(logger_name or __name__)
    logger.warning(message)


def log_error(message: str, logger_name: str = None):
    """记录error级别日志"""
    logger = get_logger(logger_name or __name__)
    logger.error(message)


def log_critical(message: str, logger_name: str = None):
    """记录critical级别日志"""
    logger = get_logger(logger_name or __name__)
    logger.critical(message)