"""
简历生成工具 - 简化版快速开始
"""

import os
import shutil
from pathlib import Path

def setup_project():
    """设置项目环境"""
    print("=== 简历生成工具快速开始 ===\n")
    
    # 创建必要目录
    dirs = ["./data", "./output", "./logs"]
    for dir_path in dirs:
        Path(dir_path).mkdir(exist_ok=True)
        print(f"✓ 创建目录: {dir_path}")
    
    # 复制示例配置
    sample_config = Path("./templates/sample_configs/sample_filled_config.xlsx")
    target_config = Path("./data/sample_config.xlsx")
    
    if sample_config.exists():
        shutil.copy2(sample_config, target_config)
        print(f"✓ 复制示例配置: {target_config}")
    else:
        print("❌ 示例配置文件不存在")
        return False
    
    print("\n=== 环境设置完成 ===")
    print("接下来您可以:")
    print("1. 修改 data/sample_config.xlsx 中的数据")
    print("2. 运行: python3 src/main.py --config ./data/sample_config.xlsx")
    print("3. 或运行演示: python3 demo.py")
    
    return True

def show_commands():
    """显示常用命令"""
    print("\n=== 常用命令 ===")
    print("# 运行示例演示")
    print("python3 demo.py")
    print()
    print("# 使用示例配置生成简历")
    print("python3 src/main.py --config ./data/sample_config.xlsx")
    print()
    print("# 使用详细模式")
    print("python3 src/main.py --config ./data/sample_config.xlsx --verbose")
    print()
    print("# 指定输出目录")
    print("python3 src/main.py --config ./data/sample_config.xlsx --output ./my_resumes")

if __name__ == "__main__":
    if setup_project():
        show_commands()
    else:
        print("❌ 项目设置失败")