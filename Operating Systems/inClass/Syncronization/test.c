/* create a number of threads and 
 * get them increament a globale(shared)
 * integer variable and print out results
 * Oct 20, 2023 */

#include <stdio.h>
#include <sys/types.h>
#include <pthread.h>

#define NUM_THREADS 100

int x = 0;

pthread_mutex_t lock;

void* worker(void * i)
{
    int temp;

    // protect cs
    
}