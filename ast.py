from lexical_analyser import LexicalAnalyser as la 
from tree_node import BinaryTreeNode
code = 'x = ( 5 + 7 ) * ( 6 + 11 )'
q = la()
q.tokenize(code)
tokens = q.getTokens()


#making variables for tree nodes
def makingTree(data):
    x = BinaryTreeNode(data)
    return x

def makingVariable(tokens):
    variables = []
    count = 0
    index = 0
    while index < len(tokens):
  
        if tokens[index][0] == "identifier":
            variables.append([count, tokens[index]])
            index += 1
        elif tokens[index][0] == "open bracket":
            variables.append([count])
            index +=  1
            secCount = 0
            while index<len(tokens) and tokens[index][0] != "close bracket":     
                variables[count].append([secCount,tokens[index]])
                index += 1
                secCount += 1
            index += 1
        else:
            variables.append([count, tokens[index]])
            index += 1
        count += 1
    return variables

def FindParents(variables):
    nodes = ["operators", "expression"]
    parents = []

    for var in variables:
        if var[1][0] in nodes:
            parents.append(variables.index(var))
    return parents

def ParentTreeStart(root, parents, variables):
    print(parents)
    x = makingTree(variables[parents[0]])
    y = makingTree(variables[parents[1]])
    
    root.add_child_left(x)
   
    x.add_child_left(variables[:parents[0]])
   
    x.add_child_right(y)
    y.add_child_left(variables[parents[0]+1:parents[1]][0])
    y.add_child_right(variables[parents[1]+1:][0])

    treeEnd(y)
    return root

def treeEnd(y):
    #print(y.right)
    #print(y.left)
    if len(y.right)>2:
     
        variables = y.right[1:]
    
        par = FindParents(variables)
        
        ParentTreeMake(y, par, variables, "right")
    if len(y.left) > 2:
        variables =y.left[1:]
  
        par = FindParents(variables)
        
        ParentTreeMake(y, par, variables, "left")
    
def ParentTreeMake(y, parents, variables, side):
    #print(variables)
    x = makingTree(variables[parents[0]])
    
    if side == "right":
        y.add_child_right(x) 
    else:
        y.add_child_left(x)
    x.add_child_left(variables[:parents[0]])
    x.add_child_right(variables[parents[0] + 1:])
    treeEnd(x)
        




#variables = makingVariable(tokens)
#parents = FindParents(variables)
#AST = BinaryTreeNode("AST")
#ParentTreeStart(AST, parents, variables)




