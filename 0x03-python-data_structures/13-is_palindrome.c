#include "lists.h"

/**
 *listint_len - return the size of the linked list
 *@h: linked list
 *
 *Return: size of elements
 */

size_t listint_len(const listint_t *h)
{
	size_t n;

	n = 0;
	while (h != NULL)
	{
		h = h->next;
		n++;
	}
	return (n);
}

/**
 *is_palindrome - checks if a linked list is palindrome
 *@head: head of the linked list
 *
 *Return: 1 if it's palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	size_t len_list, zero_len, i, count_len;
	listint_t *end_list, *beg_list, *zero_list;

	if (*head)
	{
		zero_len = 0;
		count_len = len_list = listint_len(*head) - 1;
		end_list = beg_list = zero_list = *head;
		while (count_len > zero_len)
		{
			for (i = 0; i < count_len; i++)
				end_list = end_list->next;
			for (i = 0; i < zero_len; i++)
				beg_list = beg_list->next;
			count_len--;
			zero_len++;
			if (end_list->n != beg_list->n)
				return (0);
			end_list = zero_list;
			beg_list = zero_list;
		}
		return (1);
	}
	else
		return (0);
}
