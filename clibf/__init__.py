from argparse import ArgumentParser
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