#ifndef clibf
#define clibf
#ifdef __cplusplus
extern "C" {
#endif
#include <stdio.h>
#include "Python.h"
static PyObject * run(PyObject * self, PyObject * arg);
static PyMethodDef clibf_methods[] = {
    {"run", run, METH_O, "run bf code"},
    {NULL, NULL, 0, NULL}
};
static struct PyModuleDef clibf_module = {PyModuleDef_HEAD_INIT, "_clibf", NULL, -1, clibf_methods};
PyMODINIT_FUNC PyInit__clibf(void){return PyModule_Create(&clibf_module);}
int pointer = 0, data[30000] = {0};
int end(char *source) {
    int loops = 1;
    for (int i = 0; source[i]; i++) {
        loops += (source[i] == '[') - (source[i] == ']');
        if (!loops) return i + 1;
    }
}
void execute(char *source, int loop_end);
void execute_loop(char *source, int loop_end) {
    do {
        execute(source, loop_end);
    } while (data[pointer]);
}
void execute(char *source, int loop_end) {
    int i = 0;
    while (source[i] && (i < loop_end || !loop_end)) {
        switch (source[i]) {
        case '>':
            pointer++;
            pointer %= 30000;
            break;
        case '<':
            pointer--;
            pointer += 30000;
            pointer %= 30000;
            break;
        case '+':
            data[pointer]++;
            data[pointer] %= 256;
            break;
        case '-':
            data[pointer]--;
            data[pointer] += 256;
            data[pointer] %= 256;
            break;
        case '.':
            putchar(data[pointer]);
            break;
        case ',':
            data[pointer] = getchar();
            break;
        case '[':
            int j = end(source + i + 1);
            execute_loop(source + i + 1, j);
            i += j;
            break;
        default:
            break;
        }
        i++;
    }
}
static PyObject * run(PyObject * self, PyObject * arg) {
    if (!PyUnicode_Check(arg)) {
        PyErr_SetString(PyExc_TypeError, "Argument must be a string");
        return NULL;
    }
    execute(PyUnicode_AsUTF8(arg), 0);
    Py_RETURN_NONE;
}
#ifdef __cplusplus
}
#endif
#endif