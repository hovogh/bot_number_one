sampleDict = {"class 1": {"student_1": {"name": "Mike",
                                        "marks": {"physics": 70,
                                                  "history": 80}},
                          "student_2": {"name": "Jack",
                                        "marks": {"physics": 80,
                                                  "history": 75}}},
              "class 2": {"student_1": {"name": "Jon",
                                        "marks": {"physics": 79,
                                                  "history": 40}},
                          "student_2": {"name": "Steven",
                                        "marks": {"physics": 90,
                                                  "history": 62}}}}
print('Where you want to add?')
class_n = input('Enter class number:')
student_n = input('Enter student number:')
name_i = input('Enter student name:')
velu_p = input('Enter physics velu:')
velu_h = input('Enter history velu:')
sampleDict["class 1"] = {"student_" + student_n: {"name": name_i}, "marks":{"physics": velu_p, "history": velu_h}}
print(sampleDict)




