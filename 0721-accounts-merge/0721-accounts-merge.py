class Account:
    def __init__(self, name, emails=set()):
        self.name = name
        self.emails = emails
        
    def combine(self, other, cache, allAccounts):
        if self == other:
            return 
        
        self.emails.update(other.emails)
        allAccounts.remove(other)
        
        for email in other.emails:
            cache[email] = self
    
    def toList(self):
        return [self.name] + sorted(list(self.emails))

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        cache = {}
        allAccounts = set()
        
        for account in accounts:
            name = account[0]
            emails = account[1:]
            currAccount = Account(name, set(emails))
            allAccounts.add(currAccount)
            
            for email in emails:
                if email in cache:
                    currAccount.combine(cache[email], cache, allAccounts)
                else:
                    cache[email] = currAccount
                    
        
        
        result = []
        for account in allAccounts:
            result.append(account.toList())
        return result