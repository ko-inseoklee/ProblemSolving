class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        if(len(p) > 2000):
            return false
        
        sTemp = list(s)
        pTemp = list(p)
        
        sList = []
        pList = []
        
        for i in range(len(sTemp)):
            temp = [i,sTemp[i]]
            sList.append(temp)
            
        for i in range(len(pTemp)):
            temp = [i,pTemp[i]]
            sList.append(temp)
        
        print(sList)
        print(pList)

        