keys=[]
values=[]
nullvalue=''

def set(key,value):
    global keys,values
    try:
        i=keys.index(key)
        values[i]=value
        return 1
    except:
        try:
            keys.append(key)
            values.append(value)
            return 1
        except:
            return 0
    return 0

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
        return 1
    except:
        return 0

def main():
    print('pyredis v0.0')
    set('k','v')
    print(get('k'))
    set('k2','v2')
    print(get('k2'))
    set('k','v3')
    print(get('k'))
    print(remove('k'))
    print(get('k'))
    print(remove('k'))
    print(remove('k2'))

if __name__=='__main__':
    main()
