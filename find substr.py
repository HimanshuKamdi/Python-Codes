class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
      
      for i in range(len(s)//2+1,0,-1):
        if len(s)%i==0:
          c=s.count(s[0:i])
          if len(s)//i==c and c!=1:
            return True
      return False
        
#         j=0
#         c=0
#         if len(s)%i==0:       
#           for j in range(0,len(s)-i-i+1,i):
            
#             if s[j:j+i]==s[j+i:j+i+i] :
#               c+=1
#             else:
#               break
#           if len(s)//i-1==c:
#             return True
#       return False
          
        