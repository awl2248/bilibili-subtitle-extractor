#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
B站字幕提取器核心模块
负责从B站视频下载和提取字幕
"""

import json
import re
import requests
from typing import Dict, List, Optional, Tuple
import yt_dlp


class BilibiliSubtitleExtractor:
    """B站字幕提取器"""

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

    def extract_video_id(self, url: str) -> Optional[str]:
        """从URL提取视频ID"""
        # 支持多种URL格式
        patterns = [
            r'bilibili\.com/video/(BV\w+)',  # BV号
            r'bilibili\.com/video/(av\d+)',   # av号
            r'bilibili\.com/video/(\d+)',     # 数字ID
        ]
        
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        
        return None

    def extract_video_info(self, url: str) -> Optional[Dict]:
        """使用yt-dlp提取视频信息"""
        try:
            ydl_opts = {
                'quiet': True,
                'no_warnings': True,
                'extract_flat': False,
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                
                video_info = {
                    'title': info.get('title', 'Unknown'),
                    'video_id': info.get('id', ''),
                    'duration': info.get('duration', 0),
                    'upload_date': info.get('upload_date', ''),
                    'subtitles': info.get('subtitles', {}),
                    'automatic_captions': info.get('automatic_captions', {}),
                }
                
                return video_info
        
        except Exception as e:
            print(f"Error extracting video info: {e}")
            return None

    def get_subtitles(self, video_info: Dict, language: str = 'auto') -> Optional[List[str]]:
        """获取字幕内容"""
        try:
            subtitles = video_info.get('subtitles', {})
            auto_captions = video_info.get('automatic_captions', {})
            
            # 选择字幕语言
            selected_subtitle = None
            
            if language == 'auto':
                # 优先顺序：中文 > 英文 > 其他
                for lang_code in ['zh-Hans', 'zh-Hant', 'zh', 'en', 'en-US']:
                    if lang_code in subtitles:
                        selected_subtitle = subtitles[lang_code]
                        break
                    if lang_code in auto_captions:
                        selected_subtitle = auto_captions[lang_code]
                        break
                
                # 如果没找到，取第一个可用的
                if not selected_subtitle:
                    if subtitles:
                        selected_subtitle = next(iter(subtitles.values()))
                    elif auto_captions:
                        selected_subtitle = next(iter(auto_captions.values()))
            else:
                # 特定语言
                if language in subtitles:
                    selected_subtitle = subtitles[language]
                elif language in auto_captions:
                    selected_subtitle = auto_captions[language]
            
            if not selected_subtitle:
                return None
            
            # 提取字幕文本
            subtitle_texts = []
            for item in selected_subtitle:
                if isinstance(item, dict):
                    text = item.get('text', '')
                    if text and text.strip():
                        subtitle_texts.append(text.strip())
            
            return subtitle_texts if subtitle_texts else None
        
        except Exception as e:
            print(f"Error getting subtitles: {e}")
            return None

    def parse_srt_file(self, content: str) -> List[Dict]:
        """解析SRT字幕文件"""
        try:
            subtitles = []
            entries = content.strip().split('\n\n')
            
            for entry in entries:
                lines = entry.strip().split('\n')
                if len(lines) < 3:
                    continue
                
                try:
                    # 提取索引、时间和文本
                    index = int(lines[0])
                    time_range = lines[1]
                    text = ' '.join(lines[2:])
                    
                    # 解析时间
                    match = re.match(r'(\d{2}:\d{2}:\d{2}[,.]\d{3}) --> (\d{2}:\d{2}:\d{2}[,.]\d{3})', time_range)
                    if match:
                        start_time = match.group(1).replace(',', '.')
                        end_time = match.group(2).replace(',', '.')
                        
                        subtitles.append({
                            'index': index,
                            'start': start_time,
                            'end': end_time,
                            'text': text.strip()
                        })
                except (ValueError, IndexError):
                    continue
            
            return subtitles
        
        except Exception as e:
            print(f"Error parsing SRT: {e}")
            return []
