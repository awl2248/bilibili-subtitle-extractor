# ✅ 如何验证安装是否成功

这份指南教你如何检查 **第 4 步和第 5 步** 是否完成。

---

## 📋 快速检查方法

### **方法 1：查看命令提示符的输出信息**

当你运行这两个命令时，系统会输出一些信息。**成功的标志** 包括：

#### 第 4 步：`pip install -r requirements.txt`

✅ **成功的输出示例：**
```
Collecting yt-dlp>=2023.11.16
  Downloading yt-dlp-2024.1.1-py2.py3-none-any.whl (1.8 MB)
     |████████████████████████████████| 1.8 MB 16.7 MB/s
Installing collected packages: yt-dlp, requests, chardet, python-dotenv
Successfully installed yt-dlp-2024.1.1 requests-2.31.0 chardet-5.2.0 python-dotenv-1.0.0
```

❌ **失败的输出示例：**
```
ERROR: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied
```

---

#### 第 5 步：`pip install pyinstaller`

✅ **成功的输出示例：**
```
Collecting pyinstaller
  Downloading pyinstaller-6.1.0-py3-none-any.whl (2.5 MB)
     |████████████████████████████████| 2.5 MB 15.3 MB/s
Installing collected packages: pyinstaller, ...
Successfully installed pyinstaller-6.1.0
```

❌ **失败的输出示例：**
```
ERROR: Could not find a version that satisfies the requirement pyinstaller
```

---

## 🔍 详细验证方法

### **方法 2：逐个检查每个包**

打开命令提示符，逐个验证已安装的包。

#### 检查 `yt-dlp`
```bash
pip show yt-dlp
```

✅ 成功输出：
```
Name: yt-dlp
Version: 2024.1.1
Summary: A youtube-dl fork with additional features and fixes
Location: C:\Users\你的用户名\AppData\Local\Programs\Python\Python310\lib\site-packages
```

如果显示这样的信息，说明 ✅ **安装成功**

❌ 如果输出：`WARNING: Package(s) not found`，说明 ❌ **未安装**

---

#### 检查 `requests`
```bash
pip show requests
```

#### 检查 `chardet`
```bash
pip show chardet
```

#### 检查 `python-dotenv`
```bash
pip show python-dotenv
```

#### 检查 `PyInstaller`
```bash
pip show pyinstaller
```

---

### **方法 3：一次性检查所有包**

运行这个命令查���所有已安装的包：

```bash
pip list
```

✅ 成功输出（节选）：
```
Package            Version
------------------ ---------
chardet            5.2.0
pip                23.3.1
python-dotenv      1.0.0
pyinstaller        6.1.0
requests           2.31.0
yt-dlp             2024.1.1
```

看到上面这些包都在列表里，说明 ✅ **全部安装成功**

---

## 🧪 进阶验证方法

### **方法 4：在 Python 中测试导入**

打开命令提示符，输入：

```bash
python
```

进入 Python 交互式界面，然后逐个测试：

#### 测试 yt-dlp
```python
import yt_dlp
print("yt-dlp 版本:", yt_dlp.__version__)
```

✅ 成功输出：`yt-dlp 版本: 2024.1.1`

#### 测试 requests
```python
import requests
print("requests 版本:", requests.__version__)
```

✅ 成功输出：`requests 版本: 2.31.0`

#### 测试 chardet
```python
import chardet
print("chardet 版本:", chardet.__version__)
```

✅ 成功输出：`chardet 版本: 5.2.0`

#### 测试 PyInstaller
```python
import PyInstaller
print("PyInstaller 已成功安装")
```

✅ 成功输出：`PyInstaller 已成功安装`

**退出 Python：**
```python
exit()
```

或按 `Ctrl + Z` 然后 `Enter`

---

## 📊 完整检查清单

打印下面这个清单，逐个检查：

```
□ 命令 pip install -r requirements.txt 显示 "Successfully installed"
  
□ 命令 pip show yt-dlp 显示版本号
  
□ 命令 pip show requests 显示版本号
  
□ 命令 pip show chardet 显示版本号
  
□ 命令 pip show python-dotenv 显示版本号
  
□ 命令 pip install pyinstaller 显示 "Successfully installed"
  
□ 命令 pip show pyinstaller 显示版本号
  
□ 在 Python 中导入 yt_dlp 成功
  
□ 在 Python 中导入 requests 成功
  
□ 在 Python 中导入 chardet 成功
  
□ 在 Python 中导入 PyInstaller 成功
```

