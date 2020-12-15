#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: PyObject
 * Return: Void
 */
void print_python_list_info(PyObject *p)
{
	int size;
	int alloc;
	int i;
	PyObject *item;

	size = (int)PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %i\n", size);
	printf("[*] Allocated =  %i\n", alloc);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %i: %s\n", i, Py_TYPE(item)->tp_name);
	}

}
