#include<stdio.h> 
#include<string.h> 
#define MAX 15  

struct { 
    char buff[15] ; 
    int pass; 
}key; 

int main(){
    key.pass = 0 ; 
    printf("enter pass : ") ;
    scanf("%15s",key.buff);
    // gets(key.buff)

    if (strcmp(key.buff,"123")){
        printf("Wrong pass") ; 
        key.pass = 0 ; 
    }
    else{ 
        printf("Right passs") ; 
        key.pass = 1 ; 
    }

    if (key.pass){
        printf("rootprivilages given");
    }
    return 0 ;
}