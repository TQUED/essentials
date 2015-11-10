#!/usr/bin/python2.7

def infixTOPostfix(infList):

    postFixExpr = []
    oprtrS = Stack()
    ip = infList.split()
    precd = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}

    for i in ip:
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or in "0123456789":
            postFixExpr.append(i)
        elif token == '(':
            oprtrS.push(i)
        elif token == ')':
            i1 = oprtrS.pop()
            while i1 != '(':
                postFixExpr.append(i1)
                i1 = oprtrS.pop()
        else:
            while (not oprtrS.isEmpty()) and \
                (precd[oprtrS.peek()] >= precd[i]):
                postFixExpr.append(oprtrS.pop())
            oprtrS.push(i)
    while not oprtrS.isEmpty():
        postFixExpr.append(oprtrS.pop())
    return " ".join(postFixExpr)            
