#include "lists.h"
#include <stdlib.h>

/**
* check_list - Recursively checks if an array is a palindrome
* @array: Array to be checked
* @start: Starting index
* @end: Ending index
*
* Return: 1 if array is palindrome, 0 otherwise
*/
int check_list(int *array, int start, int end)
{
	if (start >= end)
		return (1);
	if (array[start] != array[end])
		return (0);
	return (check_list(array, start + 1, end - 1));
}

/**
* is_palindrome - Checks if a linked list is a palindrome
* @head: Pointer to the head of the linked list
*
* Return: 1 if list is a palindrome, 0 otherwise
*/
int is_palindrome(listint_t **head)
{
const listint_t *current = *head;
int length = 0, i = 0, *array, result;

	if (!*head)
		return (1);

	while (current)
{
		current = current->next;
		length++;
}

	array = malloc(sizeof(int) * length);
	if (!array)
		return (0);

	current = *head;
	while (current)
{
		array[i++] = current->n;
	current = current->next;
}

	result = check_list(array, 0, length - 1);
	free(array);
	return (result);
}
