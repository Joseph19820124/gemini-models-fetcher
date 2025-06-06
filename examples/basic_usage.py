#!/usr/bin/env python3
"""
基本使用示例
演示如何使用GeminiModelsFetcher获取模型信息
"""

import os
import sys

# 添加父目录到路径，以便导入主模块
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gemini_models_fetcher import GeminiModelsFetcher

def example_basic_usage():
    """基本使用示例"""
    print("=== 基本使用示例 ===")
    
    # 从环境变量获取API密钥
    api_key = os.getenv('GOOGLE_AI_API_KEY')
    
    if not api_key:
        print("请设置GOOGLE_AI_API_KEY环境变量")
        print("获取API密钥: https://makersuite.google.com/app/apikey")
        return
    
    # 创建获取器实例
    fetcher = GeminiModelsFetcher(api_key)
    
    # 获取所有模型
    print("\n1. 获取所有模型...")
    models = fetcher.get_models_via_new_sdk()
    
    if not models:
        models = fetcher.get_models_via_sdk()
    
    if not models:
        models = fetcher.get_models_via_rest_api()
    
    if models:
        print(f"找到 {len(models)} 个模型")
        
        # 过滤最新模型
        print("\n2. 过滤最新模型...")
        latest_models = fetcher.filter_latest_models(models)
        print(f"其中 {len(latest_models)} 个是最新的Gemini模型")
        
        # 显示模型信息
        print("\n3. 显示模型详细信息:")
        fetcher.print_models_info(latest_models[:3])  # 只显示前3个
        
    else:
        print("获取模型失败")

def example_filter_specific_models():
    """过滤特定模型的示例"""
    print("\n\n=== 过滤特定模型示例 ===")
    
    api_key = os.getenv('GOOGLE_AI_API_KEY')
    if not api_key:
        return
        
    fetcher = GeminiModelsFetcher(api_key)
    models = fetcher.get_models_via_new_sdk()
    
    if models:
        # 过滤出Gemini 2.5模型
        gemini_25_models = []
        for model in models:
            if 'gemini-2.5' in model.get('name', '').lower():
                gemini_25_models.append(model)
        
        print(f"找到 {len(gemini_25_models)} 个Gemini 2.5模型:")
        for model in gemini_25_models:
            print(f"- {model.get('name')}")
        
        # 过滤出Flash模型
        flash_models = []
        for model in models:
            if 'flash' in model.get('name', '').lower():
                flash_models.append(model)
        
        print(f"\n找到 {len(flash_models)} 个Flash模型:")
        for model in flash_models:
            print(f"- {model.get('name')}")

def example_model_comparison():
    """模型比较示例"""
    print("\n\n=== 模型比较示例 ===")
    
    api_key = os.getenv('GOOGLE_AI_API_KEY')
    if not api_key:
        return
        
    fetcher = GeminiModelsFetcher(api_key)
    models = fetcher.get_models_via_new_sdk()
    
    if models:
        # 比较不同模型的token限制
        print("模型token限制比较:")
        print(f"{'模型名称':<30} {'输入限制':<15} {'输出限制':<15}")
        print("-" * 60)
        
        for model in models[:10]:  # 只显示前10个
            name = model.get('name', 'N/A')[-30:]  # 截取后30个字符
            input_limit = model.get('input_token_limit', 'N/A')
            output_limit = model.get('output_token_limit', 'N/A')
            
            print(f"{name:<30} {str(input_limit):<15} {str(output_limit):<15}")

if __name__ == "__main__":
    # 运行所有示例
    example_basic_usage()
    example_filter_specific_models()
    example_model_comparison()