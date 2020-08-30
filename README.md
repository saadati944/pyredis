# pyredis

a tiny app like redis.
this app stores key,value pairs in memory.
even you can save the pairs in the disk and reload them in the future.


## how to use ?
#### 1. direct use :
1. place pyredis.py file beside your source.
1. add `import pyredis` to top of your source code.
1. use any of these commands you need :

```
pyredis.set(key ,value)
pyredis.get(key)
pyredis.remove(key)
pyredis.have(key)
pyredis.count()
pyredis.save(path)
pyredis.load(path)
```
#### 2. using http request :


## pyredis commands
1. set(key ,value)
1. get(key)
1. remove(key)
1. have(key)
1. count()
1. save(path)
1. load(path)

Hints :
* path argument is optional for save and load functions.
* the default path for save and load functions is `pyredis.data`.
* you need pickle to use save and load functions.
* just set again a key to update it.
* get returns nullvalue if key was not setted before.
* you can change nullvalue by calling `pyredis.nullvalue = <your value>`.
* default nullvalue is '' (an empty string).


