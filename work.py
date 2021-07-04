#classes

#class MyNewClass():
#    '''my new class, doc string'''

#    pass

#x = MyNewClass()
#print(x.__doc__)


class MyNewClass():
    '''my new class, doc string'''
    b = 30
    def __init__(self):
        a = 10
        print(a)
        print(self.b)
        self.b = 15

    def hello(self, v):
        print(v)
        print(self.b)
        
'''
y = MyNewClass()
print(y.b)
print(MyNewClass.b)
print(y.b)
'''
'''
z = MyNewClass()
z.hello(2)
z.b = 90
z.hello(3)
'''

#inheritance

#single inheritance
class H(MyNewClass):
    def __init__(self):
        print(self.b)
        
    def hello(self, v):
        print(v+1)
        print(self.b+1)
        return super().hello(v)
'''
x = H()
x.hello(55)
'''
#multilevel inheritance

class Multi(H):
    def __init__(self):
        print(self.b)
'''
y = Multi()
'''
#multiple inheritance
class Ref():
    k = 33
    pass


class Multiple(MyNewClass, Ref):
    def __init__(self):
        print(self.b)
'''        print(self.k)
m = Multiple()
'''
#hierarchical inheritance
class Hierar(Ref):
    pass


class NHier(Ref):
    pass

#hybrid inheritance
class A:
    d = 56

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

z = D()
print(z.d)
        



#eg:
class ClassRoom():
    class_name = 10
    class_teacher = "sam"
    is_digital = True

class Student1(ClassRoom):
    student_name = "alex"
    student_id = 202

class Student2(ClassRoom):
    student_name = "alok"
    student_id = 101   


l1 = Student1()

print(l1.class_name)























































          
          



















    
    
    
