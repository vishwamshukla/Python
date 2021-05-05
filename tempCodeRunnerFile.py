class A:    
#     #Parent class or Super class
    
#     def __init__(self):   #Constructors
#         print("In A init")
    
#     def feature1(self):
#         print("Feature 1-A is working")
#     def feature2(self):
#         print("Feature 2 is working")
#  #Single level        
# class B:            #Child class or Sub class
    
#     def __init__(self):
#         print("In B init")
#     def feature3(self):
#         print("Feature 3 is working")
#     def feature4(self):
#         print("Feature 4 is working")
# #MRO(Method resolution order)  
# class C(A,B):
#     def __init__(self):
#         super().__init__()  #will call init of A class first(goes from left to right C->A->B)
#         print("In C init")
#     def feat(self):
#         super().feature2()
# a1 = C()
# a1.feat()