**如果全部勾选，说明 ✅ 所有安装都成功了！**

---

## ⚠️ 常见问题和解决方案

### Q: 显示 "WARNING: Package(s) not found"
**A:** 这个包没有安装。重新运行：
```bash
pip install 包名
```

例如：
```bash
pip install yt-dlp
```

---

### Q: 显示 "ERROR: Could not install packages"
**A:** 可能的原因和解决方案：

**1. 网络问题**
- 检查网络连接
- 重新运行命令

**2. 权限问题**
- 以管理员身份打开命令提示符
- 重新运行命令

**3. Python 版本问题**
- 确保使用 Python 3.8+
- 验证：`python --version`

---

### Q: 显示 "Module not found" 或 "No module named"
**A:** 说明包未成功安装。尝试：
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

### Q: 导入时显示 "ImportError"
**A:** 通常是因为：
1. 包未安装 - 重新安装
2. Python 环境混乱 - 重启命令提示符

---

## 🎯 验证流程总结

### **快速验证（1 分钟）**

1. 打开命令提示符
2. 运行：`pip list | find "yt-dlp"`（Windows）
3. 如果显示版本号，说明 ✅ 安装成功

### **完整验证（5 分钟）**

1. 运行：`pip show yt-dlp`
2. 运行：`pip show requests`
3. 运行：`pip show chardet`
4. 运行：`pip show python-dotenv`
5. 运行：`pip show pyinstaller`
6. 全部显示版本号 → ✅ 成功

### **最靠谱的验证（10 分钟）**

1. 进入 Python：`python`
2. 依次导入各个包
3. 全部成功 → ✅ 完全就绪，可以打包了

---

## ✅ 验证成功后的下一步

当你确认所有包都安装成功后，就可以进行 **第 6 步：一键打包** 了！

```bash
python build_exe.py
```

---

## 🆘 如果验证失败怎么办？

### **情景 1：某个包显示 "not found"**

重新安装这个包：
```bash
pip install 包名
```

然后再次验证。

### **情景 2：所有包都显示 "not found"**

重新运行：
```bash
pip install -r requirements.txt
pip install pyinstaller
```

### **情景 3：导入失败但 pip show 显示已安装**

尝试重启命令提示符，然后再次测试导入。

### **情景 4：还是有问题**

1. 卸载所有相关包：
   ```bash
   pip uninstall yt-dlp requests chardet python-dotenv pyinstaller -y
   ```

2. 重新安装：
   ```bash
   pip install -r requirements.txt
   pip install pyinstaller
   ```

3. 重新验证

---

## 📸 示例截图

### 成功的命令输出：

```
C:\Users\awl2248\bilibili-subtitle-extractor> pip install -r requirements.txt
Collecting yt-dlp>=2023.11.16
  Using cached yt_dlp-2024.1.1-py2.py3-none-any.whl (1.8 MB)
Collecting requests>=2.31.0
  Using cached requests-2.31.0-py3-none-any.whl (62 kB)
Collecting chardet>=5.2.0
  Using cached chardet-5.2.0-py3-none-any.whl (193 kB)
Collecting python-dotenv>=1.0.0
  Using cached python_dotenv-1.0.0-py3-none-any.whl (14 kB)
Installing collected packages: yt-dlp, requests, chardet, python-dotenv
Successfully installed yt-dlp-2024.1.1 requests-2.31.0 chardet-5.2.0 python-dotenv-1.0.0

C:\Users\awl2248\bilibili-subtitle-extractor> pip install pyinstaller
Collecting pyinstaller
  Using cached pyinstaller-6.1.0-py3-none-any.whl (2.5 MB)
...
Successfully installed pyinstaller-6.1.0
```

---

## 🎓 常用命令速查表

| 目标 | 命令 |
|------|------|
| 检查特定包版本 | `pip show 包名` |
| 列出所有已安装的包 | `pip list` |
| 安装单个包 | `pip install 包名` |
| 安装特定版本 | `pip install 包名==版本号` |
| 卸载包 | `pip uninstall 包名` |
| 升级包 | `pip install --upgrade 包名` |
| 导入包测试 | `python -c \"import 包名; print('OK')\"` |

---

## 💡 建议

1. **保存这份指南** - 截图或收藏这个页面
2. **逐步验证** - 不要跳步，确保每一步都成功
3. **遇到问题时** - 检查本页面的"常见问题"部分
4. **准备好后** - 就可以进行打包了！

---

**准备好了吗？开始验证吧！** ✅
