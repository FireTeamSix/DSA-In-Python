from .stackarray612 import ArrayStack

def reverse_file(filename):
    """Overwrite given file with its contents line-by-line reversed."""
    S = ArrayStack()
    original = open(filename)
    
    for line in original:
        S.push(line.rstrip('\n'))
    original.close()

    #now we overwrite with contents in LIFO order
    output = open(filename, 'w')  # reopening file overwrites signal
    while not S.is_empty():
        output.write(S.pop() + '\n')  # re-insert newline characters
    output.close()