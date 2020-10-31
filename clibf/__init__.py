from argparse import ArgumentParser
parser = ArgumentParser(description = 'Brainfuck input')
group = parser.add_mutually_exclusive_group(required = True)
group.add_argument('-s', '--string', metavar='', type = str)
group.add_argument('-f', '--file', metavar='', type = str)
args = parser.parse_args()
string = args.string
file = args.file
