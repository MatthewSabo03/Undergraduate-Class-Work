#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdlib.h>

int a = 0;

int main()
{
	pid_t pid;
	pid = fork();

	if (pid < 0){ 
		printf("fork() failed\n");
		return -1;
	} else if (pid ==0) {
		printf("Child (%d): a = %d\n", getpid(), a);
		a = 1;
		printf("Child (%d): a = %d\n", getpid(), a);
	} else {
		printf("Parent (%d): a = %d\n", getpid(), a);
		wait(NULL);
		printf("");
		printf("Parent (%d): a = %d\n", getpid(), a);
