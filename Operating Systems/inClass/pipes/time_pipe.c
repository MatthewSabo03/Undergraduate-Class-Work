// **** //

#include <stdio.h>
#include <sys/time.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>


int main(int argc, char** argv)
{
	int fd[2];
	pid_t pid;

	struct timeval start;
	struct timeval end;

	// create a pipe
	pipe(fd);

	// fork a child
	pid = fork();

	if (pid == 0) 
	{
		// child process

		// record current time
		gettimeofday(&start, NULL);

		// write start time to the pipe
		write(fd[1], &start, sizeof(struct timeval));

		// run the program
		execvp(argv[1], &argv[1]);
	} 
	else 
	{
		// parent process
		
		// wait for my child
		wait (NULL);

		// record current time
		gettimeofday(&end, NULL);

		// read the start time from the pipe
		read(fd[0], &start, sizeof(struct timeval));

		// compute time difference
		int sec_diff;
		int usec_diff;

		sec_diff = end.tv_sec - start.tv_sec;
		usec_diff = end.tv_usec - start.tv_usec;

		printf("time elapsed: %d.%d\n", sec_diff, usec_diff);

		close(fd[0]);
		close(fd[1]);
	}
}
