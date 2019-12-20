#include <Python.h>
#include <stdio.h>

/**
 *print_python_list_info - prints basic info about python lists
 *@p: pointer of type PyObject
 *
 *Return: nothing, it's a void
 */
void print_python_list_info(PyObject *p)
{
	long int i;
	PyObject *item;

	printf("[*] Size of the Python List = %lu\n", PyList_Size(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)(p))->allocated);
	for (i = 0; i < PyList_Size(p); i++)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %lu: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
