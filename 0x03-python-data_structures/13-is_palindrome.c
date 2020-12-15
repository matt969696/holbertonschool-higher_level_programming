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
	listint_t *current;
	int tab[4096];
	int i = 0, j = 0;

	if (*head == NULL)
		return (1);

	current = *head;
	while (current)
	{
		tab[i] = current->n;
		current = current->next;
		i += 1;
	}

	while (j < i / 2)
	{
		if (tab[j] != tab[i - 1 - j])
			return (0);
		j += 1;
	}

	return (1);
}
