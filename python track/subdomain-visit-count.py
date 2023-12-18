class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dic = Counter()
        for i in cpdomains:
            n, dom = i.split()
            n=int(n)
            while '.' in dom:
                dic[dom]+=n
                dom=dom[dom.index('.')+1:]
            dic[dom]+=n
        ans=[]
        for key,value in dic.items():
            ans.append(str(value)+" "+key)
        return ans
    
        