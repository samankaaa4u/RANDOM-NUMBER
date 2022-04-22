import random

class randomnumber:
    def execution(self):
        self.my_list = []

        for i in range(10):
            self.my_list = random.randrange(0,1000)

            print("Random #: " + str(self.my_list))

result = randomnumber()
result.execution()






