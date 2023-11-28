#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
/**
*insert_node - insert new number to a list
*
*@head: pointer of pointer to the list
*
*@number: interger to be added
*
*Return: Null or the number added
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_head = malloc(sizeof(listint_t));
listint_t *current_num = NULL;
	if (new_head == NULL)
		return (NULL);
	new_head->n = number;
	new_head->next = NULL;
	if (*head == NULL || (*head)->n >= new_head->n)
{
		new_head->next = *head;
		*head = new_head;
}
else
{
	current_num = *head;
	while (current_num->next != NULL && current_num->next->n < new_head->n)
		current_num = current_num->next;
new_head->next = current_num->next;
current_num->next = new_head;
}
	return (new_head);
}


