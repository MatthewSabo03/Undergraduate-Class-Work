// Lab 6 - Multithreading 
// Problem 1: Multithreaded Statistical Calculation 
// CISC 301
// Matthew Sabo
// Last Edited : 10/18/2023

#include <stdio.h>
#include <sys/types.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>

void* average(void* arr)
{
    int sum, i;

    for(i=0; i<2; i++)
    {
        sum = sum + arr[i];
    }

    float avg = (float)sum / i;
    printf("The average value is: %.2f\n", avg);
}

void* larger(void* arr)
{
    int max = 0;

    for(int i= ; i<2; i++)
    {
        if(arr[i] > max)
        {
            max = arr[i];
        }
    }
    printf("The largest value is: %d\n", max);
}

void* smaller(void* arr)
{
    int min = arr[0];

    for(int i=1; i<2; i++)
    {
        if(arr[i] < min)
        {
            min = arr[i];
        }
    }
    printf("The smallest value is: %d\n", min);
}


int main()
{
	pthread_t thread_ids[3];

    int nums[2] = {89, 91};
	// create 3 threads and have each of them 
	pthread_create(&(thread_ids[1]), NULL, average, nums);
    pthread_create(&(thread_ids[2]), NULL, larger, nums);
    pthread_create(&(thread_ids[3]), NULL, smaller, nums);

    // wait for them to complete
	for (int i=0; i<3; i++)
	{
		pthread_join(thread_ids[i], NULL);
	}

	return 0;
}

void* average(void* arr)
{
    int sum, i;

    for(i=0; i<2; i++)
    {
        sum = sum + arr[i];
    }

    float avg = (float)sum / i;
    printf("The average value is: %.2f\n", avg);
}

void* larger(void* arr)
{
    int max = arr[0];

    for(int i=1; i<2; i++)
    {
        if(arr[i] > max)
        {
            max = arr[i];
        }
    }
    printf("The largest value is: %d\n", max);
}

void* smaller(void* arr)
{
    int min = arr[0];

    for(int i=1; i<2; i++)
    {
        if(arr[i] < min)
        {
            min = arr[i];
        }
    }
    printf("The smallest value is: %d\n", min);
}
