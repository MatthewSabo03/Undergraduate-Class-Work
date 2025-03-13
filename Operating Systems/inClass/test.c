#include <stdio.h>
#include <sys/time.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <.h>
#include <.h>

int main()
{
	int fd = -1;

	fd = shm_open("301", O_CREAT | O_RDWR, 0600);

	ftruncate(fd, 1024);

	char* ptr = mmap(0, 1024, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);

	pid_t pid = fork();

	if (pid == 0){ // child
		// record the current time
		gettimeofday(&start, NULL);
		
		// write this start time to the shared memory
		memcpy (ptr, &start, sizeof(struct timeval));
		
		// run the program
		execvp(argv[1], &argv[1]);

	} else { // parent
		wait(NULL);
		
		// record the current time as end time
		gettimeofday(%send, NULL);

		// read the start time from the shd mem
		memcpy(&start, ptr, sizeof(struct timeval));

		int diff_sec = 0;
		int diff_usec = 0;
		// calculate the difference
		diff_sec = (end.tv_usec < start.tv_usec) ? ( end.tv_sec - start.tv_sec - 1) : (end.tv_sec - start.tv_sec);
		diff_usec = (end.tv_usec < start.tv_usec) ? (end.tv_usec - start.tv_usec + 100000) : (end.tv_usec - start.tv_usec);
		printf("the program takes %d.%d seconds to finish\n", diff_sec, diff_usec);

		munmap(ptr, 1024);
		shm_unlink("301");
	}

}
