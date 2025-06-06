#!/usr/bin/env python3
"""
Basic Usage Examples
Demonstrates how to use GeminiModelsFetcher to get model information
"""

import os
import sys

# Add parent directory to path to import main module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gemini_models_fetcher import GeminiModelsFetcher

def example_basic_usage():
    """Basic usage example"""
    print("=== Basic Usage Example ===")
    
    # Get API key from environment variable
    api_key = os.getenv('GOOGLE_AI_API_KEY')
    
    if not api_key:
        print("Please set GOOGLE_AI_API_KEY environment variable")
        print("Get API key: https://makersuite.google.com/app/apikey")
        return
    
    # Create fetcher instance
    fetcher = GeminiModelsFetcher(api_key)
    
    # Get all models
    print("\n1. Getting all models...")
    models = fetcher.get_models_via_new_sdk()
    
    if not models:
        models = fetcher.get_models_via_sdk()
    
    if not models:
        models = fetcher.get_models_via_rest_api()
    
    if models:
        print(f"Found {len(models)} models")
        
        # Filter latest models
        print("\n2. Filtering latest models...")
        latest_models = fetcher.filter_latest_models(models)
        print(f"{len(latest_models)} are latest Gemini models")
        
        # Show model details
        print("\n3. Showing model details:")
        fetcher.print_models_info(latest_models[:3])  # Only show first 3
        
    else:
        print("Failed to get models")

def example_filter_specific_models():
    """Example of filtering specific models"""
    print("\n\n=== Specific Model Filtering Example ===")
    
    api_key = os.getenv('GOOGLE_AI_API_KEY')
    if not api_key:
        return
        
    fetcher = GeminiModelsFetcher(api_key)
    models = fetcher.get_models_via_new_sdk()
    
    if models:
        # Filter Gemini 2.5 models
        gemini_25_models = []
        for model in models:
            if 'gemini-2.5' in model.get('name', '').lower():
                gemini_25_models.append(model)
        
        print(f"Found {len(gemini_25_models)} Gemini 2.5 models:")
        for model in gemini_25_models:
            print(f"- {model.get('name')}")
        
        # Filter Flash models
        flash_models = []
        for model in models:
            if 'flash' in model.get('name', '').lower():
                flash_models.append(model)
        
        print(f"\nFound {len(flash_models)} Flash models:")
        for model in flash_models:
            print(f"- {model.get('name')}")

def example_model_comparison():
    """Model comparison example"""
    print("\n\n=== Model Comparison Example ===")
    
    api_key = os.getenv('GOOGLE_AI_API_KEY')
    if not api_key:
        return
        
    fetcher = GeminiModelsFetcher(api_key)
    models = fetcher.get_models_via_new_sdk()
    
    if models:
        # Compare token limits of different models
        print("Model token limits comparison:")
        print(f"{'Model Name':<30} {'Input Limit':<15} {'Output Limit':<15}")
        print("-" * 60)
        
        for model in models[:10]:  # Only show first 10
            name = model.get('name', 'N/A')[-30:]  # Get last 30 characters
            input_limit = model.get('input_token_limit', 'N/A')
            output_limit = model.get('output_token_limit', 'N/A')
            
            print(f"{name:<30} {str(input_limit):<15} {str(output_limit):<15}")

if __name__ == "__main__":
    # Run all examples
    example_basic_usage()
    example_filter_specific_models()
    example_model_comparison()