class Solution:
    def toGoatLatin(self, S: str) -> str:
        res = []
        cnt = 1
        vowel = {'a','e','i','o','u'}
        if len(S) == 1:
            return S+'maa'
        slow, fast = 0, 0
        while fast < len(S):
            while slow == 0 and S[fast] != " ":
                fast += 1
                if fast == len(S)-1:
                    break
            if S[fast] == " " or fast==len(S)-1:
                if fast == len(S)-1:
                    word = S[slow:]
                else:
                    word = S[slow:fast]
                if word[0].lower() in vowel:
                    res.append(word + 'ma' + 'a'*cnt)
                else:
                    res.append(word[1:] + word[0] + 'ma' +'a'*cnt)
                cnt += 1
                slow = fast+1
                fast += 1
            else:
                fast += 1
        return " ".join(res)