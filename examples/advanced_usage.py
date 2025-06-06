#!/usr/bin/env python3
"""
Advanced Usage Examples
Demonstrates advanced features of GeminiModelsFetcher
"""

import os
import sys
import json
from datetime import datetime

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gemini_models_fetcher import GeminiModelsFetcher

def save_models_to_json(models, filename="gemini_models.json"):
    """Save model information to JSON file"""
    data = {
        "timestamp": datetime.now().isoformat(),
        "total_models": len(models),
        "models": models
    }
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"Model information saved to {filename}")

def compare_model_generations(models):
    """Compare models of different generations"""
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
    
    print("\n=== Model Generation Statistics ===")
    for gen, model_list in generations.items():
        print(f"Gemini {gen}: {len(model_list)} models")
        for model in model_list:
            print(f"  - {model.get('name')}")

def analyze_model_capabilities(models):
    """Analyze model capabilities"""
    print("\n=== Model Capabilities Analysis ===")
    
    capabilities = {}
    
    for model in models:
        methods = model.get('supported_generation_methods', [])
        for method in methods:
            if method not in capabilities:
                capabilities[method] = []
            capabilities[method].append(model.get('name'))
    
    for capability, model_names in capabilities.items():
        print(f"\n{capability}: {len(model_names)} models")
        for name in model_names[:5]:  # Only show first 5
            print(f"  - {name}")
        if len(model_names) > 5:
            print(f"  ... and {len(model_names) - 5} more models")

def find_best_models_by_criteria(models):
    """Find best models by different criteria"""
    print("\n=== Best Model Recommendations ===")
    
    # Maximum input token limit
    max_input_model = None
    max_input_tokens = 0
    
    # Maximum output token limit
    max_output_model = None
    max_output_tokens = 0
    
    # Latest models
    latest_models = []
    
    for model in models:
        # Check input token limit
        input_limit = model.get('input_token_limit')
        if input_limit and isinstance(input_limit, int) and input_limit > max_input_tokens:
            max_input_tokens = input_limit
            max_input_model = model
        
        # Check output token limit
        output_limit = model.get('output_token_limit')
        if output_limit and isinstance(output_limit, int) and output_limit > max_output_tokens:
            max_output_tokens = output_limit
            max_output_model = model
        
        # Check if it's a latest model
        name = model.get('name', '').lower()
        if 'gemini-2.5' in name:
            latest_models.append(model)
    
    if max_input_model:
        print(f"Highest input token limit: {max_input_model.get('name')} ({max_input_tokens:,} tokens)")
    
    if max_output_model:
        print(f"Highest output token limit: {max_output_model.get('name')} ({max_output_tokens:,} tokens)")
    
    if latest_models:
        print(f"\nLatest models (Gemini 2.5): {len(latest_models)} models")
        for model in latest_models:
            print(f"  - {model.get('name')}")

def create_model_report(models):
    """Create detailed model report"""
    print("\n=== Detailed Model Report ===")
    
    report = {
        "generated_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "total_models": len(models),
        "model_categories": {
            "by_generation": {},
            "by_type": {},
            "by_capability": {}
        },
        "token_limit_statistics": {
            "average_input_limit": 0,
            "average_output_limit": 0,
            "max_input_limit": 0,
            "max_output_limit": 0
        }
    }
    
    # Statistics by generation
    for model in models:
        name = model.get('name', '').lower()
        for version in ['1.0', '1.5', '2.0', '2.5']:
            if f'gemini-{version}' in name:
                if version not in report["model_categories"]["by_generation"]:
                    report["model_categories"]["by_generation"][version] = 0
                report["model_categories"]["by_generation"][version] += 1
                break
    
    # Statistics by type
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
        
        if model_type not in report["model_categories"]["by_type"]:
            report["model_categories"]["by_type"][model_type] = 0
        report["model_categories"]["by_type"][model_type] += 1
    
    # Calculate token limit statistics
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
        report["token_limit_statistics"]["average_input_limit"] = sum(input_limits) // len(input_limits)
        report["token_limit_statistics"]["max_input_limit"] = max(input_limits)
    
    if output_limits:
        report["token_limit_statistics"]["average_output_limit"] = sum(output_limits) // len(output_limits)
        report["token_limit_statistics"]["max_output_limit"] = max(output_limits)
    
    # Print report
    print(json.dumps(report, indent=2, ensure_ascii=False))
    
    return report

def main():
    """Main function"""
    api_key = os.getenv('GOOGLE_AI_API_KEY')
    
    if not api_key:
        print("Please set GOOGLE_AI_API_KEY environment variable")
        return
    
    fetcher = GeminiModelsFetcher(api_key)
    
    print("Fetching model information...")
    models = fetcher.get_models_via_new_sdk()
    
    if not models:
        models = fetcher.get_models_via_sdk()
    
    if not models:
        models = fetcher.get_models_via_rest_api()
    
    if models:
        print(f"Successfully retrieved {len(models)} models")
        
        # Run advanced analysis
        compare_model_generations(models)
        analyze_model_capabilities(models)
        find_best_models_by_criteria(models)
        
        # Create detailed report
        report = create_model_report(models)
        
        # Save to JSON file
        save_models_to_json(models)
        
        # Save report
        with open('model_report.json', 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print("\nDetailed report saved to model_report.json")
        
    else:
        print("Failed to retrieve models")

if __name__ == "__main__":
    main()