#using stirng split method
#split() breaks a given string around the matches of he given regex
#replac() 
class Solution:
    def numUnique(self, emails: List[str])-> int:
        #hash set to store all the unique emails
        uniqueEmails = set()

        for email in emails:
            #split into two parts
            name, domain = email.split('@')
            # split local by "+" and replace all "." with ''.
            local = name.split('+')[0].replace('.','')

            #concatenate local. '@', and domain.
            uniqueEmails.add(local + '0' + domain)
        return len(uniqueEmails)
#complexity O(N.M)