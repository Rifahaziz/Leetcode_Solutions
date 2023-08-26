class Solution:
    def addBinary(self, a: str, b: str) -> str:


        # way 1 : shortcut
         result = bin(int(a, 2) + int(b, 2))
    
         # Remove the '0b' prefix from the binary representation
         result = result[2:]
    
         return result



        # way 2 : from scratch
        # if (len(a)>len(b)):
        #     zeroes_to_add = len(a) - len(b) 
        #     for k in range(zeroes_to_add):
        #         b= "0"+b
        # elif(len(a)< len(b)):
        #      zeroes_to_add = len(b) - len(a) 
        #      for m in range(zeroes_to_add):
        #         a = "0"+a

        # print(a, "-" , b)        
        # a_split= a.split()
        # b_split= b.split()

        # result = []
        # carry=0
        # for i in reversed(a_split):
        #     for j in reversed(b_split):
        #         ij=0
        #         carry=carry
        #         if(i==0):
        #             if(j==0):
        #                 ij=0
        #                 if(carry==1):
        #                     ij = 1
        #                     carry=0
        #             else:
        #                 ij=1
        #                 if(carry==1):
        #                     ij=0
        #                     carry=1
                    
        #         elif(i==1):
        #             if(j==0):
        #                 ij=0
        #                 if(carry==1):
        #                     ij=1
        #                     carry=0
        #             else:
        #                 ij=0
        #                 carry=1

        #         result.append(ij)
                
        # result= result.reverse()
        # return result

                    

