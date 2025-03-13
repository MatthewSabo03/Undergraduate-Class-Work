#include <stdio.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/types.h>

int main()
{
	char NAME[] = "shared_memory";

	int fd = shm_open(NAME, O_CREAT | O_EXCL | O_RDWR, 0600);

	ftruncate(fd, 1024);

	char *ptr = mmap(0, 1024, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);

	sprintf(ptr, "%s", "Hello, world");

	sleep(10);

	munmap(ptr, 1024);

	shm_unlink(NAME);
	
	return 0;

}
