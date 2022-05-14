# clibf

## Install

### From PyPi

```sh
pip install clibf
```

### From GitHub

```sh
pip install git+https://github.com/donno2048/bf-interpreter
```

## Run

### Brainfuck file

```sh
clibf -f my_bf_script.b
# or with a prompt
clibf -F
```

### String

```sh
clibf -s "+[+[<<<+>>>>]+<-<-<<<+<++]<<.<++.<++..+++.<<++.<---.>>.>.+++.------.>-.>>--."
```

### Choose file with GUI

```sh
clibf -g
```
