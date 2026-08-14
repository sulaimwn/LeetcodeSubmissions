class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for c in tokens:
            #evaluate every operator
            if c=="+":
                stack.append(stack.pop()+stack.pop())
            elif c=="-":
                a,b=stack.pop(),stack.pop()
                stack.append(b-a)
                #for - and / the order matters. and its second last - first last to properly subtract
            elif c=="*":
                stack.append(stack.pop()*stack.pop())
            elif c=="/":
                a,b= stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(c))
        return stack[0]
        