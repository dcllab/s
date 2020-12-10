//#include <stdio.h>
//#include <string.h>
//#define MAX 15 int main(void)
//struct {
//
//	char buff[15];
//	int pass;
//
//}key;
//void main(){
//	key.pass=0;
//	printf("\n Enter the password : \n");
//	gets(key.buff);
//	if(strcmp(key.buff, "sabrish"))
//	{
//		printf ("\n Wrong Password \n");
//	}
//	else
//	{
//		printf ("\n Correct Password \n");
//		key.pass = 1;
//	}
//	if(key.pass)
//	{
//		printf ("\n Wrong password \n");
//	}
//
//}
//
//
//

#include <stdio.h>
#include <string.h>
#define MAX 15 int main(void)
struct {
	char buff[15];
	int pass;
}key;
void main(){
	key.pass=0;
	printf("\n Enter the password : \n");
//	gets(key.buff);
	scanf("%s",&key.buff);
	if(strcmp(key.buff, "t"))
	{
		printf ("\n Wrong Password \n");
	}
	else
	{
		printf ("\n Correct Password \n");
		key.pass = 1;
	}
	if(key.pass)
	{
	printf ("\n Root privileges given to the user \n");
	}
}

