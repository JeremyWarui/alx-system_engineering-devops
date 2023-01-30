#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - create infinite loop
 * Return: 0
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - create 5 zombie processes
 * Return: infinite_while zombies
 */

int main()
{
	unsigned int i;
	pid_t child;

	for (i = 0; i < 5; i++)
	{
		child = fork();
		if (child == 0)
			exit(0);
		printf("Zombie process created, PID: %d\n", child);
	}
	return (infinite_while());
}
