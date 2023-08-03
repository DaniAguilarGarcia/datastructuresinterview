#time complexity O(N+M)

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        #replace punctuatio with soaces, and put letters in lower case
        norm_str = ''.join(c.lower() if c.isalnum( else ' ' for c in paragraph))
        #split string into words
        words = norm_str.split()
        word_count = defaultdict(int)
        banned_words = set(banned)
        #count the appearance of each , excluding banned
        for word in words:
            if word not in banned_words:
                word_count[word] += 1
        #return the word with the highest frequency
        return max(word_count.items(), key=operator.itemgetter(1))[0]


#character processing in one pass
#process the string just once on the fly

class Solution:
    def mostCommonWord1(self, paragraph: str, banned: List[str]) -> str:

        banned_words = set(banned)
        ans = ""
        max_count = 0
        word_count = defaultdict(int)
        word_buffer = []

        for p, char in enumarate(paragraph):
            #consume the char in a word
            if char.isalnum(): #either letters or numbers
                word_buffer.append(char.lower())
                if p != len(paragraph)-1:
                    continue
            # at the end of one word or the end or paragraph
            if len(word_buffer) > 0:
                word = "".join(word_buffer)
                if word not in banned_words:
                    word_count[word] +=1
                    if word_count > max_count:
                        max_count = word_count[word]
                        ans = word
                word_buffer = []
        return ans 

