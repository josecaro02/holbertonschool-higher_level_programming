#include "lists.h"

/**
 *check_cycle - finds if a linked list has a loop
 *@head: head of the linked list
 *
 *Return: 1 if there is a cycle, 0 if not
 */
int check_cycle(listint_t *head)
{
	int *add_a, *add_b;

	if (head == NULL)
		return (0);
	while (head != NULL)
	{
		add_a = (int *)&head;
		add_b = (int *)&head->next;
		if (head->next == NULL)
			return (0);
		if (add_a[0] - add_b[0] <= 0)
		{
			return (1);
		}
		head = head->next;
	}
	return (0);
}
