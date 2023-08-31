
import re
from base import BasePlugin,Result

class StringPath(BasePlugin):   
    
    def get_results(self,query):
        
        #check if query contains / ,then converto to \\
        items=[]                                  
            
        if '/' in query:
            items.append(Result("转换路径从 // 到 \\\\","转换成：{}".format(query.replace('/','\\')),query.replace('/','\\')))
        
        if '\\' in query:
            items.append(Result("转换路径从 \\\\ 到 //","转换成：{}".format(query.replace('\\','/')),query.replace('\\','/')))
                    
        return items
        
            