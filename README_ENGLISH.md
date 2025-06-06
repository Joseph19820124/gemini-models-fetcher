# Gemini Models Fetcher - English Version

This is the English version of the Gemini Models Fetcher script. All output messages and comments have been translated to English for international users.

## 🌍 What's Different in This Branch

This branch (`english-version`) contains the same functionality as the main branch, but with:

- **English output messages**: All console output is in English
- **English comments**: All code comments and docstrings are in English  
- **English examples**: Both basic and advanced usage examples output English text

## 🚀 Quick Start

```bash
# Clone the English version
git clone -b english-version https://github.com/Joseph19820124/gemini-models-fetcher.git
cd gemini-models-fetcher

# Install dependencies
pip install -r requirements.txt

# Set your API key
export GOOGLE_AI_API_KEY="your_api_key_here"

# Run the script
python gemini_models_fetcher.py
```

## 📋 Sample Output

```
Fetching Google Gemini models list...

Method 1: Trying new Google GenAI SDK...

Found 15 models, 8 are latest Gemini models

=== Google Gemini Models List (Retrieved: 2025-06-06 09:04:15) ===

1. Model Name: models/gemini-2.5-pro-preview
   Display Name: Gemini 2.5 Pro
   Description: Most capable reasoning model
   Input Token Limit: 2000000
   Output Token Limit: 8192
--------------------------------------------------------------------------------

2. Model Name: models/gemini-2.5-flash-preview
   Display Name: Gemini 2.5 Flash  
   Description: Efficient balanced performance model
   Input Token Limit: 1000000
   Output Token Limit: 8192
--------------------------------------------------------------------------------

=== Currently Recommended Latest Models ===
✓ models/gemini-2.5-pro-preview
✓ models/gemini-2.5-flash-preview
✓ models/gemini-2.0-flash-001
```

## 🔧 Usage Examples

### Basic Usage
```bash
python examples/basic_usage.py
```

### Advanced Usage with Analysis  
```bash
python examples/advanced_usage.py
```

## 📚 Features

- **Multi-SDK Support**: Works with Google GenAI SDK, legacy SDK, and REST API
- **Smart Filtering**: Automatically identifies latest Gemini models
- **Detailed Analysis**: Shows model capabilities, token limits, and recommendations
- **Export Functions**: Save results to JSON files
- **Error Handling**: Graceful fallback if SDKs fail

## 🔗 Related Links

- **Main Repository**: [gemini-models-fetcher](https://github.com/Joseph19820124/gemini-models-fetcher)
- **Chinese Version**: Switch to `main` branch
- **Get API Key**: [Google AI Studio](https://makersuite.google.com/app/apikey)
- **Documentation**: [Gemini API Docs](https://ai.google.dev/gemini-api/docs)

## 📄 Language Support

- **🇺🇸 English Version**: You are here! (`english-version` branch)
- **🇨🇳 Chinese Version**: Switch to `main` branch for Chinese output

## 💡 Learning Purpose

This branch is perfect for:
- International users who prefer English output
- Learning how to internationalize Python applications
- Understanding the differences between localized versions
- Educational purposes and code study

## 🤝 Contributing

Contributions are welcome! Please see our [Contributing Guidelines](CONTRIBUTING.md) for more information.

---

**Note**: This English version maintains the same functionality as the Chinese version. Only the output language and comments have been changed for better international accessibility.