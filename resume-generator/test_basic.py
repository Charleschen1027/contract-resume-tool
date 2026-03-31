"""
简单测试脚本
验证各模块的基本功能
"""

import sys
import os
from pathlib import Path

# 添加src目录到Python路径
src_path = Path(__file__).parent / 'src'
sys.path.insert(0, str(src_path))

def test_imports():
    """测试模块导入"""
    print("测试模块导入...")
    
    try:
        # 直接导入，避免相对导入问题
        import data.models as models
        print("✓ 数据模型导入成功")
        
        import data.reader as reader
        print("✓ Excel读取器导入成功")
        
        import generator.base as base
        print("✓ 文档生成器基类导入成功")
        
        import generator.pdf_generator as pdf_gen
        print("✓ PDF生成器导入成功")
        
        import generator.word_generator as word_gen
        print("✓ Word生成器导入成功")
        
        import core.generator as core_gen
        print("✓ 核心生成器导入成功")
        
        import utils.logger as logger
        print("✓ 日志工具导入成功")
        
        return True
    except ImportError as e:
        print(f"✗ 导入失败: {e}")
        return False

def test_models():
    """测试数据模型"""
    print("\n测试数据模型...")
    
    try:
        from data.models import Person, Role, Contract
        from datetime import datetime
        
        # 测试Person模型
        person = Person(
            id="P001",
            name="张三",
            email="zhangsan@example.com",
            phone="13800138000",
            education="本科",
            work_experience="3年软件开发经验",
            skills="Python,Java,JavaScript",
            certifications="软件工程师认证"
        )
        print("✓ Person模型创建成功")
        
        # 测试Role模型
        role = Role(
            id="ROLE001",
            name="软件工程师",
            description="负责软件开发工作",
            required_skills=["Python", "Java"],
            person_ids=["P001", "P002"]
        )
        print("✓ Role模型创建成功")
        
        # 测试Contract模型
        contract = Contract(
            id="HT2024001",
            name="软件开发项目",
            client="XX科技有限公司",
            start_date=datetime(2024, 1, 1),
            end_date=datetime(2024, 12, 31),
            role_ids=["ROLE001", "ROLE002"]
        )
        print("✓ Contract模型创建成功")
        
        return True
    except Exception as e:
        print(f"✗ 数据模型测试失败: {e}")
        return False

def test_directory_structure():
    """测试目录结构"""
    print("\n测试目录结构...")
    
    required_dirs = [
        'src',
        'src/data',
        'src/generator',
        'src/core',
        'src/utils',
        'templates',
        'data',
        'output',
        'docs'
    ]
    
    base_path = Path(__file__).parent
    missing_dirs = []
    
    for dir_name in required_dirs:
        dir_path = base_path / dir_name
        if not dir_path.exists():
            missing_dirs.append(dir_name)
        else:
            print(f"✓ {dir_name} 目录存在")
    
    if missing_dirs:
        print(f"✗ 缺少目录: {missing_dirs}")
        return False
    
    return True

def main():
    """主测试函数"""
    print("=== 简历生成工具测试 ===\n")
    
    tests = [
        ("目录结构测试", test_directory_structure),
        ("模块导入测试", test_imports),
        ("数据模型测试", test_models)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n{test_name}:")
        if test_func():
            passed += 1
            print(f"✓ {test_name} 通过")
        else:
            print(f"✗ {test_name} 失败")
    
    print(f"\n=== 测试结果 ===")
    print(f"通过: {passed}/{total}")
    
    if passed == total:
        print("🎉 所有测试通过！")
        return 0
    else:
        print("❌ 部分测试失败")
        return 1

if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)