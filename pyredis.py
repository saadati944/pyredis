keys=[]
values=[]
nullvalue=''

def set(key,value):
    global keys,values
    try:
        i=keys.index(key)
        values[i]=value
        return True
    except:
        try:
            keys.append(key)
            values.append(value)
            return True
        except:
            return False
    return False

def get(key):
    global keys,values
    try:
        i=keys.index(key)
        return values[i]
    except:
        return nullvalue
def remove(key):
    global keys,values
    try:
        i=keys.index(key)
        keys.pop(i)
        values.pop(i)
        return True
    except:
        return False

def have(key):
    global keys
    try:
        keys.index(key)
        return True
    except:
        return False

def count():
    global keys
    return len(keys)

def save(path='pyredis.data'):
    global keys,values
    import pickle
    try:
        f=open(path,'wb')
        pickle.dump((keys,values),f)
        f.close()
        return True
    except:
        return False

def load(path='pyredis.data'):
    global keys,values
    import pickle
    try:
        f=open(path,'rb')
        keys,values=pickle.load(f)
        f.close()
        return True
    except:
        return False


def main():
    print('pyredis v0.0')
    set('k','v')
    print(get('k'))
    set('k2','v2')
    print(get('k2'))
    set('k','v3')
    print(count())
    print(get('k'))
    print(remove('k'))
    print(get('k'))
    print(remove('k'))
    print(remove('k2'))
    print(count())

if __name__=='__main__':
    main()
