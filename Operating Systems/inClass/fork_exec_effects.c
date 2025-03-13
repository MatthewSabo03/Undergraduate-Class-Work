#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main()
{
	if (fork() == 0) {
		execlp("/bin/uname", "uname", "-a", NULL);
		printf("Child (%d)\n", );
