#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <wait.h>
#include <pthread.h>

int value = 0;
void *runner(void* param);

int main()
{
	pid_t pid;
	pthread_t tid;
	pid = fork();
	if (pid == 0){
		pthread_create(&tid, NULL, runner, NULL);
		pthread_join(tid, NULL);
		printf("%d\n", value);
	} else if (pid>0) {
		wait(NULL);
		printf("%d\n", value);
	}
}

void *runner(void* param){
	value = 5;
	pthread_exit(0);
}
