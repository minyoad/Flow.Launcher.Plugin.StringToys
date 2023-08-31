# -*- coding: utf-8 -*-

import sys,os
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from flowlauncher import FlowLauncher

import importlib
import pyperclip 
import inspect

from plugin import *

PLUGIN_DIR='plugin'
PLUGIN_PREFIX='string_'

class StringToys(FlowLauncher):

    def load_plugins(self):
        plugins = []
        for filename in os.listdir(PLUGIN_DIR):
            if filename.startswith(PLUGIN_PREFIX) and filename.endswith('.py'):
                module_name = filename[:-3]
                module = importlib.import_module('{}.{}'.format(PLUGIN_DIR, module_name))
                for name in dir(module):
                    obj = getattr(module, name)
                    if inspect.isclass(obj) and issubclass(obj, BasePlugin) and obj != BasePlugin:
                        plugins.append(obj())
                    
        return plugins
    
                
    def query(self, query):
        
        if query is None or query.strip() == '':
            return []
        
        plugins = self.load_plugins()
        items=[]
        for plugin in plugins:
            subitems=plugin.get_results(query)
            if subitems is not None:
                for subitem in subitems:
                    items.append(subitem.to_dict())
                        
        return items     

    def context_menu(self, data):
        return []

    def copy_text(self, text):
        pyperclip.copy(text)
        

if __name__ == "__main__":
    StringToys()