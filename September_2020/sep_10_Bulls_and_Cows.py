class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a = 0
        secret_freq = {}
        guess_freq = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1
            else:
                if secret[i] in secret_freq:
                    secret_freq[secret[i]] += 1
                elif secret[i] not in secret_freq:
                    secret_freq[secret[i]] = 1
                if guess[i] in guess_freq:
                    guess_freq[guess[i]] += 1
                else:
                    guess_freq[guess[i]] = 1
        b = 0
        for k in guess_freq.keys():
            if k in secret_freq:
                b += min(guess_freq[k], secret_freq[k])
        return str(a) + "A" + str(b) + "B"