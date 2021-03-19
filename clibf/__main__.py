from clibf import string, file
pointer, data = 0, [0] * 30000
def end(source, loops = 1):
    for i in range(len(source)):
        loops += (source[i] == '[') - (source[i] == ']')
        if not loops:return i + 1
def execute(source, i = 0):
    global pointer, data
    while i < len(source):
        pointer += (source[i] == '>') - (source[i] == '<');pointer %= 30000;data[pointer] += (source[i] == '+') - (source[i] == '-');print((source[i] == '.') * chr(data[pointer] % 256), end='')
        if source[i] == ',':data[pointer] = ord(input('\n'))
        if source[i] == '[':j = end(source[i + 1:]);execute_loop(source[i + 1 : j + i]);i += j
        i += 1
    return data
def execute_loop(source):
    while execute(source)[pointer] % 256:pass
def main():
    if file is None: execute(string)
    else:execute(open(file,'r').read())
