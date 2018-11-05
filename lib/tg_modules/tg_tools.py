#released under:
#Attribution-NonCommercial 3.0 United States (CC BY-NC 3.0 US)
#Author: Jonah Yolles-Murphy on Date: 10/12/18

from tg_modules.cp_cpython_add_backs import delattr

def get_direction(val):
    if val < 0:
        return -1
    elif val > 0:
        return 1
    else:
        return 0

def del_dict_value(dikt,target):
    for i in dikt:
        if dikt[i] == target:
            del dikt[i]
    return

def get_key(dikt, target):
    for i in dikt:
        if dikt[i] == target:
            return i
    raise KeyError()

class holder():
    def __init__(self):
        self.contents = []
        self.key_dict = {}
        self.cur_iter = 0

    def __iter__(self):
        self._iter_count = 0
        return self 
    
    def __next__(self):
        if self._iter_count == len(self.contents):
            raise StopIteration
        else:
            self._iter_count += 1
            return self.contents[self._iter_count - 1]
            
        
    
    def add(self,name,obj):
        setattr(self,name,obj)
        self.contents.append(getattr(self,name))
        self.key_dict[str(obj)] = name
        #print(self.contents)
    
    def delete(self,name):
        self.contents.pop(self.contents.index(getattr(self,name)))
        delattr(self,name)
        
    def get(self,target):
        if type(target) == str:
            return getattr(self,target)
        else:
            #try:
            return self.key_dict[str(target)]
            #except:
            #    return
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.cur_iter == len(self.contents):
            self.cur_iter = 0
            raise StopIteration
        else:
            self.cur_iter += 1
            return self.contents[self.cur_iter-1]