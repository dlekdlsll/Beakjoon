#include <stdio.h>

int main()
{	
	unsigned long long A;
	unsigned long long B;
	
	scanf_s("%llu %llu", &A, &B);
	printf("%llu", A+B);

	return 0;
}
