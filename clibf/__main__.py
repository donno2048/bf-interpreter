from clibf import execute
from argparse import ArgumentParser
def main():
    parser = ArgumentParser(description = 'Brainfuck input')
    group = parser.add_mutually_exclusive_group(required = True)
    group.add_argument('-g', '--gui', action='store_true')
    group.add_argument('-s', '--string', metavar='', type = str)
    group.add_argument('-f', '--file', metavar='', type = str)
    args = parser.parse_args()
    string = args.string
    file = args.file
    if args.gui:
        from tkinter import Tk
        from tkinter.filedialog import askopenfilename
        Tk().withdraw()
        file = askopenfilename(filetypes = [("Brainfuck files", "*.b")])
    if file is None: execute(string)
    else: execute(open(file).read())
if __name__ == '__main__': main()
