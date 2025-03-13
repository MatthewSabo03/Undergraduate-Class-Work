/* MTSync Lab Assignment
   CISC 301-01 : Operating Systems
   Matthew Sabo
   Last Edited: 12/4/2023
*/

#include "./mtsync.h"

// total number of threads that will be sync at the fence point
int n;
// How many threads are sync now at the fence point
int counter;

sem_t mtsync_sem;
sem_t mutex_sem;

int mutex_init(int value)
{
   // Initalizes the semaphores value
   return sem_init(&mutex_sem, 0, value);
}

int mutex_lock()
{
   // locks the mutex lock
   return sem_wait(&mutex_sem);
}

int mutex_unlock()
{
   // unlocks mutex lock
   return sem_post(&mutex_sem);
}

// Initialize the MTSync fence to the specified size N.
int mtsync_fence_init(int number)
{
   counter = 0;
   n = number;
   mutex_init(1);
   sem_init(&mtsync_sem, 0, 0);

   return 0;
}

// Identify the MTSync fence.
int mtsync_fence_point(void)
{
   mutex_lock();
   counter += 1;
   if (counter == n)
   {
      sem_post(&mtsync_sem);
   }
   mutex_unlock();

   sem_wait(&mtsync_sem);
   sem_post(&mtsync_sem);

   return 0;
}