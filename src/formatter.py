#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
字幕格式化模块
负责将提取的字幕格式化为Markdown或纯文本
"""

from typing import List, Dict, Optional
from datetime import datetime
import re


class SubtitleFormatter:
    """字幕格式化器"""

    def __init__(self):
        pass

    def split_into_sections(self, texts: List[str], section_length: int = 3) -> List[List[str]]:
        """按自然段落将文本分节
        
        Args:
            texts: 字幕文本列表
            section_length: 每节包含的字幕行数（默认3行为一章节）
        
        Returns:
            分节后的文本列表
        """
        sections = []
        for i in range(0, len(texts), section_length):
            section = texts[i:i + section_length]
            sections.append(section)
        return sections

    def clean_text(self, text: str) -> str:
        """清理文本
        
        Args:
            text: 原始文本
        
        Returns:
            清理后的文本
        """
        # 移除时间戳格式 [HH:MM:SS]
        text = re.sub(r'\[\d{2}:\d{2}:\d{2}\]', '', text)
        
        # 移除多余的空格
        text = re.sub(r'\s+', ' ', text)
        
        # 移除特殊符号但保留标点
        text = text.strip()
        
        return text

    def merge_sections(self, sections: List[List[str]]) -> List[str]:
        """将每节的文本合并为单个字符串
        
        Args:
            sections: 分节的文本列表
        
        Returns:
            合并后的章节列表
        """
        merged = []
        for section in sections:
            # 连接该节的所有行，用空格分隔
            combined = ' '.join([self.clean_text(text) for text in section])
            if combined.strip():
                merged.append(combined)
        return merged

    def format_as_markdown(self, sections: List[str], video_info: Dict) -> str:
        """格式化为Markdown格式
        
        Args:
            sections: 章节文本列表
            video_info: 视频信息字典
        
        Returns:
            格式化后的Markdown文本
        """
        title = video_info.get('title', 'Untitled')
        upload_date = video_info.get('upload_date', '')
        duration = video_info.get('duration', 0)
        
        # 格式化日期
        if upload_date:
            try:
                date_obj = datetime.strptime(upload_date, '%Y%m%d')
                upload_date = date_obj.strftime('%Y-%m-%d')
            except:
                pass
        
        # 格式化时长
        duration_str = self._format_duration(duration)
        
        # 构建Markdown内容
        md_content = []
        md_content.append(f"# {title}\n")
        md_content.append("---\n")
        
        # 视频信息
        if upload_date:
            md_content.append(f"**发布日期:** {upload_date}\n")
        if duration:
            md_content.append(f"**视频时长:** {duration_str}\n")
        
        md_content.append("---\n\n")
        md_content.append("## 文字稿\n\n")
        
        # 添加章节
        for i, section in enumerate(sections, 1):
            md_content.append(f"### 第 {i} 部分\n\n")
            md_content.append(f"{section}\n\n")
        
        # 页脚
        md_content.append("---\n")
        md_content.append(f"*本文字稿由 B站字幕提取器 自动生成*\n")
        
        return ''.join(md_content)

    def format_as_txt(self, sections: List[str], video_info: Dict) -> str:
        """格式化为纯文本格式
        
        Args:
            sections: 章节文本列表
            video_info: 视频信息字典
        
        Returns:
            格式化后的纯文本
        """
        title = video_info.get('title', 'Untitled')
        upload_date = video_info.get('upload_date', '')
        duration = video_info.get('duration', 0)
        
        # 格式化日期
        if upload_date:
            try:
                date_obj = datetime.strptime(upload_date, '%Y%m%d')
                upload_date = date_obj.strftime('%Y-%m-%d')
            except:
                pass
        
        # 格式化时长
        duration_str = self._format_duration(duration)
        
        # 构建纯文本内容
        txt_content = []
        txt_content.append(f"{title}\n")
        txt_content.append("=" * len(title) + "\n\n")
        
        # 视频信息
        if upload_date:
            txt_content.append(f"发布日期: {upload_date}\n")
        if duration:
            txt_content.append(f"视频时长: {duration_str}\n")
        
        txt_content.append("\n" + "-" * 50 + "\n\n")
        txt_content.append("文字稿\n\n")
        
        # 添加章节
        for i, section in enumerate(sections, 1):
            txt_content.append(f"【第 {i} 部分】\n\n")
            txt_content.append(f"{section}\n\n")
        
        # 页脚
        txt_content.append("-" * 50 + "\n")
        txt_content.append("本文字稿由 B站字幕提取器 自动生成\n")
        
        return ''.join(txt_content)

    def format_subtitles(self, subtitle_texts: List[str], video_info: Dict, 
                        output_format: str = 'markdown') -> str:
        """主格式化函数
        
        Args:
            subtitle_texts: 字幕文本列表
            video_info: 视频信息
            output_format: 输出格式 ('markdown' 或 'txt')
        
        Returns:
            格式化后的文本
        """
        # 分节
        sections = self.split_into_sections(subtitle_texts, section_length=3)
        
        # 合并文本
        merged_sections = self.merge_sections(sections)
        
        # 选择格式
        if output_format == 'markdown':
            return self.format_as_markdown(merged_sections, video_info)
        else:
            return self.format_as_txt(merged_sections, video_info)

    @staticmethod
    def _format_duration(seconds: int) -> str:
        """将秒数格式化为 HH:MM:SS
        
        Args:
            seconds: 秒数
        
        Returns:
            格式化后的时间字符串
        """
        if not seconds:
            return "未知"
        
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        secs = seconds % 60
        
        if hours > 0:
            return f"{hours}小时{minutes}分钟{secs}秒"
        elif minutes > 0:
            return f"{minutes}分钟{secs}秒"
        else:
            return f"{secs}秒"
