#%%
import re

def get_result(x):
    if x.find('通过'):
        return 1
    return 0

def get_year_of_stay(x):
    for match in re.finditer('来新', x):
        s = match.start()
        e = match.end()
        laixin = x[s+1:e+4]
        cout = 0
        keys = ['一','二','三','四','五','六','七','八','九','十','十一','十二','十三','十四','十五']
        if re.findall(r'新(\d+)年', laixin):
            return re.findall(r'新(\d+)年', laixin)[0]
        elif re.findall(r'坡(\d+)年', laixin):
            return re.findall(r'坡(\d+)年', laixin)[0]
        elif re.findall(r'新(.+?)年', laixin):
            for key in keys:
                cout += 1
                if key in laixin: return cout 
        elif re.findall(r'坡(.+?)年', laixin):
            for key in keys:
                cout += 1
                if key in laixin: return cout 
    return 0

def is_local_uni(x):
    keys = ['nus','NUS','ntu','NTU','SMU','sm','SM','SIM','本地大学','公立大学','国立大学','南洋']
    for key in keys:
        if key in x:
            return 1
    return 0

def is_local_poly(x):
    keys = ['poly','本地大专']
    for key in keys:
        if key in x:
            return 1
    return 0

def is_diploma(x):
    keys = ['diploma','ite','Diploma']
    for key in keys:
        if key in x:
            return 1
    return 0

def is_bachelor(x):
    keys = ['本科','学士','bach','Bach','美本','澳洲本','美国本','欧本','大学Degree','大学学士']
    for key in keys:
        if key in x:
            return 1
    return 0

def is_master(x):
    keys = ['硕','msc','master','美硕','澳洲硕','美国硕','欧硕','欧洲小硕']
    for key in keys:
        if key in x:
            return 1
    return 0

def is_phd(x):
    keys = ['博','phd','PHD','美国博']
    for key in keys:
        if key in x:
            return 1
    return 0

def is_malaysian(x):
    keys = ['马来','马来西亚','malaysian']
    for key in keys:
        if key in x:
            return 1
    return 0 

def is_couple(x):
    keys = ['老公','老婆','丈夫','太太','结婚','husband','wife','全家']
    for key in keys:
        if key in x:
            return 1
    return 0

def with_child(x):
    keys = ['孩子','小孩','儿子','女儿','child','男孩','女孩','全家']
    for key in keys:
        if key in x:
            return 1
    return 0

def is_ep(x):
    keys = ['ep','EP']
    for key in keys:
        if key in x:
            return 1
    return 0

#%%
