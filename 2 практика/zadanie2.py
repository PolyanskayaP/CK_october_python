#x = xо +v*t + (a*(t*t))/2
def func(t, x0, v=5, a=2):
    x = x0 +v*t + (a*(t*t))/2   
    return x

print(func(10,0))
print(func(10,0,3))
print(func(10,0,3,1))
