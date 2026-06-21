# 安装和使用指南

## 方式一：使用预编译的 .exe （推荐 - 最简单）

### 步骤
1. 从 [GitHub Releases](https://github.com/awl2248/bilibili-subtitle-extractor/releases) 下载最新的 `B站字幕提取器.exe`
2. 双击运行
3. 按照界面提示操作

**优点：** 开箱即用，无需安装任何依赖

---

## 方式二：从源代码运行

### 前置要求
- Windows 7 或更新版本
- Python 3.8 或更高版本
- pip（Python包管理工具）

### 安装步骤

#### 1. 检查Python是否已安装
```bash
python --version
```

如果显示版本号，说明已安装。如果显示"找不到命令"，请：
- 访问 [python.org](https://www.python.org/downloads/)
- 下载 Windows 64-bit 版本
- 安装时 **勾选 "Add Python to PATH"**
- 重启电脑

#### 2. 下载项目代码
```bash
git clone https://github.com/awl2248/bilibili-subtitle-extractor.git
cd bilibili-subtitle-extractor
```

或者：
- 访问 GitHub 仓库
- 点击 "Code" → "Download ZIP"
- 解压到本地
- 打开该文件夹

#### 3. 安装依赖
```bash
pip install -r requirements.txt
```

#### 4. 运行程序
```bash
python main.py
```

---

## 方式三：自己构建 .exe

### 前置要求
- 完成"方式二"的所有步骤
- 安装 PyInstaller

### 构建步骤

#### 1. 安装 PyInstaller
```bash
pip install pyinstaller
```

#### 2. 运行构建脚本
```bash
python build_exe.py
```

#### 3. 找到生成的 .exe
构建完成后，执行文件位于：
```
dist/B站字幕提取器.exe
```

可以将其移到任何地方使用，或发给朋友使用。

---

## 常见问题

### Q: 打开程序时出现 "Python不是内部或外部命令"
**A:** Python 未正确安装或未添加到 PATH。请重新安装 Python，并在安装时勾选 "Add Python to PATH"。

### Q: 提取时显示 "无法获取视频信息"
**A:** 
- 检查网络连接
- 检查URL是否正确（应该是 `https://www.bilibili.com/video/BV...` 的格式）
- 某些视频可能有地域限制或权限限制

### Q: "无法获取字幕，可能视频没有字幕"
**A:** 该视频确实没有上传字幕。B站只有部分视频有字幕文件。

### Q: 如何卸载程序？
**A:** 
- 如果是 .exe 单文件，直接删除即可
- 如果是从源代码运行，删除项目文件夹即可
- 如需清理 Python 环境，运行：`pip uninstall yt-dlp requests chardet`

---

## 获取帮助

遇到问题？
1. 查看本文件中的"常见问题"部分
2. 检查 [GitHub Issues](https://github.com/awl2248/bilibili-subtitle-extractor/issues)
3. 提交新的 Issue 或 Pull Request

---

## 下一步

- 📖 查看 [README.md](README.md) 了解功能详情
- 🚀 开始使用程序提取字幕
- 💡 提供反馈和建议
