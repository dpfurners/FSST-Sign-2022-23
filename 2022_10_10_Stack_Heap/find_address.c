/*
Address management in C
Daniel Pfurner
Oct.22
*/


#include <stdio.h>
#include <stdlib.h>

#define heap 10
//#define heap2 12
//#define heap3 13

int function(int countdown){
    int saved = 22;
    if (countdown == 10){
        printf("The STACK is located at: %p\n", (void *)&saved);
    }else if (countdown == 0){
        return saved;
    }else {
        // To display other stack addresses to check if the address is getting smaller
        //printf("%p\n", (void *)&saved);
    }
    countdown --;
    return function(countdown);
}

int main(){
    printf("Main function (code) is located at: %p\n", (void *)&main);
    printf("The HEAP is located at: %p\n", (void *)heap);
    //printf("The HEAP is located at: %p\n", (void *)heap2);
    //printf("The HEAP is located at: %p\n", (void *)heap3);
    int stack = function(10);
    int addr = (int)((int *)&stack - (int *)heap);
    printf("There are %d Addresses (ca. %d GB) to give away in the STACK and the HEAP...\n", addr, addr/1000000);
}