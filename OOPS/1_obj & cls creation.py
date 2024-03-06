class college_Bus:
    name = ''
    rouat = ''
    def Bus_no11(self):
        print("Mangalam road")
    def Bus_no17(self):
        print("Paladam road")
person_1 = college_Bus()
person_2 = college_Bus()

person_1.name = "Boy_1"
person_1.rouat = "Andipalayam"
print(person_1.name , person_1.rouat)
person_1.Bus_no11()
print(end = "\n")

person_2.name = "Boy_2"
person_2.rouat = "Paladam"
print(person_2.name , person_2.rouat)
person_2.Bus_no17()