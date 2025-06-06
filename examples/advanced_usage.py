#!/usr/bin/env python3
"""
高级使用示例
演示GeminiModelsFetcher的高级功能
"""

import os
import sys
import json
from datetime import datetime

# 添加父目录到路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gemini_models_fetcher import GeminiModelsFetcher

def save_models_to_json(models, filename="gemini_models.json"):
    """将模型信息保存到JSON文件"""
    data = {
        "timestamp": datetime.now().isoformat(),
        "total_models": len(models),
        "models": models
    }
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"模型信息已保存到 {filename}")

def compare_model_generations(models):
    """比较不同代系的模型"""
    generations = {
        "1.0": [],
        "1.5": [],
        "2.0": [],
        "2.5": []
    }
    
    for model in models:
        name = model.get('name', '').lower()
        if 'gemini-1.0' in name:
            generations["1.0"].append(model)
        elif 'gemini-1.5' in name:
            generations["1.5"].append(model)
        elif 'gemini-2.0' in name:
            generations["2.0"].append(model)
        elif 'gemini-2.5' in name:
            generations["2.5"].append(model)
    
    print("\n=== 不同代系模型统计 ===")
    for gen, model_list in generations.items():
        print(f"Gemini {gen}: {len(model_list)} 个模型")
        for model in model_list:
            print(f"  - {model.get('name')}")

def analyze_model_capabilities(models):
    """分析模型功能"""
    print("\n=== 模型功能分析 ===")
    
    capabilities = {}
    
    for model in models:
        methods = model.get('supported_generation_methods', [])
        for method in methods:
            if method not in capabilities:
                capabilities[method] = []
            capabilities[method].append(model.get('name'))
    
    for capability, model_names in capabilities.items():
        print(f"\n{capability}: {len(model_names)} 个模型")
        for name in model_names[:5]:  # 只显示前5个
            print(f"  - {name}")
        if len(model_names) > 5:
            print(f"  ... 还有 {len(model_names) - 5} 个模型")

def find_best_models_by_criteria(models):
    """根据不同标准找出最佳模型"""
    print("\n=== 最佳模型推荐 ===")
    
    # 最大输入token限制
    max_input_model = None
    max_input_tokens = 0
    
    # 最大输出token限制
    max_output_model = None
    max_output_tokens = 0
    
    # 最新模型
    latest_models = []
    
    for model in models:
        # 检查输入token限制
        input_limit = model.get('input_token_limit')
        if input_limit and isinstance(input_limit, int) and input_limit > max_input_tokens:
            max_input_tokens = input_limit
            max_input_model = model
        
        # 检查输出token限制
        output_limit = model.get('output_token_limit')
        if output_limit and isinstance(output_limit, int) and output_limit > max_output_tokens:
            max_output_tokens = output_limit
            max_output_model = model
        
        # 检查是否是最新模型
        name = model.get('name', '').lower()
        if 'gemini-2.5' in name:
            latest_models.append(model)
    
    if max_input_model:
        print(f"最大输入token限制: {max_input_model.get('name')} ({max_input_tokens:,} tokens)")
    
    if max_output_model:
        print(f"最大输出token限制: {max_output_model.get('name')} ({max_output_tokens:,} tokens)")
    
    if latest_models:
        print(f"\n最新模型 (Gemini 2.5): {len(latest_models)} 个")
        for model in latest_models:
            print(f"  - {model.get('name')}")

def create_model_report(models):
    """创建详细的模型报告"""
    print("\n=== 详细模型报告 ===")
    
    report = {
        "生成时间": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "总模型数": len(models),
        "模型分类": {
            "按代系": {},
            "按类型": {},
            "按功能": {}
        },
        "token限制统计": {
            "平均输入限制": 0,
            "平均输出限制": 0,
            "最大输入限制": 0,
            "最大输出限制": 0
        }
    }
    
    # 统计按代系分类
    for model in models:
        name = model.get('name', '').lower()
        for version in ['1.0', '1.5', '2.0', '2.5']:
            if f'gemini-{version}' in name:
                if version not in report["模型分类"]["按代系"]:
                    report["模型分类"]["按代系"][version] = 0
                report["模型分类"]["按代系"][version] += 1
                break
    
    # 统计按类型分类
    for model in models:
        name = model.get('name', '').lower()
        if 'pro' in name:
            model_type = 'Pro'
        elif 'flash' in name:
            model_type = 'Flash'
        elif 'nano' in name:
            model_type = 'Nano'
        else:
            model_type = 'Other'
        
        if model_type not in report["模型分类"]["按类型"]:
            report["模型分类"]["按类型"][model_type] = 0
        report["模型分类"]["按类型"][model_type] += 1
    
    # 计算token限制统计
    input_limits = []
    output_limits = []
    
    for model in models:
        input_limit = model.get('input_token_limit')
        output_limit = model.get('output_token_limit')
        
        if input_limit and isinstance(input_limit, int):
            input_limits.append(input_limit)
        
        if output_limit and isinstance(output_limit, int):
            output_limits.append(output_limit)
    
    if input_limits:
        report["token限制统计"]["平均输入限制"] = sum(input_limits) // len(input_limits)
        report["token限制统计"]["最大输入限制"] = max(input_limits)
    
    if output_limits:
        report["token限制统计"]["平均输出限制"] = sum(output_limits) // len(output_limits)
        report["token限制统计"]["最大输出限制"] = max(output_limits)
    
    # 打印报告
    print(json.dumps(report, indent=2, ensure_ascii=False))
    
    return report

def main():
    """主函数"""
    api_key = os.getenv('GOOGLE_AI_API_KEY')
    
    if not api_key:
        print("请设置GOOGLE_AI_API_KEY环境变量")
        return
    
    fetcher = GeminiModelsFetcher(api_key)
    
    print("正在获取模型信息...")
    models = fetcher.get_models_via_new_sdk()
    
    if not models:
        models = fetcher.get_models_via_sdk()
    
    if not models:
        models = fetcher.get_models_via_rest_api()
    
    if models:
        print(f"成功获取 {len(models)} 个模型")
        
        # 运行高级分析
        compare_model_generations(models)
        analyze_model_capabilities(models)
        find_best_models_by_criteria(models)
        
        # 创建详细报告
        report = create_model_report(models)
        
        # 保存到JSON文件
        save_models_to_json(models)
        
        # 保存报告
        with open('model_report.json', 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print("\n详细报告已保存到 model_report.json")
        
    else:
        print("获取模型失败")

if __name__ == "__main__":
    main()