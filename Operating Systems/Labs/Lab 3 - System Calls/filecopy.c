/*makes a copy of a text file
 * by Matthew Sabo
 * last updated 09/21/2023
 * CISC 301*/

#include <stdio.h>
#include <unistd.h>
#include <sys/syscall.h>

int main()
{
	FILE* in;
	FILE* out;
	char in_file[32];
	char out_file[32];
	int c;

	// get input from users about the files to copy
	scanf("%s", in_file);
	printf("in_file: %s\n", in_file);
	scanf("%s", out_file);
	
	// checks if file the source file exists
	// if it doesn't then it prints out an error message and ends the program 
	if (access(in_file, F_OK) != 0)
	{
		printf("Invalid source file\n");
		return 1;
	}
	else
	{
		// open files
		in = fopen(in_file, "r");
		out = fopen(out_file, "w");
		
		// keep reading from the src file and write into the dst file
		c = getc(in);
		while (c != EOF)
		{
			putc(c, out);
			c = getc(in);
		}
		
		// close files
		fclose(in);
		fclose(out);

		return 0;
	}	

}
