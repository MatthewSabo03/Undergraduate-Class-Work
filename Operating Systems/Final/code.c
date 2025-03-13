#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdio.h>

int x =0;
int y=0;

int main()
{
    int fd[2];
    pid_t pid;

    pipe(fd);
    pid = fork();

    if (pid==0)
    {
        read(fd[0], &y, sizeof(int));
        close(fd[0]);

        x = x+1;

        write(fd[1], &x, sizeof(int));
        close(fd[1]);

        printf("child: %d, %d\n", x, y);
    } else {
        x+=1;
        write(fd[1], &x, sizeof(int));
        close(fd[1]);

        wait(NULL);

        read(fd[0], &y, sizeof(int));
        close(fd[0]);

        printf("parent: %d, %d\n", x, y);
    }
}