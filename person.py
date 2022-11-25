class Person:
    legs=2
    eyes=2
    def accept(self,id,name,height):
        self.id=id
        self.name=name
        self.height=height
    def display(self):
        print(f'id={self.id},name={self.name},height={self.height}')
    @classmethod
    def disp(cls):
        print(f'legs={cls.legs},eyes={cls.eyes}')

yoji=Person()
yoji.accept(1,'yojith',4.2)
yoji.display()
yoji.disp()
ayyappa=Person()
ayyappa.accept(100,'ayyappa',5.3)
ayyappa.display()
ayyappa.disp()
jay=Person()
jay.accept(4,'jay',2.5)
jay.display()
jay.disp()
