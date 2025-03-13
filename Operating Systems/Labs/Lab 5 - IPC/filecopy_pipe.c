// In class example of the Lab
// File copy using ordinary pipe

#include <stdio.h>
#include <sys/types.h> // pid_t
#include <sys/wait.h> // wait()
#include <stdlib.h>

#define READ 0
#define WRITE 1

int main()
{
    // can either use parameters or scanf
    // will use scanf for this example

    FILE* in;
    FILE* out;
    char in_filename[64];
    char out_filename[64];

    int c;
    char r_buf;

    pid_t pid;

    int fd[2];

    // get user input
    printf("input filename:\n");
    scanf("%s", in_filename);
    printf("output filename:\n");
    scanf("%s", out_filename);

    // create the pipe
    if (pipe(fd) < 0)
    {
        printf("pipe error\n");
        return -1;
    }

    pid = fork();
    if (pid == 0)
    {
        //child process first close the read end
        close(fd[READ]); 

        // open the input text file
        in = fopen(in_filename, "r");

        // read the input text file and write into the pipe
        while ((c = getc(in)) != EOF)
        {
            //should not use putc()
            write(fd[WRITE], (char*)&c, sizeof(char));
        }

        // close the input text file
        fclose(in);

        // close the write end of the pipe
        close(fd[WRITE]);

        exit(0);
    }
    else
    {
        // parent process first close the write end
        close(fd[WRITE]);

        // open the text file
        fopen(out_filename, "w");

        // read from the pipe and write into the output text file
        while(read(fd[READ], %r_buf, 1) > 0) 
        {
            putc(r_buf, out);
        }

        // clean up
        fclose(out);
        close(fd[READ]);

        wait(NULL);

        exit(0);
    }
}