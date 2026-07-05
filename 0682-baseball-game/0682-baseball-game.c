#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int calPoints(char** operations, int operationsSize) {
    int n=operationsSize;
    int *record=malloc(n*sizeof(int));
    int top=-1;
    int sum=0;
    for(int i=0;i<n;i++){
        if(strcmp(operations[i],"C")==0){
            
            top--;


        }
        else if(strcmp(operations[i],"D")==0){
            
            int x=record[top];
            
            record[++top]=x*2;


        }
        else if(strcmp(operations[i],"+")==0){
            
            int a=record[top];
            int b=record[top-1];
            int c=a+b;
            record[++top]=c;


        }
        else{
            record[++top]=atoi(operations[i]);
        }


    }
    for(int j=0;j<=top;j++){
        sum+=record[j];
    }
    return sum;
    
}