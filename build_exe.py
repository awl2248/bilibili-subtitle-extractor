#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
将Python项目打包为Windows .exe可执行文件
使用 PyInstaller

用法:
    pip install pyinstaller
    python build_exe.py
"""

import os
import subprocess
import shutil
import sys

def build_exe():
    """构建exe文件"""
    
    # 检查PyInstaller
    try:
        import PyInstaller
    except ImportError:
        print("请先安装 PyInstaller:")
        print("pip install pyinstaller")
        return False
    
    # 清理旧的构建文件
    if os.path.exists('dist'):
        shutil.rmtree('dist')
    if os.path.exists('build'):
        shutil.rmtree('build')
    if os.path.exists('main.spec'):
        os.remove('main.spec')
    
    print("开始构建 .exe 文件...")
    
    # PyInstaller 命令
    cmd = [
        'pyinstaller',
        '--onefile',  # 单个文件
        '--windowed',  # 无控制台窗口
        '--name', 'B站字幕提取器',  # 程序名称
        '--icon', 'icon.ico' if os.path.exists('icon.ico') else None,  # 图标
        '--add-data', f'src{os.pathsep}src',  # 添加数据文件
        'main.py'
    ]
    
    # 移除None值
    cmd = [x for x in cmd if x is not None]
    
    try:
        result = subprocess.run(cmd, check=True)
        print("\n✅ 构建成功!")
        print(f"可执行文件位置: dist/B站字幕提取器.exe")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n✗ 构建失败: {e}")
        return False

if __name__ == '__main__':
    success = build_exe()
    sys.exit(0 if success else 1)
