class Solution(object):
    def isNumber(self, s,t=1,tt=1):
        if t==1: s,i=s.strip(' '),s.strip(' ').find('e')
        if t==1 and i!=-1: return self.isNumber(s[:i],0,1) and self.isNumber(s[i+1:],-1,0)
        if s.count('.')>tt: return False
        return len(s)-len(s.lstrip('+-'))<2 and s.lstrip('+-').replace('.','').isdigit()
