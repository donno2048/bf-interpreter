from clibf import execute
from questionary import path
from argparse import ArgumentParser
def main():
    parser = ArgumentParser(description = 'Brainfuck input')
    group = parser.add_mutually_exclusive_group(required = True)
    group.add_argument('-g', '--gui', action='store_true')
    group.add_argument('-s', '--string', metavar='', type = str)
    group.add_argument('-f', '--file', metavar='', type = str)
    group.add_argument('-F', '--file-prompt', action='store_true')
    args = parser.parse_args()
    string = args.string
    file = args.file if not args.file_prompt else path('Brainfuck file').ask()
    if args.gui:
        from tkinter import Tk
        from tkinter.filedialog import askopenfilename
        Tk().withdraw()
        file = askopenfilename(filetypes = [("Brainfuck files", "*.b")])
    if file is None: execute(string)
    else: execute(open(file).read())
    print() # Newline
if __name__ == '__main__': main()
