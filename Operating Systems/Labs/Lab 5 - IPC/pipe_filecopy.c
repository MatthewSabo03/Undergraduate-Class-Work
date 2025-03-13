// CISC 301
// Matthew Sabo
// 10/10/2023

#include <stdio.h>
#include <unistd.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <fcntl.h>
#include <sys/syscall.h>
#include <string.h>
#include <stdlib.h>
#include <sys/wait.h>

int main(int argc, char** argv)
{
	FILE* in;
	FILE* out;
	int fd[2];
	pid_t pid;
	char buf[128];
	int size = 50;
	
	// create a pipe
	pipe(fd);

	// fork a child
	pid = fork();

	int in_file = open(argv[1], 0);
	int out_file = open(argv[2], O_RDWR | O_CREAT | O_APPEND, 0600);

	if (pid == 0)
	{
		// child process

		close(fd[1]);
		
		while (read(in_file, buf, sizeof(buf)) > 0 )
		{
			write(out_file, buf, strlen(buf) - 1 );
		}
		close(fd[0]);
		close(out_file);
	}	
	else
	{
		close(fd[0]);
		while (read(in_file, buf, sizeof(buf)) > 0 )
		{
			write(fd[1], buf, sizeof(buf));
			memset(buf, 0, size);
		}
		close(fd[1]);
		close(in_file);
		wait(NULL);
	}

}
