def increment(num):
    try:
        return int(num)+1
    except:
        raise ValueError("this is not good Dipesh")
    
a = increment("87")
print(a)