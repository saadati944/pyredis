keys=[]
values=[]

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

def main():
    print('pyredis v0.0')
    set('k','v')
    print(keys,values)
    set('k2','v2')
    print(keys,values)
    set('k','v3')
    print(keys,values)

if __name__=='__main__':
    main()
