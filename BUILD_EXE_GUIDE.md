# 📦 一键打包指南 - 生成 .exe 可执行文件

这份指南会教你如何将 Python 项目打包成一个独立的 Windows .exe 可执行文件，之后就可以直接双击运行，无需安装 Python！

---

## ⏱️ 预计时间

- **准备环境**：5 分钟
- **下载项目**：2 分钟
- **打包过程**：10-15 分钟
- **总耗时**：20 分钟左右

---

## 📋 前置要求

✅ Windows 7 或更新版本
✅ 网络连接（下载依赖）
✅ 至少 500MB 硬盘空间
✅ 管理员权限（推荐）

---

## 🛠️ 详细步骤

### **第 1 步：安装 Python**

**如果你已经装过 Python，跳到第 2 步**

#### 1.1 下载 Python

访问 https://www.python.org/downloads/

![download python](https://i.imgur.com/xxx.png)

- 点击 **"Download Python 3.10.x"** （或最新版本）
- 选择 **Windows installer (64-bit)**

#### 1.2 安装 Python

1. 双击下载的 `.exe` 文件
2. **重要！** 勾选 ✅ **"Add Python to PATH"**
   
   ![Add Python to PATH](https://i.imgur.com/xxx.png)

3. 点击 **"Install Now"** 或 **"Customize installation"**
4. 等待安装完成
5. 点击 **"Close"**

#### 1.3 验证安装

打开 **命令提示符**（Windows 命令行）：
- 按 `Win + R`
- 输入 `cmd`
- 按 Enter

输入以下命令检查：
```bash
python --version
```

如果显示版本号（如 `Python 3.10.x`），说明安装成功！✅

---

### **第 2 步：下载项目文件**

#### 方法 A：使用 Git（推荐，如果你装过 Git）

打开命令提示符，输入：
```bash
git clone https://github.com/awl2248/bilibili-subtitle-extractor.git
cd bilibili-subtitle-extractor
```

#### 方法 B：手动下载（不需要 Git）

1. 打开 https://github.com/awl2248/bilibili-subtitle-extractor
2. 点击绿色的 **"Code"** 按钮
3. 选择 **"Download ZIP"**
4. 解压下载的 ZIP 文件到你想要的位置
5. 打开文件夹

---

### **第 3 步：打开命令提示符**

1. 在项目文件夹中，按住 **Shift** + 右击空白处
2. 选择 **"在此处打开 PowerShell 窗口"** 或 **"在此处打开命令窗口"**

   或者：
3. 按 `Win + R`
4. 输入 `cmd`
5. 按 Enter
6. 输入项目路径，例如：
   ```bash
   cd C:\Users\你的用户名\Downloads\bilibili-subtitle-extractor
   ```

---

### **第 4 步：安装依赖包**

在命令提示符中输入以下命令：

```bash
pip install -r requirements.txt
```

**等待完成**（会显示一些下载进度信息）

这个命令会安装以下包：
- `yt-dlp` - 下载和提取视频信息
- `requests` - 网络请求
- `chardet` - 编码检测

---

### **第 5 步：安装 PyInstaller**

继续在命令提示符中输入：

```bash
pip install pyinstaller
```

这个工具会把你的 Python 程序转换成 .exe 文件。

---

### **第 6 步：一键打包**

在命令提示符中输入：

```bash
python build_exe.py
```

**等待打包完成**（可能需要 10-15 分钟）

你会看到类似这样的输出：
```
开始构建 .exe 文件...
... (一堆打包信息)
✅ 构建成功!
可执行文件位置: dist/B站字幕提取器.exe
```

---

### **第 7 步：完成！🎉**

打包完成后，你会在项目文件夹中看到一个 **`dist`** 文件夹。

打开 `dist` 文件夹，里面有 **`B站字幕提取器.exe`** 文件。

这就是你的可执行程序！

---

## 📌 如何使用生成的 .exe

### **简单使用**

1. 找到 `B站字幕提取器.exe` 文件
2. 双击打开
3. 程序会启动（可能需要几秒钟）
4. 开始使用！

### **分享给别人**

你可以直接把 `B站字幕提取器.exe` 发给别人，他们只需要：
- 双击即可运行
- **无需安装任何东西**
- **无需 Python 环境**

### **创建快捷方式**

1. 右击 `B站字幕提取器.exe`
2. 选择 **"发送到"** → **"桌面（创建快捷方式）"**
3. 快捷方式会出现在你的桌面上，更方便使用！

---

## 🐛 常见问题

### Q: 打包时显示错误 "找不到 PyInstaller"
**A:** 你可能没有成功安装 PyInstaller。重新运行：
```bash
pip install pyinstaller
```

### Q: 打包完成但 .exe 无法运行
**A:** 可能是以下原因：
1. 依赖包未完全安装 - 重新运行 `pip install -r requirements.txt`
2. Python 版本问题 - 确保使用 Python 3.8+
3. 重新打包一次

### Q: .exe 文件很大（200MB+），正常吗？
**A:** 正常！因为打包时把整个 Python 解释器和所有依赖都包含了。可以接受。

### Q: 打包后能删除 build 文件夹吗？
**A:** 可以。`build` 和 `bilibili-subtitle-extractor.spec` 都是临时文件，打包完成后可以删除，只需保留 `dist` 文件夹里的 .exe。

### Q: 能否进一步减小 .exe 文件大小？
**A:** 可以修改 `build_exe.py` 中的 PyInstaller 选项：
```python
'--onefile',      # 改为 False 会生成多个文件但总体更小
'--strip',        # 添加这行
'--noupx',        # 添加这行
```

但对于一般使用，200MB 左右的大小是可接受的。

---

## 🔄 更新程序后重新打包

如果你修改了代码或更新了程序，想重新生成 .exe：

1. 打开命令提示符
2. 进入项目文件夹
3. 运行：
   ```bash
   python build_exe.py
   ```
4. 新的 .exe 文件会覆盖 `dist/B站字幕提取器.exe`

**提示：** 旧的 `dist` 文件夹会被自动清理，保持干净。

---

## 📦 打包后的项目结构

打包完成后，项目文件夹看起来是这样的：

```
bilibili-subtitle-extractor/
├── dist/
│   └── B站字幕提取器.exe          ⭐ 你的可执行程序
├── build/                         (临时文件，可删除)
├── main.py
├── build_exe.py
├── requirements.txt
├── README.md
├── INSTALL.md
├── src/
│   ├── __init__.py
│   ├── bilibili_extractor.py
│   └── formatter.py
└── ...其他文件
```

---

## ✅ 打包成功的标志

- ✅ 命令提示符显示"构建成功!"
- ✅ 出现 `dist` 文件夹
- ✅ `dist` 文件夹中有 `B站字幕提取器.exe` 文件
- ✅ 双击 .exe 能打开程序窗口

---

## 🎯 下一步

1. **测试程序** - 试着粘贴一个 B 站视频链接，看看能否正常提取字幕
2. **分享给朋友** - 把 .exe 文件发给他们使用
3. **收集反馈** - 如果有问题，可以在 GitHub Issues 中反馈

---

## 📞 需要帮助？

如果遇到问题：

1. 检查本页面的"常见问题"部分
2. 查看 [README.md](README.md) 和 [INSTALL.md](INSTALL.md)
3. 在 GitHub 提交 Issue：https://github.com/awl2248/bilibili-subtitle-extractor/issues

---

## 🎉 完成了！

恭喜！你现在拥有了一个完整的、可以独立运行的 Windows 桌面程序！

现在你可以：
- 🎬 轻松提取 B 站视频字幕
- 📝 自动生成格式化文稿
- 📤 分享给其他人使用

祝你使用愉快！🚀
