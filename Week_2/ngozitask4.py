# #1
quote= input("enter favourite quote :")
quotes = quote.title()
print(f"Ngozi once said \"{quotes}\"")

2
empty_list = []
items = input("Enter 1st shoping items :")
empty_list.append(items)
items = input("Enter 2nd shoping items :")
empty_list.append(items)
items = input("Enter 3rd shoping items :")
empty_list.append(items)
print(empty_list)

#3
sentence = input("Enter your sentence")
print(len(sentence.split()))

#4
username = input("Enter 5 names seperated by spaces").split()
names = [name.lower() for name in username]
print(*names , sep = "\n")

#5
student_names = []
student_scores = []
studentone_name = input("enter 1st student name")
studentone_score = input("enter 1st student score")
student_names.append(studentone_name)
student_scores.append(studentone_score)
studenttwo_name = input("enter 2nd student name")
studenttwo_score = input("enter 2nd student score")
student_names.append(studenttwo_name)
student_scores.append(studenttwo_score)
studentthree_name = input("enter 3rd student name")
studentthree_score = input("enter 3rd student score")
student_names.append(studentthree_name)
student_scores.append(studentthree_score)
print(f"Student\t Scores\n{student_names[0]}\t{student_scores[0]}\n{student_names[1]}\t{student_scores[1]}\n{student_names[2]}\t{student_scores[2]}")

#6
word = input("Enter your words: ")
print(f"the word entered is: {len(word)}")
print(word.isupper())
print(word.islower())
print(word.istitle())

#7
city_list = ["asaba","oshogbo","akoda-ede", "ikirun","ajegunle"]
city_list[3]= "miami"
city_list.pop()
city_list.insert(0,"texas")
print(city_list)