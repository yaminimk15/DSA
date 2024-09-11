

class letter:
    def __init__(self,string):
        self.string=string
    def seperator(self):
        vowels="aieou"
        vowel=""
        constant=""
        for ch in self.string.lower():
            if ch in vowels:
                vowel+=ch
            else:
                constant+=ch
        print("constant+vowels:" ,constant+vowel)
        return 0
a=input("enter a word: ")
obj=letter(a)
obj.seperator()
