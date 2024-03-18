from base import BasePlugin,Result

class StringPath(BasePlugin):   
    
    def get_results(self,query):
        
        #check if query contains / ,then converto to hex string
        items=[]                                  
            
        if '/' in query:
            bs=query.encode()
            target=' '.join(['0x%02X' % b for b in bs])
            items.append(Result("转换普通字符串为hex字符串","转换成：{}".format(target),target))         
        
        if '0x' in query:
            target=bytes.fromhex(query.replace('0x','')).decode()
            items.append(Result("hex字符串转换成普通字符串","转换成：{}".format(target),target))
                    
        return items