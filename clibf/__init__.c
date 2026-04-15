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
    return -1;
}
int execute(const char *source, int loop_end);
int execute_loop(const char *source, int loop_end) {
    do {
        if (execute(source, loop_end))
            return 1;
    } while (data[pointer]);
    return 0;
}
int execute(const char *source, int loop_end) {
    if (loop_end == -1) {
        PyErr_SetString(PyExc_ValueError, "'[' and ']' mismatched");
        return 1;
    }
    int i = 0, j;
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
            j = end(source + i + 1);
            if (execute_loop(source + i + 1, j))
                return 1;
            i += j;
            break;
        default:
            break;
        }
        i++;
    }
    return 0;
}
static PyObject * run(PyObject * self, PyObject * arg) {
    if (!PyUnicode_Check(arg)) {
        PyErr_SetString(PyExc_TypeError, "Argument must be a string");
        return NULL;
    }
    if (execute(PyUnicode_AsUTF8(arg), 0))
        return NULL;
    Py_RETURN_NONE;
}
#ifdef __cplusplus
}
#endif
#endif
