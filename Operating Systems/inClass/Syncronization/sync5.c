#include <stdio.h>
#include <unistd.h> // for sleep
#include <pthread.h>

#define TARGET 10

// shared variables
int counter;
pthread_mutex_t counter_lock;
pthread_cond_t counter_cond;

void* worker1(void*);
void* worker2(void*);

int main()
{
    pthread_t tid[2];

    counter = 0;

    pthread_mutex_init(&counter_lock, NULL);
    pthread_cond_init(&counter_cond, NULL);

    // create two threads
    pthread_create(&tid[0], 0, worker1, NULL);
    pthread_create(&tid[1], 0, worker1, NULL);

    pthread_join(tid[0], NULL);
    pthread_join(tid[1], NULL);

    pthread_mutex_destroy(&counter_lock);
    pthread_cond_destroy(&counter_cond);

    return 0;
}

void* worker1(void* param)
{
    pthread_mutex_lock(&counter_lock);

    while (counter != TARGET) {
        printf("Worker1: counter = %d, waiting ...\n", counter);
        pthread_cond_wait(&counter_cond, &counter_lock);
    }

    pthread_mutex_unlock(&counter_lock);

    printf("Worker1: Target %d is reached\n", TARGET);
    printf("Worker1: I'm done.\n");
}

void* worker2(void* param)
{
    while(1) {
        pthread_mutex_lock(&counter_lock);
        counter += 1;
        printf("Worker2: counter = %d\n", counter);
        pthread_cond_signal(&counter_cond);

        if (counter == 2 * TARGET) {
            printf("Worker2: I'm done\n");
            pthread_mutex_unlock(&counter_lock);
            break;
        /*} else if (counter == TARGET) {
            pthread_cond_signal(&counter_cond);
            pthread_mutex_unlock(&counter_lock);
            sleep(1);*/
        } else {
            pthread_mutex_unlock(&counter_lock);
            sleep(1);
        }
    }
}
