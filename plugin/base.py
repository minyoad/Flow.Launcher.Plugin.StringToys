
class Result(object):
    
    def __init__(self,title,subtitle,value):
        self.title=title
        self.subtitle=subtitle
        self.value=value
    
    def to_dict(self):
        return {
            "Title": self.title,
            "SubTitle": self.subtitle,
            "IcoPath": "Images/app.png",
            "JsonRPCAction": {
                "method": "copy_text",
                "parameters": [self.value]
            }
        }
     

class BasePlugin:
    
    def get_results(self,query):
        
        return []        


            