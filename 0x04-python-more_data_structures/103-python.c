#include <Python.h>
#include <stdio.h>


/**
 *print_python_bytes - print basic info about python bytes
 *@p: pointer of type PyObject
 *
 *Return: nothing, its a void
 */
void print_python_bytes(PyObject *p)
{
	int i;

	if (PyBytes_Check(p))
	{
		printf("[.] bytes object info\n");
		printf("  size: %lu\n", PyBytes_Size(p));
		printf("  trying string: %s\n", PyBytes_AsString(p));
		if (PyBytes_Size(p) >= 10)
			printf("  first 10 bytes: ");
		else
			printf("  first %lu bytes: ", PyBytes_Size(p) + 1);
		for (i = 0; i < PyBytes_Size(p) && i <= 9; i++)
		{
			printf("%02hhx ", (PyBytes_AsString(p)[i]));
		}
		if (PyBytes_Size(p) < 10)
			printf("00\n");
		else
			printf("\n");
	}
	else
	{
		printf("[.] bytes object info\n");
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}

/**
 *print_python_list - prints basic info about python lists
 *@p: pointer of type PyObject
 *
 *Return: nothing, it's a void
 */
void print_python_list(PyObject *p)
{
	long int i;
	PyObject *item;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %lu\n", PyList_Size(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)(p))->allocated);
	for (i = 0; i < PyList_Size(p); i++)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %lu: ", i);
		printf("%s\n", (((PyObject *)(item))->ob_type)->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
