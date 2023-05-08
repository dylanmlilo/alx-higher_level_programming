#include "lists.h"

/**
 * check_cycle - function that checks if a linked list contains a cycle
 *
 * @list: the linked list to check
 *
 * Return: 0 if there is no cycle, 1 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *head = list, *tail = list;

	if (!list || !list->next)
	{
		return (0);
	}

	while (head && tail && tail->next)
	{
		head = head->next;
		tail = tail->next->next;

		if (head == tail)
		{
			return (1);
		}
	}
	return (0);
}
