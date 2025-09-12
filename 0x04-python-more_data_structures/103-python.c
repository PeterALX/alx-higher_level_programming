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
	int bytesToPrint = size + 1 < 10 ? size + 1 : 10;

  printf("  size: %zd\n", size);
  printf("  trying string: %s\n", sval);
  printf("  first %d bytes:", bytesToPrint);
  for (int i = 0; i < bytesToPrint; i++) {
    printf(" %02x", (unsigned char)sval[i]);
  }
  printf("\n");
}
void print_python_list(PyObject *p) {
	PyListObject *pAsList =  (PyListObject *)p;
	Py_ssize_t size = pAsList->ob_base.ob_size;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", pAsList->allocated);

	for (Py_ssize_t i = 0; i < size; i++){
		const char *type = pAsList->ob_item[i]->ob_type->tp_name;
		printf("Element %zd: %s\n", i ,type);
		if (strcmp("bytes", type) == 0) {
			print_python_bytes(pAsList->ob_item[i]);
		}
	}
}
