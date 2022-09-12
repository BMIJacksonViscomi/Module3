#Problem 1
#using .copy() to make sure no answers are overwritten

#1a
One_a = list(range(0,10)) #range to go from 0 - 9 (10 chars)
#print(One_a)

#1b
One_b = One_a.copy() 
One_b[5] = One_b[5] + 3 #using list index and then adding 3 to str
#print(One_b)

#1c
One_c = One_b.copy()
One_c = [float(x) for x in One_c] #using list comprehension to convert all values to floats
#print(One_c)

#1d
One_d = One_c.copy()
One_d = set(One_d) #Coerce to set
#print(One_d)

#1e
One_e = One_d.copy()
One_e.add(10.0) #adding 10.0 to end of set
#print(One_e)

#1f
One_f = One_e.copy()
One_f.pop() #popping random element from set
#print(One_f)

#1g
One_g = len(One_f) #len function to get number of items
#print(One_g)

#1h
One_h = (len(One_c) == One_g) #1c was last list variable. Using bool to evaluate if both lengths are equal
#print(One_h)

#1i
One_i = One_f.copy()
One_i = list(One_i) #Coerce back to list
One_i = One_i + One_a #appending lists together
#print(One_i)

#1j
One_j = One_i.copy() 
One_j = set(One_j) #Coerce back to set
#print(One_j)

#1k
One_k = len(One_j) #Setting 1k as length of previous set
#print(One_k)

#for testing answers

print(One_a)
print(One_b)
print(One_c)
print(One_d)
print(One_e)
print(One_f)
print(One_g)
print(One_h)
print(One_i)
print(One_j)
print(One_k)



#Problem 2

#Prep dictionaries
two_patient_dictionary_kinoko = {
  "name" : "Kinoko",
  "year" : 2021
}
two_patient_dictionary_dango = {
  "name" : "Dango",
  "year" : 2019
}
two_patient_dictionary_mochi  = {
  "name" : "Mochi",
  "year" : 2020
}


#2a
#manually create nested dictionary with flat dict names  
two_a = {
  "two_patient_dictionary_kinoko" : two_patient_dictionary_kinoko,
  "two_patient_dictionary_dango" : two_patient_dictionary_dango,
  "two_patient_dictionary_mochi" : two_patient_dictionary_mochi
}
#print(two_a)

#2b
two_b = two_a["two_patient_dictionary_dango"]["name"] #extract Dango's name using nested keys
#print(two_b)

#2c
two_a["two_patient_dictionary_mochi"]["year"] = 2018 #changing year using nested keys
#print(two_a)

#2d
two_d = { #manually creating flat dict using name as key
  "Kinoko": 2021,
  "Dango": 2019,
  "Mochi": 2019
}
#print(two_d)

#2e
two_e = list(two_d.keys()) #creating list of flat dict keys
#print(two_e)

#2f
two_f = list(two_d.values()) #creating list of flat dict values
#print(two_f)

#2g
two_g = dict(zip(two_e, two_f)) #creating a dictionary by zipping keys and values together
#print(two_g)

#test answers

print(two_a)
print(two_b)
#2c just updates 2a
print(two_d)
print(two_e)
print(two_f)
print(two_g)


#Problem 3

#Prep
three_setA = {1,2,3,4,5}
three_setB = {2,3,4,5,6}
three_setC = {3,5,7,9}
three_setD = {2,4,6,8}
three_setE = {1,2,3,4}

#3a
three_a = three_setE.issubset(three_setA) #checking is E is subset of A
#print(three_a)

#3b
#check if E is subset of A, but E doesn't equal A 
three_b = (three_setE.issubset(three_setA)) & (three_setE != three_setA)
#print(three_b)

#3c
#finding insection of A and B
three_c = three_setA.intersection(three_setB)
#print(three_c)

#3d creating union of C, D, E
three_d = three_setC.union(three_setD,three_setE)
#print(three_d)

#3e
three_d.add(9) #add 9 to end of union
three_e = three_d 
#print(three_e) #doesn't change since 9 already exists

#3f
three_f = (three_e == One_a) #setting f to bool checking if e = a
#print(three_f)

#3g
#they are not the same because One_a has a '0' at the begging and is a list (as opposed to a set)
#to make it True..
three_g = three_e.copy()
three_g = list(three_g) #change to list
three_g.insert(0,0) #insert 0 at position 0
three_g == One_a #test

#checking answers

print(three_a)
print(three_b)
print(three_c)
print(three_d)
print(three_e)
print(three_f)
print(three_g == One_a )

#Problem 4

#using .copy() to not overwrite answers

#4a
four_a = int(8) #setting 8 to int
#print(four_a)

#4b
four_b = list() #creating empty list
#print(four_b)

#4c
four_c = four_b.copy() 
four_c.append(type(four_a)) #appending type of 4a to list
#print(four_c)

#4d
four_d = four_c.copy()
four_d.append(0.39) #appending 0.39 to list
#print(four_d)

#4e
four_e = four_d.copy()
four_e.append(type(four_e[1])) #appending type of 0.39 to list using list index
#print(four_e)

#4f
four_f = four_e.copy()
four_f.append(round(.038**-10)) ##using ** for exponentials, round() to get rid of decimals
#print(four_f)

#4g
four_g = four_f.copy()
four_g.append(type(four_g[3])) #appending type using index, will be int since no decimals
#print(four_g)

#test answers
 
print(four_a)
print(four_b)
print(four_c)
print(four_d)
print(four_e)
print(four_f)
print(four_g)


#Problem 5

#5a
#manually create table
five_a = {
    0 : type(8),
    1 : 0.39,
    2 : type(0.39),
    3 : 159281022082815,
    4 : type(159281022082815)
}
#print(five_a)

#5b
five_b = four_g.copy()
five_b.append(300) #append 300 to list
five_b[5] = str(300) #using index chagne 300 to string
#print(five_b)

#5c
five_c = five_b.copy()
five_c.append(type(five_b[5])) #appending type of 5b using list index
#print(five_c)

#5d
five_d = five_c.copy()
five_d = five_d[5][0:2] #slicing 300 using list index and string index
#print(five_d)

#5e
five_e = five_c.copy()
five_e.append(type(five_d)) #appending type of sliced int (now a string)
#print(five_e)

#5f
five_f = five_d
five_f = [int(x) for x in five_f] #using list comprehension to cast all values as int
#print(five_f)

#5g
five_g = five_f.copy()
five_g.append(type(five_g)) #appending the type of list to the list
#print(five_g)

#5h
five_h = five_e.copy() #copyig the last iteration of P4 list
five_h.append(type(three_setA)) #appending hte type of three_setA set to end of list
#print(five_h)

#test answers
print(five_a)
print(five_b)
print(five_c)
print(five_d)
print(five_e)
print(five_f)
print(five_g)
print(five_h)


