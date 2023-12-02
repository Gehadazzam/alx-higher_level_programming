#include "lists.h"
#include <stdlib.h>
/**
*check_list - compare the list
*
*@array: first parameter
*
*@idx1: seconed one
*
*@idx2: third one
*
*Return: 1 or 0
*/
int check_list(int *array, int idx1, int idx2)
{
	if (idx1 > idx2)
		return (1);
	if (array[idx1] != array[idx2])
		return (0);
	return (check_list(array, idx1 + 1, idx2 - 1));
}
/**
*is_palindrome - check if the list is palindrome
*
*@head: pointer to pointer of the list
*
*Return: 1 or 0
*/
int is_palindrome(listint_t **head)
{
const listint_t *current = *head;
int length = 0, x = 0, *array;
	if (!*head)
		return (1);
	while (current)
{
		current = current->next;
		length++;
}
	current = *head;
	array = malloc(sizeof(int) * length);
	if (!array)
		return (0);
	for (x = 0; x < length; x++)
{
		array[x] = current->n;
		current = current->next;
}
	if (check_list(array, 0, length - 1) == 1)
{
		free(array);
		return (1);
}
	free(array);
	return (0);
}
