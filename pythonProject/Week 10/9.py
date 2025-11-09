class VotingCheck(Exception):
    def idk(self):
        print('age is too low')

try:
    age = int(input("Enter age: "))
    if age < 18:
        raise VotingCheck()
    else:
        print("Eligible to vote.")
except VotingCheck as e:
    e.idk()
