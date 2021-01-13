#include <stdio.h>
#include <Python.h>
#include <math.h>

/**
 * print_python_string - prints some basic info about Python strings
 * @p: PyObject
 * Return: Void
 */
void print_python_string(PyObject *p)
{

	printf("[.] string object info\n");
	if (PyUnicode_Check(p))
	{
		if (PyUnicode_IS_COMPACT_ASCII(p))
			printf("  type: compact ascii\n");
		else
			printf("  type: compact unicode object\n");
		printf("  length: %zd\n", PyUnicode_GetLength(p));
		printf("  value: %ls\n", PyUnicode_AsWideCharString(p, NULL));}
	else
	{
		printf("  [ERROR] Invalid String Object\n");
	}
}
