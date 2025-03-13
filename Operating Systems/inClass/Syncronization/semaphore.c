#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <semaphore.h>

int fib[128];
void* fib_gen(void* param);

int main()
{
    pthread_t tid;

    int num_of_fib = 8;

    sem_init(&fib_gen, 0, 1);

    pthread_create(&tid, NULL, fib_gen, &num_of_fib);

    // pthread_join(tid, NULL);
    sem_wait(&fib_gen);

    printf("Main thread:\n");
    for(int i=0; i < num_of_fib; i++)
    {
        printf("%d\n", fib[i]);
    }

    pthread_join(tid, NULL);
    printf("Main thread: everything done.\n");
    return 0;
}

void* fib_gen(void* param)
{
    int n = *((int*)param);

    printf("worker generating fib sequence......\n");
    if(n == 0) 
    {
        pthread_exit(0);
    } 
    else if (n == 1) 
    {
        fib[0] = 0;
    } 
    else if (n == 2) 
    {
        fib[0] = 0;
        fib[1] = 1;
    } 
    else 
    {
        fib[0] = 0;
        fib[1] = 1;
        for(int i=2; i<n; i++) 
        {
            fib[i] = fib[i-1] + fib[i-2];
        }
    }
    printf("Worker finished generating fib sequence\n");
    fflush(stdout);
    sem_post(&fib_sem);

    printf("Worker is working on something else\n");
    // working on something else
    sleep(5);

}