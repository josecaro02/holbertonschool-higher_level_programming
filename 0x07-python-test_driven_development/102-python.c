#include <stdarg.h>
#include <Python.h>
#include <stdio.h>

/**
 *print_python_string - print basic strings info
 *@p: pirint of type PyObject
 *
 *Return: nothing, it's a void
 */
void print_python_string(PyObject *p)
{
	if (PyUnicode_Check(p))
	{
		printf("[.] string object info\n");
		printf("  type: %s\n", PyUnicode_FromObject(p));
		printf("  lenght: %lu\n", PyUnicode_GET_SIZE(p));
		/* printf("  value: %s\n", PyUnicode_AS_DATA(p)); */
	}
	else
	{
		printf("[.] string object info\n");
		printf("  [ERROR] Invalid String Object\n");
	}
}
