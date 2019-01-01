# class Dog:
#     species ='mammal'
#     def __init__(self, name,age):
#         self.name = name
#         self.age= age


# philo = Dog('doggy',12)
# miko= Dog('doggg',23)

#  print ("dog one is {} and {} dog two is {} and {}.".format(philo.name,philo.age,miko.name,miko.age))  

# class Dog:
#     species ='mammal'
#     def __init__(self, name,age):
#         self.species= species

# philo = Dog('doggy',12)
# print("dog one is {}".format(philo.species))

# class Dog:
#     def highest_age(self,age):
#         self.age= age


 

# class Dog:
#     species ='mammal'
#     def __init__(self, name,age):
#         self.name = name
#         self.age= age


# philo = Dog('doggy',12)
# miko= Dog('doggg',23)
# piku =Dog('doy',33)

# def highest_age(*args):
#     return max(args)
# print("i am the heighest age {}.".format(highest_age(philo.age,miko.age,piku.age)))



# class Dog:
#     species ='mammal'
#     def __init__(self, name,age):
#         self.name = name
#         self.age= age


# philo = Dog('doggy',12)
# miko= Dog('doggg',23)
# piku =Dog('doy',33)

# if philo.species =='mammal':
#      print ('philo is mammal')


# class Dog:
#     def __init__(self, name):
#         self.name=name
#     def barks(self,bark):
#         return "{} says {}".format(self.name,bark)

# d=Dog('fido')
# make_sound = d.barks('wow wow')
# print (make_sound)
        

# class Course:
#     def __init__(self, name, ratings):
#         self.name=name
#         self.ratings=ratings
#     def average(self):
#         numberofratings=len(self.ratings)
#         average= sum(self.ratings)/numberofratings
#         print("average ratings for",self.name, "is",average)

# c1=Course('webDesign',[1,2,3,4,5])
# print c1.name
# print c1.ratings
# print c1.average()
# c2=Course('python',[5,5,5,5,5])
# print c2.name
# print c2.ratings


# class Programmer:
#     def setName(self,name):
#         self.name=name
#     def getName(self):
#         return self.name
# p1=programmer()
# p1.setName('vikas')
# print (p1.getName())


# class wheel:
#     def __init__(self, Numofwheels):
#         self.Numofwheels=Numofwheels
#         @property
#         def Numofwheels(self):
#             return self.Numofwheels
#         @Numofwheels.setter
#         def Numofwheels(self,Numofwheels):
#             self.Numofwheels=Numofwheels

# a1=wheel(12)
# a1.setNumofwheels(12)
# print(a1.getNumofwheels())

        