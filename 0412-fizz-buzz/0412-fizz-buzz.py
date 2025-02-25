class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizz = 3
        buzz = 5

        output = []
        

        for i in range(1,n+1):
            fizz -= 1
            buzz -= 1

            if fizz == 0 and buzz ==0:
                output.append("FizzBuzz")
                fizz = 3
                buzz = 5
            elif fizz == 0:
                output.append("Fizz")
                fizz = 3
            elif buzz == 0:
                output.append("Buzz")
                buzz =5
            else:
                output.append(str(i))
        
        return output



            
        