from threading import Thread

a = lambda :print('Hello')
b = lambda x:print(x)
t1 = Thread(target=a)
t2 = Thread(target=b, args=(1,))

t1.run()
import pdb;pdb.set_trace()
print(t1.get_ident())
t2.run()