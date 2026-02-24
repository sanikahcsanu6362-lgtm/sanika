class student:
    def __init__(self):
        self.items=[]
    def insert(self):
        n=int(input("enter the number of records:"))
        for i in range(n):
            name=input("enter sname:")
            regno=input("enter registration number:")
            branch=input("enter branch name:")
            result=input("enter result:")
    def delete(self):
        regno=int(input("enter regno to delete:"))
        for row in self.items:
            for i in row:
                if i==regno:
                    self.items.remove(row)
    def display(self):
        for i in self.items:
            print(i)
s=student()
s.insert()
s.display()
s.delete()
s.display()456
