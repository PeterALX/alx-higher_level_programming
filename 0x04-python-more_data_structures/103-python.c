#include <Python.h>
void print_python_bytes(PyObject *p) {
  printf("[.] bytes object info\n");
  if (!PyBytes_Check(p)) {
    printf("  [ERROR] Invalid Bytes Object\n");
    return;
  }
  PyBytesObject *pAsBytesObj = (PyBytesObject *)p;
  Py_ssize_t size = pAsBytesObj->ob_base.ob_size;
  char *sval = pAsBytesObj->ob_sval;

  printf("  size: %zd\n", size);
  printf("  trying string: %s\n", sval);
  printf("  first %zd bytes:", size + 1);
  for (int i = 0; i < size + 1; i++) {
    printf(" %02x", (unsigned char)sval[i]);
  }
  printf("\n");
}
void print_python_list(PyObject *p) { printf("in biz: %p\n", (void *)p); }
