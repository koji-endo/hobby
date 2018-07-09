#include <stdio.h>
#include <stdlib.h>

//qsortの比較用関数
int asc(const void *a, const void *b) {
	return *(int *)a - *(int *)b;
}
//csv読み込み関数
int read_csv(char* filename){
	FILE *fp;
	char readline[256] = {'\0'};
	if ((fp = fopen(filename, "r")) == NULL) {
        fprintf(stderr, "%sのオープンに失敗しました.\n", filename);
        exit(EXIT_FAILURE);
    }

    /* ファイルの終端まで文字を読み取り表示する */
    while ( fgets(readline, 256, fp) != NULL ) {
        printf("%s", readline);
    }

    /* ファイルのクローズ */
    fclose(fp);
    return 0;
}


int main() {
    char *filename = "connect.txt";
    read_csv(filename);


	int a[] = {2, 3, 1};
	qsort(a, sizeof(a) / sizeof(int), sizeof(int), asc);
	printf("%d%d%d", a[0], a[1], a[2]); // "123"
}