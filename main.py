#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
B站字幕提取器 - 主程序
一个简单易用的Windows图形界面工具，用于从B站视频自动提取字幕并生成格式化的Markdown文稿。
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import threading
import os
import sys
from pathlib import Path

from src.bilibili_extractor import BilibiliSubtitleExtractor
from src.formatter import SubtitleFormatter


class BilibiliSubtitleExtractorGUI:
    """B站字幕提取器GUI应用程序"""

    def __init__(self, root):
        self.root = root
        self.root.title("B站字幕提取器")
        self.root.geometry("800x700")
        self.root.resizable(True, True)
        
        # 设置风格
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        self.output_folder = str(Path.home() / "Downloads")
        self.is_extracting = False
        
        self.setup_ui()
        self.center_window()

    def center_window(self):
        """将窗口居中显示"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def setup_ui(self):
        """设置用户界面"""
        # 主框架
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(5, weight=1)

        # 标题
        title_label = ttk.Label(
            main_frame,
            text="B站字幕提取器",
            font=("SimHei", 18, "bold")
        )
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))

        # 输入URL
        ttk.Label(main_frame, text="B站视频网址:", font=("SimHei", 10)).grid(
            row=1, column=0, sticky=tk.W, pady=10
        )
        
        url_frame = ttk.Frame(main_frame)
        url_frame.grid(row=1, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        url_frame.columnconfigure(0, weight=1)
        
        self.url_entry = ttk.Entry(url_frame, width=50)
        self.url_entry.grid(row=0, column=0, sticky=(tk.W, tk.E))
        self.url_entry.insert(0, "https://www.bilibili.com/video/BV")
        
        paste_btn = ttk.Button(url_frame, text="粘贴", command=self.paste_url, width=5)
        paste_btn.grid(row=0, column=1, padx=(10, 0))

        # 字幕语言选择
        ttk.Label(main_frame, text="字幕语言:", font=("SimHei", 10)).grid(
            row=2, column=0, sticky=tk.W, pady=10
        )
        
        lang_frame = ttk.Frame(main_frame)
        lang_frame.grid(row=2, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        self.lang_var = tk.StringVar(value="zh")
        languages = [("中文", "zh"), ("English", "en"), ("自动检测", "auto")]
        
        for text, value in languages:
            ttk.Radiobutton(
                lang_frame,
                text=text,
                variable=self.lang_var,
                value=value
            ).pack(side=tk.LEFT, padx=10)

        # 输出格式选择
        ttk.Label(main_frame, text="输出格式:", font=("SimHei", 10)).grid(
            row=3, column=0, sticky=tk.W, pady=10
        )
        
        format_frame = ttk.Frame(main_frame)
        format_frame.grid(row=3, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        self.format_var = tk.StringVar(value="markdown")
        formats = [("Markdown (.md)", "markdown"), ("纯文本 (.txt)", "txt")]
        
        for text, value in formats:
            ttk.Radiobutton(
                format_frame,
                text=text,
                variable=self.format_var,
                value=value
            ).pack(side=tk.LEFT, padx=10)

        # 输出文件夹选择
        ttk.Label(main_frame, text="保存位置:", font=("SimHei", 10)).grid(
            row=4, column=0, sticky=tk.W, pady=10
        )
        
        folder_frame = ttk.Frame(main_frame)
        folder_frame.grid(row=4, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        folder_frame.columnconfigure(0, weight=1)
        
        self.folder_label = ttk.Label(
            folder_frame,
            text=self.output_folder,
            foreground="blue",
            font=("SimHei", 9)
        )
        self.folder_label.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        browse_btn = ttk.Button(
            folder_frame,
            text="浏览",
            command=self.browse_folder,
            width=8
        )
        browse_btn.grid(row=0, column=1, padx=(10, 0))

        # 进度和日志
        ttk.Label(main_frame, text="处理日志:", font=("SimHei", 10)).grid(
            row=5, column=0, sticky=(tk.W, tk.N), pady=(20, 0)
        )
        
        self.log_text = scrolledtext.ScrolledText(
            main_frame,
            height=8,
            width=70,
            font=("Courier", 9),
            state=tk.DISABLED
        )
        self.log_text.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(20, 20))

        # 进度条
        self.progress = ttk.Progressbar(
            main_frame,
            mode="indeterminate",
            length=400
        )
        self.progress.grid(row=6, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))

        # 按钮框架
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=7, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 0))
        button_frame.columnconfigure(0, weight=1)

        self.start_btn = ttk.Button(
            button_frame,
            text="开始提取",
            command=self.start_extraction,
            width=15
        )
        self.start_btn.pack(side=tk.LEFT, padx=5)

        self.stop_btn = ttk.Button(
            button_frame,
            text="停止",
            command=self.stop_extraction,
            width=15,
            state=tk.DISABLED
        )
        self.stop_btn.pack(side=tk.LEFT, padx=5)

        clear_btn = ttk.Button(
            button_frame,
            text="清空日志",
            command=self.clear_log,
            width=15
        )
        clear_btn.pack(side=tk.LEFT, padx=5)

        exit_btn = ttk.Button(
            button_frame,
            text="退出",
            command=self.root.quit,
            width=15
        )
        exit_btn.pack(side=tk.LEFT, padx=5)

    def paste_url(self):
        """从剪贴板粘贴URL"""
        try:
            clipboard_text = self.root.clipboard_get()
            self.url_entry.delete(0, tk.END)
            self.url_entry.insert(0, clipboard_text)
            self.add_log(f"✓ 已粘贴URL: {clipboard_text[:50]}...")
        except tk.TclError:
            messagebox.showerror("错误", "无法读取剪贴板")

    def browse_folder(self):
        """浏览文件夹"""
        folder = filedialog.askdirectory(title="选择输出文件夹", initialdir=self.output_folder)
        if folder:
            self.output_folder = folder
            self.folder_label.config(text=folder)
            self.add_log(f"✓ 输出文件夹已设置: {folder}")

    def add_log(self, message):
        """添加日志信息"""
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)
        self.root.update()

    def clear_log(self):
        """清空日志"""
        self.log_text.config(state=tk.NORMAL)
        self.log_text.delete(1.0, tk.END)
        self.log_text.config(state=tk.DISABLED)

    def start_extraction(self):
        """开始提取字幕"""
        url = self.url_entry.get().strip()
        
        if not url or "bilibili.com" not in url:
            messagebox.showerror("错误", "请输入有效的B站视频网址")
            return
        
        if not os.path.exists(self.output_folder):
            messagebox.showerror("错误", "输出文件夹不存在")
            return
        
        self.is_extracting = True
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.progress.start()
        self.clear_log()
        self.add_log("开始处理...")
        
        # 在新线程中运行提取
        thread = threading.Thread(
            target=self.extraction_worker,
            args=(url,),
            daemon=True
        )
        thread.start()

    def extraction_worker(self, url):
        """后台提取工作线程"""
        try:
            self.add_log(f"📥 正在下载视频信息: {url}")
            
            extractor = BilibiliSubtitleExtractor()
            video_info = extractor.extract_video_info(url)
            
            if not video_info:
                self.add_log("✗ 无法获取视频信息")
                return
            
            self.add_log(f"✓ 视频标题: {video_info.get('title', 'Unknown')}")
            self.add_log("📝 正在提取字幕...")
            
            language = self.lang_var.get()
            subtitle_data = extractor.get_subtitles(video_info, language)
            
            if not subtitle_data:
                self.add_log("✗ 无法获取字幕，可能视频没有字幕")
                return
            
            self.add_log(f"✓ 字幕提取成功，共 {len(subtitle_data)} 行")
            
            self.add_log("🎨 正在格式化内容...")
            formatter = SubtitleFormatter()
            formatted_content = formatter.format_subtitles(
                subtitle_data,
                video_info,
                output_format=self.format_var.get()
            )
            
            self.add_log("💾 正在保存文件...")
            output_file = self.save_output(
                video_info.get('title', 'video'),
                formatted_content
            )
            
            if output_file:
                self.add_log(f"✅ 成功! 文件已保存: {output_file}")
                messagebox.showinfo("成功", f"字幕已成功提取并保存到:\n{output_file}")
            
        except Exception as e:
            self.add_log(f"✗ 错误: {str(e)}")
            messagebox.showerror("错误", f"处理失败: {str(e)}")
        
        finally:
            self.is_extracting = False
            self.progress.stop()
            self.start_btn.config(state=tk.NORMAL)
            self.stop_btn.config(state=tk.DISABLED)
            self.add_log("\n处理完成")

    def save_output(self, title, content):
        """保存输出文件"""
        try:
            # 清理文件名
            clean_title = "".join(
                c for c in title
                if c.isalnum() or c in (' ', '-', '_', '（', '）')
            ).strip()
            
            format_ext = "md" if self.format_var.get() == "markdown" else "txt"
            filename = f"{clean_title}.{format_ext}"
            filepath = os.path.join(self.output_folder, filename)
            
            # 如果文件已存在，添加序号
            if os.path.exists(filepath):
                name, ext = os.path.splitext(filename)
                counter = 1
                while os.path.exists(os.path.join(self.output_folder, f"{name}_{counter}{ext}")):
                    counter += 1
                filepath = os.path.join(self.output_folder, f"{name}_{counter}{ext}")
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return filepath
        
        except Exception as e:
            self.add_log(f"✗ 保存文件失败: {str(e)}")
            return None

    def stop_extraction(self):
        """停止提取"""
        self.is_extracting = False
        self.progress.stop()
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.add_log("\n已停止处理")


def main():
    """主函数"""
    root = tk.Tk()
    app = BilibiliSubtitleExtractorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
