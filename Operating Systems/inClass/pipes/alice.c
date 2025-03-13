// **** //

#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

int main()
{
	int fd = -1;
	char recv_buf[128];
	char send_buf[128];

	mkfifo("/tmp/my-pipe-301", 0600);
	
	while(1)
	{
		open("/tmp/my-pipe-301", O_RDONLY);
		read(fd, recv_buf, 128);
		close(fd);
		printf("Bob says: %s\n", recv_buf);

		fgets(send_buf, 128, stdin);
		fd = open("/tmp/my-pipe-301", O_WRONLY);
		write(fd, send_buf, 128);
		close(fd);
	}
}
