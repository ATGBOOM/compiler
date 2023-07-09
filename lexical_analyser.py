#stream of text put into compiler
text = 'x = ( 5 + 6 ) * ( 3 - 4 )'

#function to tokenize the stream of text
class LexicalAnalyser():
    def __init__(self):
        self.tokens = []
        self.integers = ("0123456789")
        self.operators ={
        "+":"Add",
        "-":"Subtract",
        "/":"divide",
        "*":"multiply",
        }
        self.literals = ('"')
        self.punctuation = (".", ",", ";", ",")
        self.identifiers = {}
        self.colon = (":")
        self.openBracket = ("(")
        self.closeBracket = (")")
        self.conditional = ("if", "else", "elif")
     
    def tokenize(self, text):
        i = 0
        
        while i < len(text):
          
            if i == " ":
                pass
            elif text[i] == self.openBracket:
                self.tokens.append(("open bracket", i))
            elif text[i] == self.closeBracket:
                self.tokens.append(("close bracket", i))
            elif text[i] == self.colon:
                self.tokens.append(("colon", i))
            elif text[i] in self.integers:
                s = f"{text[i]}"
                i += 1
                while i <len(text) and text[i] in self.integers :
                    s += text[i]
                    i += 1
                self.tokens.append(("integers", int(s))) 
      
            elif text[i] in self.operators:
                self.tokens.append(("operators", text[i]))
            
            elif text[i] == '"':
                s = ""
                i += 1
                while i <len(text) and text[i] != '"' :
                    s += text[i]
                    i += 1
                self.tokens.append(("literals", s))  
            
            elif text[i].lower() in "abcdefghijklmnopqrstuvwxyz":
                s = ""
            
                indentifierVal = LexicalAnalyser()
            
                while i <len(text) and text[i] != " ":
                    s += text[i] 
                    i += 1
                if s in self.conditional:
                    self.tokens.append(("conditional", text[i]))
                    break
                i += 1
                if text[i] == "=":
                    g = ""
                    i += 2
                    while i <len(text) and text[i] != " ":  
                        g += text[i]
                        i+=1                   
                    g += " "
                    indentifierVal.tokenize(g)
                    self.identifiers[s] = indentifierVal.getTokens()
                else:
                    print("ERROR WRONG VARIABLE SYNTAX")
                
                self.tokens.append(("identifier", s)) 
                self.tokens.append(("expression", "yes"))
                self.tokens.append((self.identifiers[s][0][0], self.identifiers[s][0][1]))
                
            i += 1
      
    def getTokens(self):
        return self.tokens
    def getIdentifiers(self):
        return self.identifiers
