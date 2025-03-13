/* Creates a Zombie process
 * by Matthew Sabo
 * last updated 10/2/2023
 * CISC 301*/
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>

int main()
{
	pid_t child_pid;

	child_pid = fork();

	// parent process
	if (child_pid > 0) 
	{
		sleep(60);
	}
	// child process
	else
	{
		exit(0);
	}
	return 0;
}
