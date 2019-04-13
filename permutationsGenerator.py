# l = [1, 2, 3]

def swap(a, b):
    tmp = a
    a = b
    b = tmp

def generatePermutations(A):
    # c is an encoding of the stack state. c[k] encodes the for-loop counter for when generate(k+1, A) is called
    c = []
    n = len(A)
    ans = []
    for i in range(n):
        c.append(0)

    temp = ''
    for i in A:
        temp += str(i)
    ans.append(temp + '')

    # i acts similarly to the stack pointer
    i = 0
    while i < n:
        if c[i] < i:
            if i % 2 == 0:
                tmp = A[0]
                A[0] = A[i]
                A[i] = tmp
            else:
                tmp = A[c[i]]
                A[c[i]] = A[i]
                A[i] = tmp
            temp = ''
            for j in A:
                temp += str(j)
            ans.append(temp + '')
            # Swap has occurred ending the for-loop. Simulate the increment of the for-loop counter
            c[i] += 1
            # Simulate recursive call reaching the base case by bringing the pointer to the base case analog in the array
            i = 0
        else:
            # Calling generate(i+1, A) has ended as the for-loop terminated. Reset the state and simulate popping the stack by incrementing the pointer.
            c[i] = 0
            i += 1
    return ans + []

# print(generatePermutations(l))
