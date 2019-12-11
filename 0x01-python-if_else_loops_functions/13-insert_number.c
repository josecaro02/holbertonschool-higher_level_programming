#include "lists.h"

/**
 *insert_node - insert a node at the position in wich the list keep sorted
 *@head: head of the linked list
 *@number: value of the node to add
 *
 *Return: new linked list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *actual;

	new = malloc(sizeof(listint_t));
	new->n = number;
	actual = *head;
	if (number < (actual->n))
	{
		new->next = actual;
		*head = new;
		return(*head);
	}
	while (number > (actual->next->n) && actual->next->next != NULL)
		actual = actual->next;
	if(actual->next->next == NULL && actual->next->n < number)
	{
		actual->next->next = new;
		new->next = NULL;
		return(*head);
	}
	new->next = actual->next;
	actual->next = new;
	return(*head);
}
