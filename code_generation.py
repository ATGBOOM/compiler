import ast, syntax_analyser, tree_node
from lexical_analyser import LexicalAnalyser as la 

class VariableForRegister:
    def __init__(self):
        self.data = None 
    def addData(self, data):
        self.data = data
    def returnData(self):
        return self.data

code = 'x = ( 5 - 4 ) * ( 7 + 2 )'
q = la()
q.tokenize(code)
tokens = q.getTokens()
variables = ast.makingVariable(tokens)
parents = ast.FindParents(variables)
AST = tree_node.BinaryTreeNode("AST")
ast.ParentTreeStart(AST, parents, variables)

#so what we r doing here is the x = V1 then v1 = v2 * v3 thing. So u made a class and assigned register dictionary to keep all the code and then a variables to store the V1, v2 etc
# here you first check if its an expression or operator, if expression u make a V and assign it to the left side and the recurse through the right side of tree
#now u fill find an operator, 

class traverseTree:
    def __init__(self):
        self.registers = {}
        self.count = 0
        self.variables = {}
    def assigningTreeAdress(self, tree):
        if str(type(tree)) == "<class 'tree_node.BinaryTreeNode'>":
            val = tree.returnSelf()
            
            if val[1][0] == "expression":
                self.count += 1
                self.variables[f"V{self.count}"] = []
                x = tree.left
                self.registers[tree.left[0][1][1]] = f"V{self.count}"
                self.assigningTreeAdress(tree.right)
            if val[1][0] == "operators":
                
                self.registers[f"V{self.count}"] = [val[1]]
                og = self.count
           
                self.count += 1
                self.variables[f"V{self.count}"] = []
                self.registers[f"V{og}"].append(f"V{self.count}")
                self.assigningTreeAdress(tree.left)

                self.count += 1
                self.variables[f"V{self.count}"] = []          
                self.registers[f"V{og}"].append(f"V{self.count}")
                self.assigningTreeAdress(tree.right)
        else:
            self.variables[f"V{self.count}"].append(tree[0][1][1]) 
    
    def returnVar(self):
        return self.variables
    def returnReg(self):
        return self.registers
        
a = traverseTree()
a.assigningTreeAdress(AST.left)
variables = a.returnVar()
registers = a.returnReg()

def codeGeneration(vars, regs):
    i = len(vars) - 1
    for i in reversed(regs.keys()):
   
        if len(regs[i]) == 3:
           
            vars[i] = [eval(f"{vars[regs[i][1]][0]} {regs[i][0][1]} {vars[regs[i][2]][0]}")]
            regs[i] = eval(f"{vars[regs[i][1]][0]} {regs[i][0][1]} {vars[regs[i][2]][0]}")
        else:
            regs[i] = regs[regs[i]]
    return regs[i]
       
print(codeGeneration(variables, registers))
