#include <Python.h>
#include <stdio.h>

/**
 *print_python_float - print basic info about python floats
 *@p: pointer of type PyObjetc
 *
 *Return: nothing, it's a void
 */
void print_python_float(PyObject *p)
{
	char *value;

	if (PyFloat_Check(p))
	{
		printf("[.] float object info\n");
		value = PyOS_double_to_string(PyFloat_AsDouble(p), 'r',
					      0, Py_DTSF_ADD_DOT_0, NULL);
		printf("  %s\n", value);
	}
	else
	{
		printf("[.] float object info\n");
		printf("  [ERROR] Invalid List Object\n");
	}
}
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
		printf("  trying string: %s\n", ((PyBytesObject *)(p))->ob_sval);
		if (PyBytes_Size(p) >= 10)
			printf("  first 10 bytes: ");
		else
			printf("  first %lu bytes: ", PyBytes_Size(p) + 1);
		for (i = 0; i < PyBytes_Size(p) && i <= 9; i++)
		{
			printf("%02hhx", (((PyBytesObject *)(p))->ob_sval)[i]);
			if (i < 9)
				printf(" ");
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

	if (PyList_Check(p))
	{
		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %lu\n", ((PyVarObject *)(p))->ob_size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)(p))->allocated);
		for (i = 0; i < ((PyVarObject *)(p))->ob_size; i++)
		{
			item = PyList_GET_ITEM(p, i);
			printf("Element %lu: ", i);
			printf("%s\n", (((PyObject *)(item))->ob_type)->tp_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
			if (PyFloat_CheckExact(item))
				print_python_float(item);
		}
	}
	else
	{
		printf("[*] Python list info\n");
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}
