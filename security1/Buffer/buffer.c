#include <stdio.h>
#include <string.h>
#define MAX 15 

struct {
    char buff[15];
    int pass;
} key;


int main() {

   key.pass = 0;
   printf("Enter the password : ");
//    gets(key.buff);
   scanf("%15s", key.buff);
   if (strcmp(key.buff, "123")) {
       printf("Wrong Password \n");
      
   }
   else {
       printf("Correct Password\n");
       key.pass = 1;
   }
   if (key.pass)
       printf("Root privileges given to the user\n");
   return 0;
}
