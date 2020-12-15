#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current, *final;
	int len = 0, i = 0, j;

	if (*head == NULL)
		return (1);
	current = *head;
	while (current)
	{
		len += 1;
		current = current->next;
	}
	current = *head;
	while (i < len / 2)
	{
		final = current;
		for (j = 0; j < len - i * 2 - 1; j++)
			final = final->next;
		if (final->n != current->n)
			return (0);
		current = current->next;
		i += 1;
	}

	return (1);
}
