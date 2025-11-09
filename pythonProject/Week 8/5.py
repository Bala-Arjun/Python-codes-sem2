class Sample:
    def __init__(self):
        print("Object is created")
    def msg(self):
        print("Hello CSE")
    def __del__(self):
        print("Object is destroyed..")
s=Sample()
for i in range(3):
    s.msg()
