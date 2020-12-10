#include<stdio.h> 
#include<string.h> 

#define MAX 15 

struct {
    char buff[15]; 
    int bol; 
}key; 

int main(){ 
    key.bol = 0 ; 
    printf("enter a password") ; 
    scanf("%15s", key.buff) ; 
    // gets(key.buff); 
    
    if (strcmp(key.buff, "123")){ 
        printf("Wrong password")
    }
    else{
        printf("correct password"); 
        key.bol = 1; 
    }
    if (key.bol) { 
        printf("access given to the user"); 
    }
}