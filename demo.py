import numpy as np 

a = np.array([1,2,3,4])
b = np.arange(24).reshape(8,3)
c = np.arange(10,34).reshape(8,3)
print(a.shape)
print(b+c)
print(b.shape , b.ndim)
print(np.exp(a))
print(f"sqrt of a : {np.sqrt(a)}")
print(f"min : {(b+c).min()}" )
print(f"max : {(b+c).max()}" )
print(f"sum : {(b+c).sum()}" )
print("type : " ,a.dtype)
d = b*c
print("d : \n" , d)
print("sum along each row : \n" , d.sum(axis=1))
print("cumulative sum along each row :  \n" , d.cumsum(axis=1))
print("Sine Operation : " , np.sin(a))
print("Matrix product : " , b@c.reshape(3,8))
print("array exponentiation : \n",c**3)

def f(x,y):
    return x+2*y


k = np.fromfunction(f,(5,4),dtype=np.int16)
print("k : \n" , k)
print("The fourth elements of index 2 to 4:\n",k[2:5,3])

print("Reversed k array : \n" , k[::-1])
print("Row reversed k array : \n" , k[:,::-1])

