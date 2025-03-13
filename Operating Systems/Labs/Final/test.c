/*
 * MTSync -- test driver -- Fall 2023
 *
 * by DY
 *
 * compile and link:
 *     gcc mtsync.c test.c -lpthread -fcommon
 *
 * run:
 *     ./a.out <number of threads>
 *
 * Last Update: Nov 14, 2023
 *
 * * */

// headers
#include <stdio.h>
#include <stdlib.h> // for rand()
#include <unistd.h> // for sleep()
#include <sys/time.h> // for srand() and rand()
#include <pthread.h> // for testing driver

#include "./mtsync.h" // <<<<<< include our library

/* worker function */
void *worker(void *arg);

int main(int argc, char** argv)
{
	int i;
	int num_threads;

	srand(time(NULL)); // for mimicing doing something

	if (argc != 2) {
		printf("usage: ./a.out <number of threads>\n");
		return -1;
	}
	num_threads = atoi(argv[1]);
	printf("%d threads will be waiting at the mtsync fence point\n", num_threads);

	pthread_t workers[num_threads];
	int worker_IDs[num_threads];
	
	// initialize the fence point
	mtsync_fence_init(num_threads);

	// create threads and let them run worker()
	for (i = 0; i < num_threads; i++) {
		worker_IDs[i] = i + 1;
		pthread_create(&workers[i], 0, worker, &(worker_IDs[i]) );
	}

	for (i = 0; i < num_threads; i++) {
		pthread_join(workers[i], 0);
	}
	
	printf("main thread: all done!\n");

	return 0;
}

void* worker(void* arg)
{
	int my_id = *((int*)arg);
	struct timeval time_stamp;
	int workload = (rand() % 23 + 1);

	gettimeofday(&time_stamp,NULL);
	printf("worker [%2d] is working on sth for [%2d] sec from [%ld] \n",
			my_id, workload, time_stamp.tv_sec);
	sleep(workload);

	// reach the fence point
	gettimeofday(&time_stamp,NULL);
	printf("worker [%2d] reached the mtsync fence point at [%ld]\n",
			my_id, time_stamp.tv_sec);
	// sync here
	mtsync_fence_point();

	gettimeofday(&time_stamp, NULL);
	printf("worker [%2d] completes at [%ld]\n", my_id, time_stamp.tv_sec);

	pthread_exit(0);
}
