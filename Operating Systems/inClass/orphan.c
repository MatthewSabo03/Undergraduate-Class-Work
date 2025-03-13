/* xxxx */
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main()
{
	pid_t pid;

	pid = fork();

	if (pid < 0)
	{
		printf("fork() error\n");
		return -1;
	} 
	
	else if (pid == 0) 
	{
		sleep(60); // child become an orphan after 10 sec
		return 0;
	} 
	
	else 
	{
		sleep(10);
		printf("parent exiting\n");
       		return 0;	       
	}
}
