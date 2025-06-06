# Gemini Models Fetcher

一个用于获取Google最新Gemini模型信息的Python脚本。支持通过多种方式获取模型列表，包括最新的Google GenAI SDK、传统的Generative AI SDK以及REST API。

## 功能特点

- 🚀 **多种获取方式**: 支持新版SDK、旧版SDK和REST API三种方式
- 🔍 **智能过滤**: 自动识别和过滤最新的Gemini模型
- 📊 **详细信息**: 显示模型名称、描述、token限制等完整信息
- 🛡️ **错误处理**: 包含完善的错误处理和回退机制
- 🌐 **多语言支持**: 支持中文和英文输出

## 支持的模型

当前脚本能够获取以下最新Gemini模型信息：

### Gemini 2.5系列 (最新)
- **Gemini 2.5 Pro** - 最先进的推理模型，具有思考能力
- **Gemini 2.5 Flash** - 平衡性能和成本的高效模型

### Gemini 2.0系列
- **Gemini 2.0 Flash** - 下一代多模态模型
- **Gemini 2.0 Flash-Lite** - 优化成本和延迟的版本

### Gemini 1.5系列
- **Gemini 1.5 Pro** - 中型多模态模型
- **Gemini 1.5 Flash** - 快速多用途模型
- **Gemini 1.5 Flash-8B** - 轻量级模型

## 安装

### 1. 克隆仓库

```bash
git clone https://github.com/Joseph19820124/gemini-models-fetcher.git
cd gemini-models-fetcher
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 获取API密钥

访问 [Google AI Studio](https://makersuite.google.com/app/apikey) 获取免费的API密钥。

### 4. 设置环境变量

```bash
export GOOGLE_AI_API_KEY="your_api_key_here"
```

或者在Windows中：

```cmd
set GOOGLE_AI_API_KEY=your_api_key_here
```

## 使用方法

### 命令行使用

```bash
python gemini_models_fetcher.py
```

### 编程式使用

```python
from gemini_models_fetcher import GeminiModelsFetcher

# 创建获取器实例
fetcher = GeminiModelsFetcher("your_api_key")

# 获取模型列表
models = fetcher.get_models_via_new_sdk()

# 过滤最新模型
latest_models = fetcher.filter_latest_models(models)

# 打印模型信息
fetcher.print_models_info(latest_models)
```

## 输出示例

```
正在获取Google Gemini模型列表...

方法1: 尝试使用新版Google GenAI SDK...

找到 15 个模型，其中 8 个是最新的Gemini模型

=== Google Gemini 模型列表 (获取时间: 2025-06-06 08:42:54) ===

1. 模型名称: models/gemini-2.5-pro-preview
   显示名称: Gemini 2.5 Pro
   描述: 最先进的推理模型
   输入token限制: 2000000
   输出token限制: 8192
--------------------------------------------------------------------------------

2. 模型名称: models/gemini-2.5-flash-preview
   显示名称: Gemini 2.5 Flash
   描述: 高效的平衡性能模型
   输入token限制: 1000000
   输出token限制: 8192
--------------------------------------------------------------------------------

=== 当前推荐的最新模型 ===
✓ models/gemini-2.5-pro-preview
✓ models/gemini-2.5-flash-preview
✓ models/gemini-2.0-flash-001
```

## API参考

### GeminiModelsFetcher类

#### 构造函数

```python
GeminiModelsFetcher(api_key: Optional[str] = None)
```

#### 主要方法

- `get_models_via_new_sdk()`: 使用新版Google GenAI SDK获取模型
- `get_models_via_sdk()`: 使用旧版Google Generative AI SDK获取模型
- `get_models_via_rest_api()`: 使用REST API获取模型
- `filter_latest_models(models)`: 过滤最新的Gemini模型
- `print_models_info(models)`: 打印模型详细信息

## 示例代码

项目包含两个详细的示例文件：

### 基本使用示例 (`examples/basic_usage.py`)

演示如何：
- 获取所有可用模型
- 过滤特定类型的模型
- 比较不同模型的规格

```bash
python examples/basic_usage.py
```

### 高级使用示例 (`examples/advanced_usage.py`)

演示如何：
- 生成详细的模型报告
- 按不同标准分析模型
- 保存结果到JSON文件

```bash
python examples/advanced_usage.py
```

## 依赖项

- `google-genai` - 新版Google GenAI SDK
- `google-generativeai` - 传统的Google Generative AI SDK
- `requests` - HTTP请求库

## 错误处理

脚本包含多层错误处理机制：

1. **API密钥验证**: 检查环境变量或参数中的API密钥
2. **SDK回退**: 如果新版SDK失败，自动尝试旧版SDK
3. **REST API备用**: 如果所有SDK都失败，使用REST API
4. **网络错误处理**: 处理网络连接和API请求错误

## 贡献

欢迎提交Issue和Pull Request！

### 开发环境设置

1. Fork这个仓库
2. 创建特性分支: `git checkout -b feature/your-feature`
3. 提交更改: `git commit -am 'Add some feature'`
4. 推送到分支: `git push origin feature/your-feature`
5. 提交Pull Request

## 许可证

此项目使用MIT许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 更新日志

### v1.0.0 (2025-06-06)
- 初始版本发布
- 支持多种SDK和REST API
- 智能模型过滤功能
- 完善的错误处理机制

## 相关链接

- [Google AI Studio](https://makersuite.google.com/)
- [Gemini API文档](https://ai.google.dev/gemini-api/docs)
- [Google GenAI SDK](https://ai.google.dev/gemini-api/docs/sdks)
- [Vertex AI文档](https://cloud.google.com/vertex-ai/generative-ai/docs)

## 常见问题

### Q: 如何获取API密钥？
A: 访问 [Google AI Studio](https://makersuite.google.com/app/apikey) 并登录你的Google账户，然后创建一个新的API密钥。

### Q: 为什么需要多种获取方式？
A: 不同的SDK和API版本可能在不同时间更新，多种方式确保了更好的兼容性和可靠性。

### Q: 如何报告问题？
A: 请在GitHub上创建一个Issue，并提供详细的错误信息和重现步骤。

---

**注意**: 此脚本仅用于获取公开的模型信息，请确保遵守Google的使用条款和API配额限制。