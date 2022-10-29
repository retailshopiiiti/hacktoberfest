#include <stdio.h>
#include <stdlib.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <unistd.h>
#include <sys/wait.h>

void main()
{
    key_t key = 100;
    int size = sizeof(int);
    int *ptr = NULL;
    int shmid = shmget(key, size, 0666|IPC_CREAT);
    ptr = shmat(shmid, NULL, 0);
    *ptr = 0;
    int process1_id, process2_id;
		
    process1_id = fork();
    if(process1_id == 0)
		{
        int *a_ptr = shmat(shmid, NULL, 0);
        for(int i=0;i<100000;i++)
				{
            (*a_ptr)= (*a_ptr) + 1;
        }
        shmdt(a_ptr);
    } 
		else
		{
					process2_id = fork();
					if(process2_id == 0)
		 			{
							int *b_ptr = shmat(shmid, NULL, 0);
							for(int i=0;i<100000;i++)
			 				{
									(*b_ptr)= (*b_ptr) - 1;
							}
							shmdt(b_ptr);
					}
			}

    sleep(1);
    if(process1_id>0 && process2_id>0)
		{
        printf("X = %d\n",*ptr);
        shmdt(ptr);
        shmctl(shmid, IPC_RMID, NULL);
    }
}
