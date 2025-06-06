#!/usr/bin/env python3
"""
Script to fetch the latest Google Gemini models list
Supports fetching model information via Gemini Developer API and Vertex AI API
"""

import os
import requests
from typing import List, Dict, Optional
from datetime import datetime

class GeminiModelsFetcher:
    """Class for fetching Google Gemini models list"""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the model fetcher
        
        Args:
            api_key: Google AI Studio API key, if not provided, will get from environment variable
        """
        self.api_key = api_key or os.getenv('GOOGLE_AI_API_KEY')
        self.base_url = "https://generativelanguage.googleapis.com/v1beta/models"
        
    def get_models_via_rest_api(self) -> List[Dict]:
        """
        Get all available Gemini models via REST API
        
        Returns:
            List of dictionaries containing model information
        """
        if not self.api_key:
            raise ValueError("API key is required. Please set GOOGLE_AI_API_KEY environment variable or pass api_key parameter")
            
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
            print(f"API request failed: {e}")
            return []
    
    def get_models_via_sdk(self) -> List[Dict]:
        """
        Get models list via Python SDK
        Requires installation: pip install google-generativeai
        
        Returns:
            List of dictionaries containing model information
        """
        try:
            import google.generativeai as genai
            
            if not self.api_key:
                raise ValueError("API key is required")
                
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
            print("Please install Google Generative AI SDK: pip install google-generativeai")
            return []
        except Exception as e:
            print(f"SDK model fetching failed: {e}")
            return []
    
    def get_models_via_new_sdk(self) -> List[Dict]:
        """
        Get models list via new Google GenAI SDK
        Requires installation: pip install google-genai
        
        Returns:
            List of dictionaries containing model information
        """
        try:
            from google import genai
            
            if not self.api_key:
                raise ValueError("API key is required")
                
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
            print("Please install new Google GenAI SDK: pip install google-genai")
            return []
        except Exception as e:
            print(f"New SDK model fetching failed: {e}")
            return []
    
    def filter_latest_models(self, models: List[Dict]) -> List[Dict]:
        """
        Filter out the latest Gemini models
        
        Args:
            models: List of all models
            
        Returns:
            List of latest Gemini models
        """
        latest_models = []
        
        # Define keywords for latest models
        latest_keywords = [
            'gemini-2.5',      # Gemini 2.5 series
            'gemini-2.0',      # Gemini 2.0 series
            'gemini-1.5',      # Gemini 1.5 series
        ]
        
        for model in models:
            model_name = model.get('name', '').lower()
            
            # Check if contains latest model keywords
            for keyword in latest_keywords:
                if keyword in model_name:
                    latest_models.append(model)
                    break
        
        # Sort by model name, latest versions first
        latest_models.sort(key=lambda x: x.get('name', ''), reverse=True)
        
        return latest_models
    
    def print_models_info(self, models: List[Dict]):
        """
        Print model information
        
        Args:
            models: List of models
        """
        if not models:
            print("No model information retrieved")
            return
            
        print(f"\n=== Google Gemini Models List (Retrieved: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}) ===\n")
        
        for i, model in enumerate(models, 1):
            name = model.get('name', 'N/A')
            display_name = model.get('display_name', 'N/A')
            description = model.get('description', 'N/A')
            input_limit = model.get('input_token_limit', 'N/A')
            output_limit = model.get('output_token_limit', 'N/A')
            
            print(f"{i}. Model Name: {name}")
            print(f"   Display Name: {display_name}")
            print(f"   Description: {description}")
            print(f"   Input Token Limit: {input_limit}")
            print(f"   Output Token Limit: {output_limit}")
            print("-" * 80)

def main():
    """Main function"""
    # Set API key (get from Google AI Studio)
    api_key = os.getenv('GOOGLE_AI_API_KEY')
    
    if not api_key:
        print("Please set GOOGLE_AI_API_KEY environment variable or provide API key in code")
        print("Get API key: https://makersuite.google.com/app/apikey")
        return
    
    fetcher = GeminiModelsFetcher(api_key)
    
    print("Fetching Google Gemini models list...")
    
    # Try multiple methods to get models
    models = []
    
    # Method 1: Use new SDK (recommended)
    print("\nMethod 1: Trying new Google GenAI SDK...")
    models = fetcher.get_models_via_new_sdk()
    
    # Method 2: Use legacy SDK (if new version fails)
    if not models:
        print("\nMethod 2: Trying legacy Google Generative AI SDK...")
        models = fetcher.get_models_via_sdk()
    
    # Method 3: Use REST API (if all SDKs fail)
    if not models:
        print("\nMethod 3: Trying REST API...")
        models = fetcher.get_models_via_rest_api()
    
    if models:
        # Filter latest models
        latest_models = fetcher.filter_latest_models(models)
        
        print(f"\nFound {len(models)} models, {len(latest_models)} are latest Gemini models")
        
        # Print latest model information
        fetcher.print_models_info(latest_models)
        
        # Print currently recommended models
        print("\n=== Currently Recommended Latest Models ===")
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
        print("Failed to retrieve models list, please check API key and network connection")

if __name__ == "__main__":
    main()

# Usage example:
"""
# 1. Set environment variable
export GOOGLE_AI_API_KEY="your_api_key_here"

# 2. Install dependencies
pip install google-genai google-generativeai requests

# 3. Run script
python gemini_models_fetcher.py

# Or use directly in code:
fetcher = GeminiModelsFetcher("your_api_key")
models = fetcher.get_models_via_new_sdk()
latest = fetcher.filter_latest_models(models)
fetcher.print_models_info(latest)
"""