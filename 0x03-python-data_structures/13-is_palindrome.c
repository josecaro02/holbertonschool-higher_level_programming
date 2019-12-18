#include "lists.h"

/**
 *is_palindrome - checks if a linked list is palindrome
 *@head: head of the linked list
 *
 *Return: 1 if it's palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	size_t len_list, zero_len, i, count_len;
	listint_t *end_list, *beg_list;

	if (head == NULL)
		return (0);
	if (*head)
	{
		len_list = zero_len = 0;
		end_list = beg_list = *head;
		while (beg_list != NULL)
		{
			beg_list = beg_list->next;
			len_list++;
		}
		beg_list = *head;
		count_len = len_list = len_list - 1;
		while (count_len > zero_len)
		{
			end_list = beg_list = *head;
			for (i = 0; i < count_len; i++)
				end_list = end_list->next;
			for (i = 0; i < zero_len; i++)
				beg_list = beg_list->next;
			count_len--;
			zero_len++;
			if (end_list->n != beg_list->n)
				return (0);
		}
		return (1);
	}
	else
		return (1);
}
