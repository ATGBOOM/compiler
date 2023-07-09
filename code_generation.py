import ast, syntax_analyser, tree_node
from lexical_analyser import LexicalAnalyser as la 

code = 'x = ( 5 + 4 ) * ( 7 + 2 )'
q = la()
q.tokenize(code)
tokens = q.getTokens()
variables = ast.makingVariable(tokens)
parents = ast.FindParents(variables)
AST = tree_node.BinaryTreeNode("AST")
ast.ParentTreeStart(AST, parents, variables)

print(AST.left.right.left.returnSelf())