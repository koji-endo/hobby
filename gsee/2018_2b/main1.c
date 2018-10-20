#include <stdio.h>
#include "stack.h"
// gcc -o main1 main1.c stack.h element.h
int main(){
	push('o');
	push('y');
	push('k');
	push('o');
	push('t');
	while(!empty_s()){
		printf("%c",pop());
	}
	return 0;
}
