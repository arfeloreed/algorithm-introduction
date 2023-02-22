# use recursion to implement a countdown timer

def countdown(n):
    if n <= 0:
        print('Blastoff!')
        return
    else:
        print(f"{n}...")
        countdown(n-1)
        print("foo")

countdown(5)