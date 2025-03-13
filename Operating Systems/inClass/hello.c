#include <stdio.h>
#include <unistd.h>
#include <sys/syscall.h>

int main()
{
	//printf("Hello World\n");
	//write(1, "hellow  world\n", 12);
	//syscall(SYS_write, 1, "Hello World\n", 12);
	char buf[] = "Hello World\n";

	asm volatile (
			"mov $0x1, %%rax;"
			"mov $0x1, %%rdi;"
			"mov %0, %%rsi;"
			"mov $0xc, %%rdx;"
			"syscall;"
			:
			: "r" (buf)
			: "rax", "rdi", "rsi", "rdx"
		     );

	return 0;
}
