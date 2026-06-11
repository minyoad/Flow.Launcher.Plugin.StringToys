from .base import BasePlugin,Result
import subprocess

class StringPlayer(BasePlugin): 
    def __init__(self,settings):
        super().__init__()
        self.settings = settings
        self._register_methods()
    
    def _register_methods(self):
        self._result_map['play_video_with_vlc'] = self.play_video_with_vlc
        self._result_map['play_video_with_ffplay'] = self.play_video_with_ffplay

    def play_video_with_vlc(self,query):
        #use vlc to play video
        #find vlc path, C:\Program Files\VideoLAN\VLC\vlc.exe
        vlc_path = self.settings.get('vlc_path', "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe")
        #use vlc to play video
        subprocess.Popen([vlc_path,query])

    def play_video_with_ffplay(self,query):
        #use ffplay to play video
        #find ffplay path
        ffplay_path = self.settings.get('ffplay_path', "D:\\Tools\\ffmpeg\\bin\\ffplay.exe")
        #use ffplay to play video
        subprocess.Popen([ffplay_path,query])
    
    def get_results(self,query):
        
        #check if query contains start with http or https or rtsp or rtmp
        items=[]     

        if query.startswith('http') or query.startswith('rtsp') or query.startswith('rtmp') or query.endswith('.mp4') or query.endswith('.mkv') or query.endswith('.avi') or query.endswith('.m3u8'):
            items.append(Result("使用ffplay播放视频","播放：{}".format(query),query, "play_video_with_ffplay"))
            items.append(Result("使用vlc播放视频","播放：{}".format(query),query, "play_video_with_vlc"))           
                    
        return items