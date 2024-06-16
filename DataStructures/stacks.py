from collections import deque


browsingSession = []

print(browsingSession)

browsingSession.append(1)
browsingSession.append(2)
browsingSession.append(3)

print(browsingSession)

# browsingSession.pop()
# browsingSession.pop()
# browsingSession.pop()  # the last pop makes the browsingSession an [] which is falsy-value
print(browsingSession)

# Falsy values: "", 0, [], False, None
if browsingSession:
    print(browsingSession[-1], " is the last item")
    print("disable back button")

stack = deque()

print(stack)

stack.append(1)
stack.append(3)
stack.append(2)

print(stack)
print(stack.pop())
print(stack.popleft())
print(stack)
