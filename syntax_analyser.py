from lexical_analyser import LexicalAnalyser as la 
from tree_node import TreeNode
text = 'if a  "brnv": vr = 8 - 4'

# Abstract syntax tree

# https://docs.google.com/presentation/d/1MTPMNYwi5UeIVZmG8UHqmGR07cKFshrsJW6RHGFRO6o/edit#slide=id.g24ea8820cd1_0_66

root = TreeNode("root")
conditional = TreeNode("conditional")
conditional, variable, output, colon, integerLiteral = TreeNode("conditional"), TreeNode("identifier"), TreeNode("output"), TreeNode("colon"), TreeNode("integers")
stringLiteral, operators, openBracket, closeBracket =  TreeNode("literals"), TreeNode("operators"), TreeNode("open bracket"), TreeNode("close bracket")
#expression 
integerLiteralExpression1 = integerLiteral
integerLiteralExpression2 = integerLiteral

operatorsExpression = operators
stringLiteralExpression = stringLiteral
variableExpression = variable

expression = TreeNode("expression")
expression.add_child(integerLiteralExpression1), expression.add_child(stringLiteralExpression), expression.add_child(variableExpression)
integerLiteralExpression1.add_child(operatorsExpression)
operatorsExpression.add_child(integerLiteralExpression2)


#first level
root.add_child(conditional), root.add_child(variable), root.add_child(output)

#second level
expressionSecondLevel1 = expression
expressionSecondLevel2 = expression
conditional.add_child(expressionSecondLevel1)
output.add_child(openBracket)
variable.add_child(expressionSecondLevel2)


#third level
expressionThirdLevel = expression
expressionSecondLevel1.add_child(colon)
openBracket.add_child(expressionThirdLevel)

#fourth level
expressionThirdLevel.add_child(closeBracket)

#initializing lexical analyser
q = la()
q.tokenize(text)
print(q.getTokens)

#goes through types of the tokens and matches with tree. 
def syntaxAnalyser(tokens):
    syntaxBool = True
    node = root

    for j in tokens:
        if len(node.children) == 0:
            node = root
        
        children = [i for i in node.children]
        childrenVal = [i.data for i in node.children]
        if len(children) == 0:
            node = root
        token = j[0]   
       
        if token in childrenVal:
            node = children[childrenVal.index(token)]
        else:
            syntaxBool = False
            break
        

    if syntaxBool:
        print("correct syntax")
    else:
        print("wrong syntax")
 