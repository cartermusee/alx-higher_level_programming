#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - function checks if list is cyclical
 * @list: pointer to list to check
 * Return: 1 cyclical, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *s = list, *f = list;

	while (f && f->next)
	{
		s = s->next;
		f = f->next->next;
		if (s == f)
			return (1);
	}
	return (0);
}
