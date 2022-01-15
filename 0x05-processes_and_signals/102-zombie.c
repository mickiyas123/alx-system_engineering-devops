#include<stdio.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * main - creates 5 zombie processes
 *
 * Return: Always Success
 */
int main()
{
	int i;
	for (i=0; i<5; i++)
	{
		pid_t child_pid = fork();

		if (child_pid > 0)
			printf("Zombie process created, PID: %d", child_pid);
	}
}
/**
 * infinite_while - while loop
 */

int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}
