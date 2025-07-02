
import sys
stack = []

# push X: 정수 X를 스택에 넣는 연산이다.
def push(x):
    stack.append(x)

# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def pop():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])
        stack.pop()

# size: 스택에 들어있는 정수의 개수를 출력한다.
def size():
    print(len(stack))

# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)

# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
def top():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])

if __name__ == "__main__":

    # how many commands
    lines = int(input())
    # print(f"{lines}")
    
    for commands in range(lines):
        cmd = input().strip().split()
        if cmd[0] == "push":
            push(int(cmd[1]))
        elif cmd[0] == "pop":
            pop()
        elif cmd[0] == "size":
            size()
        elif cmd[0] == "empty":
            empty()
        elif cmd[0] == "top":
            top()
