#include <pthread.h>
#include <stdio.h>

void* worker(void* parameter); // the thread worker function

int main()
{
	pthread_t thread_ids[10];
	int names[10];

	// create 10 threads and have each of them show their name
	for (int i = 0; i < 10; i++)
	{
		names[i] = i;
		pthread_create(&(thread_ids[i]), NULL, worker, &(names[i]));
	}

	// wait for them to complete
	for (int i = 0; i < 10; i++)
	{
		pthread_join(thread_ids[i], NULL);
	}

	// main thread done
	printf("Main thread done.\n");

	return 0;
}

void* worker(void* parameters)
{
	int my_name = *((int*)parameters);

	printf("My name is: %d\n", my_name);
}
