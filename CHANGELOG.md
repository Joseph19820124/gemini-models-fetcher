# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Add support for Vertex AI authentication
- Add model performance benchmarking
- Add model comparison features
- Add support for custom model filtering rules
- Add web interface for model browsing

## [1.0.0] - 2025-06-06

### Added
- Initial release of Gemini Models Fetcher
- Support for multiple API access methods:
  - Google GenAI SDK (new v1.0+)
  - Google Generative AI SDK (legacy)
  - REST API fallback
- Smart model filtering for latest Gemini models
- Comprehensive error handling and fallback mechanisms
- Detailed model information display including:
  - Model names and display names
  - Descriptions
  - Input/output token limits
  - Supported generation methods
- Command-line interface
- Programmatic API for integration
- Example scripts for basic and advanced usage
- Complete documentation and setup guide
- MIT license
- Python 3.8+ support

### Features
- **Multi-SDK Support**: Automatically tries multiple methods to ensure compatibility
- **Intelligent Filtering**: Identifies latest Gemini 2.5, 2.0, and 1.5 series models
- **Robust Error Handling**: Graceful degradation if SDKs fail
- **Detailed Reporting**: Comprehensive model information and statistics
- **Export Functionality**: Save results to JSON format
- **Model Analysis**: Compare models by capabilities and limits

### Documentation
- Comprehensive README with installation and usage instructions
- API reference documentation
- Basic usage examples
- Advanced usage examples with analysis features
- Contributing guidelines
- FAQ section

### Development
- GitHub Actions CI/CD pipeline
- Automated testing across Python 3.8-3.12
- Code linting and formatting checks
- Import and basic functionality testing

### Dependencies
- `google-genai>=1.0.0` - New Google GenAI SDK
- `google-generativeai>=0.7.0` - Legacy Google Generative AI SDK  
- `requests>=2.28.0` - HTTP requests library
- `typing-extensions>=4.0.0` - Type hints for older Python versions

---

## Release Notes

### v1.0.0 Release Highlights

This initial release provides a comprehensive solution for fetching and analyzing Google Gemini model information. Key highlights include:

🚀 **Multi-Method Access**: Three different ways to access the Gemini API ensure maximum compatibility and reliability.

🔍 **Smart Filtering**: Automatically identifies the latest and most relevant Gemini models from the complete API response.

📊 **Detailed Analysis**: Get comprehensive information about each model including capabilities, limits, and supported features.

🛡️ **Robust Design**: Extensive error handling and fallback mechanisms ensure the tool works reliably across different environments.

🎯 **Easy Integration**: Both command-line and programmatic interfaces make it easy to integrate into existing workflows.

### Supported Models (as of v1.0.0)

- **Gemini 2.5 Pro**: State-of-the-art reasoning model with thinking capabilities
- **Gemini 2.5 Flash**: Balanced performance and cost efficiency
- **Gemini 2.0 Flash**: Next-generation multimodal model
- **Gemini 2.0 Flash-Lite**: Cost-optimized version
- **Gemini 1.5 Pro**: Mid-size multimodal model
- **Gemini 1.5 Flash**: Fast and versatile model
- **Gemini 1.5 Flash-8B**: Lightweight model

### Getting Started

1. Get a free API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Install the package: `pip install -r requirements.txt`
3. Set your API key: `export GOOGLE_AI_API_KEY="your_key"`
4. Run the script: `python gemini_models_fetcher.py`

For detailed instructions, see the [README](README.md).

### Contributing

We welcome contributions! Please see our [contributing guidelines](README.md#贡献) for more information.

### Support

- 📖 [Documentation](README.md)
- 🐛 [Issue Tracker](https://github.com/Joseph19820124/gemini-models-fetcher/issues)
- 💬 [Discussions](https://github.com/Joseph19820124/gemini-models-fetcher/discussions)

---

*For more information about this project, visit the [GitHub repository](https://github.com/Joseph19820124/gemini-models-fetcher).*