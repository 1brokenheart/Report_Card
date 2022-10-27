
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

#create a list with all the subjects 
subjects = ["physics", "calculus", "poetry", "history"]

#create a list with all the grades
grades = [98, 97, 85, 88]

#create a two dimensional list that combines subjects and grades.
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

print(gradebook)

gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

gradebook[5][1] = 98

gradebook[2].remove(85) 
gradebook[2].append("Pass") 

print(gradebook)

#create a new list that combines last semester gradebook with the current semester gradebook.
full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)
