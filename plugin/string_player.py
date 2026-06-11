from .base import BasePlugin,Result
import subprocess
import shutil
import os

class StringPlayer(BasePlugin): 
    def __init__(self,settings):
        super().__init__()
        self.settings = settings
        self._register_methods()
        self.vlc_path = self._find_executable('vlc.exe', 'vlc_path', "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe")
        self.ffplay_path = self._find_executable('ffplay.exe', 'ffplay_path', "D:\\Tools\\ffmpeg\\bin\\ffplay.exe")

    def _find_executable(self, name, settings_key, default_path):
        # 1. Check settings from plugin.json
        path_from_settings = self.settings.get(settings_key)
        if path_from_settings and os.path.exists(path_from_settings):
            return path_from_settings

        # 2. Check system PATH
        path_from_env = shutil.which(name)
        if path_from_env:
            return path_from_env

        # 3. Check hardcoded default path
        if os.path.exists(default_path):
            return default_path
            
        # 4. Check the other default path for VLC (Program Files (x86))
        if name == 'vlc.exe':
            x86_default_path = "C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"
            if os.path.exists(x86_default_path):
                return x86_default_path

        return None
    
    def _register_methods(self):
        self._result_map['play_video_with_vlc'] = self.play_video_with_vlc
        self._result_map['play_video_with_ffplay'] = self.play_video_with_ffplay

    def play_video_with_vlc(self,query):
        if self.vlc_path:
            subprocess.Popen([self.vlc_path,query])

    def play_video_with_ffplay(self,query):
        if self.ffplay_path:
            subprocess.Popen([self.ffplay_path,query])
    
    def get_results(self,query):
        items=[]     
        is_video_link = query.startswith(('http', 'rtsp', 'rtmp')) or query.endswith(('.mp4', '.mkv', '.avi', '.m3u8'))

        if is_video_link:
            if self.ffplay_path:
                items.append(Result("使用ffplay播放视频","播放：{}".format(query),query, "play_video_with_ffplay"))
            if self.vlc_path:
                items.append(Result("使用vlc播放视频","播放：{}".format(query),query, "play_video_with_vlc"))           
                    
        return items