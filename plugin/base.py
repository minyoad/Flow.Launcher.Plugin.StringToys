
class Result(object):
    
    def __init__(self,title,subtitle,value, method=None):
        self.title=title
        self.subtitle=subtitle
        self.value=value
        self.method=method
    
    def to_dict(self):
        
        json_rpc_action = {
            "method": "copy_text",
            "parameters": [self.value]
        }
        if self.method is not None:
            json_rpc_action = {
                "method": "run_plugin_method",
                "parameters": [self.value, self.method]
            }
            
        return {
            "Title": self.title,
            "SubTitle": self.subtitle,
            "IcoPath": "Images/app.png",
            "JsonRPCAction": json_rpc_action
        }
class BasePlugin:
    
    def __init__(self):
        self._result_map = {}
        
    def get_results(self,query):
        
        return []
    
    def run_method(self, query, method_name):
        if method_name in self._result_map:
            self._result_map[method_name](query)