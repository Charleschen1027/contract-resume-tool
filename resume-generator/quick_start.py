#!/bin/bash
"""
简历生成工具快速开始脚本
帮助用户快速配置和使用工具
"""

import os
import shutil
from pathlib import Path

def print_welcome():
    """打印欢迎信息"""
    print("=" * 60)
    print("           简历生成工具 - 快速开始向导")
    print("=" * 60)
    print()

def show_menu():
    """显示主菜单"""
    print("请选择操作:")
    print("1. 查看模板文件")
    print("2. 复制示例配置文件")
    print("3. 复制空白模板文件")
    print("4. 运行示例演示")
    print("5. 运行简历生成器")
    print("6. 查看使用说明")
    print("0. 退出")
    print()

def list_templates():
    """列出可用的模板文件"""
    template_dir = Path("./templates")
    if not template_dir.exists():
        print("❌ 模板目录不存在")
        return
    
    print("📋 可用模板文件:")
    print("-" * 40)
    
    # 综合模板
    combined_template = template_dir / "config_templates" / "resume_config_template.xlsx"
    if combined_template.exists():
        print(f"📄 综合配置模板: {combined_template}")
    
    # 示例配置
    sample_config = template_dir / "sample_configs" / "sample_filled_config.xlsx"
    if sample_config.exists():
        print(f"📊 示例配置文件: {sample_config}")
    
    # 单独模板
    config_templates = template_dir / "config_templates"
    if config_templates.exists():
        for template in config_templates.glob("*.xlsx"):
            if "resume_config_template" not in template.name:
                print(f"📑 {template.stem}: {template}")
    
    print()

def copy_sample_config():
    """复制示例配置文件"""
    source = Path("./templates/sample_configs/sample_filled_config.xlsx")
    dest_dir = Path("./data")
    dest_file = dest_dir / "my_config.xlsx"
    
    if not source.exists():
        print("❌ 示例配置文件不存在")
        return
    
    # 创建数据目录
    dest_dir.mkdir(exist_ok=True)
    
    # 复制文件
    try:
        shutil.copy2(source, dest_file)
        print(f"✅ 示例配置已复制到: {dest_file}")
        print("💡 您可以在Excel中打开此文件并修改为实际数据")
    except Exception as e:
        print(f"❌ 复制失败: {e}")

def copy_blank_template():
    """复制空白模板文件"""
    source = Path("./templates/config_templates/resume_config_template.xlsx")
    dest_dir = Path("./data")
    dest_file = dest_dir / "blank_config.xlsx"
    
    if not source.exists():
        print("❌ 空白模板文件不存在")
        return
    
    # 创建数据目录
    dest_dir.mkdir(exist_ok=True)
    
    # 复制文件
    try:
        shutil.copy2(source, dest_file)
        print(f"✅ 空白模板已复制到: {dest_file}")
        print("💡 您可以在Excel中打开此文件并填写所有数据")
    except Exception as e:
        print(f"❌ 复制失败: {e}")

def run_demo():
    """运行示例演示"""
    print("🚀 运行示例演示...")
    try:
        os.system("python3 demo.py")
    except Exception as e:
        print(f"❌ 演示运行失败: {e}")

def run_generator():
    """运行简历生成器"""
    # 检查配置文件
    config_files = list(Path("./data").glob("*.xlsx"))
    
    if not config_files:
        print("❌ data目录中没有找到配置文件")
        print("💡 请先复制模板文件并填写数据")
        return
    
    print("📋 可用的配置文件:")
    for i, config_file in enumerate(config_files, 1):
        print(f"{i}. {config_file.name}")
    
    try:
        choice = int(input("请选择要使用的配置文件编号: ")) - 1
        if 0 <= choice < len(config_files):
            config_path = config_files[choice]
            print(f"🚀 使用配置文件: {config_path}")
            os.system(f"python3 src/main.py --config {config_path}")
        else:
            print("❌ 无效的选择")
    except ValueError:
        print("❌ 请输入有效的数字")
    except Exception as e:
        print(f"❌ 运行失败: {e}")

def show_help():
    """显示使用说明"""
    help_file = Path("./docs/user_guide.md")
    if help_file.exists():
        print("📖 使用说明文档位置:")
        print(f"   {help_file.absolute()}")
        print("\n💡 建议在文本编辑器中打开查看详细说明")
    else:
        print("❌ 使用说明文档不存在")

def main():
    """主函数"""
    print_welcome()
    
    while True:
        show_menu()
        try:
            choice = input("请输入选项编号: ").strip()
            
            if choice == "1":
                list_templates()
            elif choice == "2":
                copy_sample_config()
            elif choice == "3":
                copy_blank_template()
            elif choice == "4":
                run_demo()
            elif choice == "5":
                run_generator()
            elif choice == "6":
                show_help()
            elif choice == "0":
                print("👋 感谢使用简历生成工具！")
                break
            else:
                print("❌ 无效选项，请重新选择")
            
            input("\n按回车键继续...")
            print("\n" + "=" * 60 + "\n")
            
        except KeyboardInterrupt:
            print("\n\n👋 程序已退出")
            break
        except Exception as e:
            print(f"❌ 发生错误: {e}")

if __name__ == "__main__":
    main()