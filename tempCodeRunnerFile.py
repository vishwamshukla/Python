    pos = close_list.index(i)
            if ((len(stack) > 0) and (open_list[pos] == stack[len(stack)-1])):
                stack.pop()