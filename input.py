import sys
print('Starting to get input from the std input')
while True:
    x = sys.stdin.readline()
    print(f'got a line from stdin: len= {len(x)} and text: {x}')
    