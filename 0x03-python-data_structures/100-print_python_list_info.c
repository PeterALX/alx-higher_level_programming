#include <Python.h>
void print_python_list_info(PyObject *p) {
	PyListObject *pAsList =  (PyListObject *)p;
	printf("[*] Size of the Python List = %zd\n", Py_SIZE(p));
	printf("[*] Allocated = %zd\n", pAsList->allocated);

	for (Py_ssize_t i = 0; i < Py_SIZE(p); i++){
		printf("Element %zd: %s\n", i ,Py_TYPE(pAsList->ob_item[i])->tp_name);
	}
}
