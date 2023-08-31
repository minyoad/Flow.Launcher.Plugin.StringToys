from base import BasePlugin,Result

import base64

class StringPath(BasePlugin):  
    
    def is_base64(self,text):
        try:
            base64.b64decode(text)
            return True
        except:
            return False
         
    
    def get_results(self,query):
        
        #check if query contains / ,then converto to \\
        items=[]                                  
            
        if self.is_base64(query):
            decoded_str = base64.b64decode(query).decode()
            items.append(Result("Base64解码","解码后：{}".format(decoded_str),decoded_str))        
        else: 
            encoded_str = base64.b64encode(query.encode()).decode()       
            items.append(Result("用Base64编码","编码后：{}".format(encoded_str),encoded_str))
                    
        return items