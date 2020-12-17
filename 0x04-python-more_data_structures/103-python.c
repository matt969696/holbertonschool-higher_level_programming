#include <stdio.h>
#include <Python.h>


void print_python_bytes(PyObject *p);


/**
 * print_python_list - prints some basic info about Python lists
 * @p: PyObject
 * Return: Void
 */
void print_python_list(PyObject *p)
{
	int size;
	int alloc;
	int i;
	PyObject *item;
	PyObject **obj;

	if (PyList_Check(p))
	{
		size = ((PyVarObject *)p)->ob_size;
		alloc = ((PyListObject *)p)->allocated;
		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %i\n", size);
		printf("[*] Allocated = %i\n", alloc);

		obj = ((PyListObject *)p)->ob_item;
		for (i = 0; i < size; i++)
		{
			item = obj[i];
			printf("Element %i: %s\n", i, item->ob_type->tp_name);
			if (strcmp(item->ob_type->tp_name, "bytes") == 0)
				print_python_bytes(item);
		}
	}
}



/**
 * print_python_bytes - prints some basic info about Python Bytes
 * @p: PyObject
 * Return: Void
 */
void print_python_bytes(PyObject *p)
{
	int size, nb, i;
	char *string;

	printf("[.] bytes object info\n");

	if (PyBytes_Check(p) != 1)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	printf("  size: %i\n", size);
	string = ((PyBytesObject *)p)->ob_sval;
	printf("  trying string: %s\n", string);
	if (size <= 9)
		nb = size + 1;
	else
		nb = 10;

	printf("  first %i bytes:", nb);
	for (i = 0; i < nb; i++)
		printf(" %02x", string[i] & 0xff);
	printf("\n");

}
