

class MyMath:

    @classmethod
    def add(self, *args):
        return sum(args)

    def max(self,*args):
        return max(args)




print(MyMath.add(5,6,7,8,9))
