/*make a copy of a text file
 * by XXX
 * last updated xxx/xx/xxx
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
	// scanf("%s", in_file);
	int tmp = syscall(SYS_read, 0, in_file, 32);
	in_file[tmp-1] = '\0';
	printf("in_file: %s\n", in_file);
	scanf("%s", out_file);

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
