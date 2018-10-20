#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Student{
	char name[256];
	int score;
};

struct Student* high_score(struct Student *arg_test){
	struct Student *p;
	int tmp=0;
	int highest=0;
	for (int i=0; i<6;i++){
		if((arg_test[i]).score>tmp){
			tmp=(arg_test[i]).score;
			highest=i;
		}
	}
	p=&(arg_test[highest]);
	return p;
}
int main(void){
	struct Student test[6]=
	{{"Aki",10},{"Akj",20},{"Akk",30},
	{"Akl",20},{"Akm",10},{"Akn",15}};
	struct Student *top;
	top=high_score(test);
	printf("%s %d\n",top->name,top->score);
}
