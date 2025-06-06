#!/usr/bin/env python3
"""
获取Google Gemini最新模型列表的脚本
支持通过Gemini Developer API和Vertex AI API获取模型信息
"""

import os
import requests
from typing import List, Dict, Optional
from datetime import datetime

class GeminiModelsFetcher:
    """获取Google Gemini模型列表的类"""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        初始化模型获取器
        
        Args:
            api_key: Google AI Studio API密钥，如果未提供则从环境变量获取
        """
        self.api_key = api_key or os.getenv('GOOGLE_AI_API_KEY')
        self.base_url = "https://generativelanguage.googleapis.com/v1beta/models"
        
    def get_models_via_rest_api(self) -> List[Dict]:
        """
        通过REST API获取所有可用的Gemini模型
        
        Returns:
            包含模型信息的字典列表
        """
        if not self.api_key:
            raise ValueError("需要提供API密钥。请设置GOOGLE_AI_API_KEY环境变量或传入api_key参数")
            
        headers = {
            'Content-Type': 'application/json',
        }
        
        params = {
            'key': self.api_key
        }
        
        try:
            response = requests.get(self.base_url, headers=headers, params=params)
            response.raise_for_status()
            
            data = response.json()
            return data.get('models', [])
            
        except requests.exceptions.RequestException as e:
            print(f"API请求失败: {e}")
            return []
    
    def get_models_via_sdk(self) -> List[Dict]:
        """
        通过Python SDK获取模型列表
        需要安装: pip install google-generativeai
        
        Returns:
            包含模型信息的字典列表
        """
        try:
            import google.generativeai as genai
            
            if not self.api_key:
                raise ValueError("需要提供API密钥")
                
            genai.configure(api_key=self.api_key)
            
            models = []
            for model in genai.list_models():
                models.append({
                    'name': model.name,
                    'display_name': getattr(model, 'display_name', ''),
                    'description': getattr(model, 'description', ''),
                    'supported_generation_methods': getattr(model, 'supported_generation_methods', []),
                    'input_token_limit': getattr(model, 'input_token_limit', None),
                    'output_token_limit': getattr(model, 'output_token_limit', None),
                })
            
            return models
            
        except ImportError:
            print("请安装Google Generative AI SDK: pip install google-generativeai")
            return []
        except Exception as e:
            print(f"SDK获取模型失败: {e}")
            return []
    
    def get_models_via_new_sdk(self) -> List[Dict]:
        """
        通过新的Google GenAI SDK获取模型列表
        需要安装: pip install google-genai
        
        Returns:
            包含模型信息的字典列表
        """
        try:
            from google import genai
            
            if not self.api_key:
                raise ValueError("需要提供API密钥")
                
            client = genai.Client(api_key=self.api_key)
            
            models = []
            response = client.models.list()
            
            for model in response:
                models.append({
                    'name': model.name,
                    'display_name': getattr(model, 'display_name', ''),
                    'description': getattr(model, 'description', ''),
                    'supported_generation_methods': getattr(model, 'supported_generation_methods', []),
                    'input_token_limit': getattr(model, 'input_token_limit', None),
                    'output_token_limit': getattr(model, 'output_token_limit', None),
                })
            
            return models
            
        except ImportError:
            print("请安装新版Google GenAI SDK: pip install google-genai")
            return []
        except Exception as e:
            print(f"新SDK获取模型失败: {e}")
            return []
    
    def filter_latest_models(self, models: List[Dict]) -> List[Dict]:
        """
        过滤出最新的Gemini模型
        
        Args:
            models: 所有模型列表
            
        Returns:
            最新的Gemini模型列表
        """
        latest_models = []
        
        # 定义最新模型的关键词
        latest_keywords = [
            'gemini-2.5',      # Gemini 2.5系列
            'gemini-2.0',      # Gemini 2.0系列
            'gemini-1.5',      # Gemini 1.5系列
        ]
        
        for model in models:
            model_name = model.get('name', '').lower()
            
            # 检查是否包含最新模型关键词
            for keyword in latest_keywords:
                if keyword in model_name:
                    latest_models.append(model)
                    break
        
        # 按模型名称排序，最新版本在前
        latest_models.sort(key=lambda x: x.get('name', ''), reverse=True)
        
        return latest_models
    
    def print_models_info(self, models: List[Dict]):
        """
        打印模型信息
        
        Args:
            models: 模型列表
        """
        if not models:
            print("未获取到任何模型信息")
            return
            
        print(f"\n=== Google Gemini 模型列表 (获取时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}) ===\n")
        
        for i, model in enumerate(models, 1):
            name = model.get('name', 'N/A')
            display_name = model.get('display_name', 'N/A')
            description = model.get('description', 'N/A')
            input_limit = model.get('input_token_limit', 'N/A')
            output_limit = model.get('output_token_limit', 'N/A')
            
            print(f"{i}. 模型名称: {name}")
            print(f"   显示名称: {display_name}")
            print(f"   描述: {description}")
            print(f"   输入token限制: {input_limit}")
            print(f"   输出token限制: {output_limit}")
            print("-" * 80)

def main():
    """主函数"""
    # 设置API密钥 (需要从Google AI Studio获取)
    api_key = os.getenv('GOOGLE_AI_API_KEY')
    
    if not api_key:
        print("请设置GOOGLE_AI_API_KEY环境变量或在代码中提供API密钥")
        print("获取API密钥: https://makersuite.google.com/app/apikey")
        return
    
    fetcher = GeminiModelsFetcher(api_key)
    
    print("正在获取Google Gemini模型列表...")
    
    # 尝试多种方法获取模型
    models = []
    
    # 方法1: 使用新版SDK (推荐)
    print("\n方法1: 尝试使用新版Google GenAI SDK...")
    models = fetcher.get_models_via_new_sdk()
    
    # 方法2: 使用旧版SDK (如果新版失败)
    if not models:
        print("\n方法2: 尝试使用旧版Google Generative AI SDK...")
        models = fetcher.get_models_via_sdk()
    
    # 方法3: 使用REST API (如果SDK都失败)
    if not models:
        print("\n方法3: 尝试使用REST API...")
        models = fetcher.get_models_via_rest_api()
    
    if models:
        # 过滤最新模型
        latest_models = fetcher.filter_latest_models(models)
        
        print(f"\n找到 {len(models)} 个模型，其中 {len(latest_models)} 个是最新的Gemini模型")
        
        # 打印最新模型信息
        fetcher.print_models_info(latest_models)
        
        # 打印当前最受推荐的模型
        print("\n=== 当前推荐的最新模型 ===")
        recommended_models = [
            "gemini-2.5-pro",
            "gemini-2.5-flash", 
            "gemini-2.0-flash-001",
            "gemini-1.5-pro-002",
            "gemini-1.5-flash-002"
        ]
        
        for model_id in recommended_models:
            for model in latest_models:
                if model_id in model.get('name', '').lower():
                    print(f"✓ {model.get('name')}")
                    break
        
    else:
        print("获取模型列表失败，请检查API密钥和网络连接")

if __name__ == "__main__":
    main()

# 使用示例：
"""
# 1. 设置环境变量
export GOOGLE_AI_API_KEY="your_api_key_here"

# 2. 安装依赖
pip install google-genai google-generativeai requests

# 3. 运行脚本
python gemini_models_fetcher.py

# 或者直接在代码中使用：
fetcher = GeminiModelsFetcher("your_api_key")
models = fetcher.get_models_via_new_sdk()
latest = fetcher.filter_latest_models(models)
fetcher.print_models_info(latest)
"""