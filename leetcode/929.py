class Solution:
    def numUniqueEmails(self, emails: 'List[str]') -> 'int':
        uniqueEmails = set()
        for email in emails:
            local, domain = email.split('@')
            localPlus = local.split('+')[0]
            localDot = ''.join(localPlus.split('.'))
             
            uniqueEmails.add(''.join([localDot, domain]))
        return len(uniqueEmails)

#test 
if __name__ == '__main__':
    print(Solution().numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))