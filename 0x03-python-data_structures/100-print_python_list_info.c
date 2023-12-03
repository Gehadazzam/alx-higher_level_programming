#include <Python.h>
#include <listobject.h>
#include <stdio.h>
/**
*print_python_list_info - print the info list of python
*
*@p: pointer
*
*Return: void
*/
void print_python_list_info(PyObject *p)
{
int i;
	if (!PyList_Check(p))
{
		printf("Error: p is not a valid PyListObject\n");
		return;
}
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < PyList_Size(p); i++)
{
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
}
}
