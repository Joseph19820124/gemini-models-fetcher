# Contributing to Gemini Models Fetcher

首先，感谢你对 Gemini Models Fetcher 项目的关注和贡献！我们欢迎任何形式的贡献，包括但不限于：

- 🐛 Bug 报告
- 💡 功能建议
- 📝 文档改进
- 🔧 代码修复
- ✨ 新功能开发

## 开发环境设置

### 1. Fork 和克隆仓库

```bash
# Fork 项目到你的 GitHub 账户，然后克隆
git clone https://github.com/your-username/gemini-models-fetcher.git
cd gemini-models-fetcher

# 添加上游仓库
git remote add upstream https://github.com/Joseph19820124/gemini-models-fetcher.git
```

### 2. 创建开发环境

```bash
# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或者
venv\Scripts\activate  # Windows

# 安装依赖
pip install -r requirements.txt
pip install pytest pytest-cov flake8 black isort
```

### 3. 设置 API 密钥

```bash
# 获取 Google AI Studio API 密钥
# https://makersuite.google.com/app/apikey

export GOOGLE_AI_API_KEY="your_api_key_here"
```

## 代码规范

### Python 代码风格

我们遵循 [PEP 8](https://pep8.org/) 代码规范，并使用以下工具：

- **flake8**: 代码检查
- **black**: 代码格式化
- **isort**: 导入排序

```bash
# 代码格式化
black gemini_models_fetcher.py examples/
isort gemini_models_fetcher.py examples/

# 代码检查
flake8 gemini_models_fetcher.py examples/
```

### 代码质量要求

- ✅ 所有函数和类必须有适当的文档字符串
- ✅ 代码必须通过 flake8 检查
- ✅ 必须包含类型提示（Type Hints）
- ✅ 新功能需要有相应的测试
- ✅ 保持向后兼容性

## 提交流程

### 1. 创建分支

```bash
# 确保在最新的 main 分支
git checkout main
git pull upstream main

# 创建新的功能分支
git checkout -b feature/your-feature-name
# 或者修复分支
git checkout -b fix/issue-description
```

### 2. 进行开发

- 遵循代码规范
- 编写清晰的提交信息
- 保持提交原子性（一个提交只做一件事）

### 3. 测试

```bash
# 运行基本测试
python -c "from gemini_models_fetcher import GeminiModelsFetcher; print('Import test passed')"

# 运行功能测试
python examples/basic_usage.py
python examples/advanced_usage.py

# 代码质量检查
flake8 .
```

### 4. 提交代码

```bash
git add .
git commit -m "feat: add new feature description"
# 或者
git commit -m "fix: fix bug description"
```

### 5. 推送和创建 Pull Request

```bash
git push origin feature/your-feature-name
```

然后在 GitHub 上创建 Pull Request。

## 提交信息规范

我们使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

- `feat`: 新功能
- `fix`: 修复 bug
- `docs`: 文档更新
- `style`: 代码格式修改
- `refactor`: 重构代码
- `test`: 添加或修改测试
- `chore`: 维护任务

示例：
```
feat: add support for Vertex AI authentication
fix: handle API rate limiting properly
docs: update installation instructions
```

## 测试指南

### 单元测试

```python
# 创建测试文件 test_gemini_models_fetcher.py
import pytest
from gemini_models_fetcher import GeminiModelsFetcher

def test_model_filtering():
    fetcher = GeminiModelsFetcher()
    sample_models = [
        {'name': 'models/gemini-2.5-pro', 'description': 'Test'},
        {'name': 'models/text-embedding-004', 'description': 'Test'}
    ]
    result = fetcher.filter_latest_models(sample_models)
    assert len(result) == 1
    assert 'gemini-2.5' in result[0]['name']
```

### 集成测试

如果你有 API 密钥，可以运行完整的集成测试：

```bash
python gemini_models_fetcher.py
```

## 文档贡献

### README 更新

如果你的更改影响用户使用方式，请更新：
- 安装说明
- 使用示例
- API 文档

### 示例代码

添加新功能时，请在 `examples/` 目录中提供使用示例。

## 问题报告

### Bug 报告

请包含以下信息：

1. **环境信息**:
   - Python 版本
   - 操作系统
   - 依赖版本

2. **重现步骤**:
   - 详细的操作步骤
   - 期望结果
   - 实际结果

3. **错误信息**:
   - 完整的错误堆栈
   - 相关日志

### 功能请求

请描述：
- 功能的使用场景
- 期望的行为
- 可能的实现方案

## 发布流程

### 版本管理

我们使用 [Semantic Versioning](https://semver.org/):

- `MAJOR`: 不兼容的 API 更改
- `MINOR`: 向后兼容的功能添加
- `PATCH`: 向后兼容的 bug 修复

### 发布步骤

1. 更新 `CHANGELOG.md`
2. 更新 `setup.py` 中的版本号
3. 创建 Git 标签
4. 发布到 PyPI（维护者负责）

## 代码审查

所有的 Pull Request 都需要经过代码审查：

### 审查要点

- ✅ 代码功能正确性
- ✅ 代码质量和可读性
- ✅ 测试覆盖率
- ✅ 文档完整性
- ✅ 性能影响
- ✅ 安全性考虑

### 回应审查

- 友好地回应审查意见
- 解释设计决策
- 及时修复指出的问题

## 社区准则

### 行为准则

我们致力于创建一个友好、包容的社区环境：

- 🤝 尊重不同观点和经验
- 💭 提供建设性的反馈
- 🌟 关注什么对社区最好
- 🤗 对新贡献者表现出友善

### 沟通

- 使用清晰、友好的语言
- 保持专业和尊重
- 及时回应问题和评论

## 获得帮助

如果你需要帮助：

- 📖 查阅 [README](README.md) 和 [CHANGELOG](CHANGELOG.md)
- 🐛 在 [Issues](https://github.com/Joseph19820124/gemini-models-fetcher/issues) 中搜索已有问题
- 💬 创建新的 Issue 描述你的问题
- 📧 联系维护者

## 致谢

感谢所有为这个项目做出贡献的开发者！你们的努力让这个项目变得更好。

---

再次感谢你的贡献！🎉