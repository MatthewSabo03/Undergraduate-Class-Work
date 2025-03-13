/* Creates threads and have those threads update an integer
   By: Matthew Sabo
   Date: 11/14/2023
   CISC 301-01 */

#include <stdio.h>
#include <pthread.h>
#include <unistd.h>

// shared variables
int counter;
pthread_mutex_t mutex;

void* worker1(void*);

int main()
{
    pthread_t tid[2];

    counter = 0;

    pthread_mutex_init(&mutex, NULL);

    pthread_create(&tid[0], 0, worker1, NULL);
    pthread_create(&tid[1], 0, worker1, NULL);

    pthread_join(tid[0], NULL);
    pthread_join(tid[1], NULL);

    pthread_mutex_destroy(&mutex);

    printf("Value of counter is: %d\n", counter);
    return 0;
}

void* worker1(void*param)
{
    pthread_mutex_lock(&mutex);
    counter +=1;
    printf("Worker 1: counter = %d\n", counter);
    pthread_mutex_unlock(&mutex);
}