#include<string.h>
#include <stdlib.h>
#include <stdbool.h>
bool isValid(char* s) {
    int n=strlen(s);
    char*stack=malloc(n*sizeof(char));
    int top=-1;
    for(int i=0;i<n;i++){
        char ch=s[i];
        if(ch=='('|| ch=='{'|| ch=='['){
            stack[++top]=ch;
        }
        else{
            if(top==-1){
                free(stack);
                return false;
            }
            char x=stack[top--];
            if(ch==')' && x!='('){
                free(stack);
                return false;
            }
            else if(ch==']'&& x!='['){
                free(stack);
                return false;

            }
            else if(ch=='}'&& x!='{'){
                free(stack);
                return false;
            }
        }
    }
if(top == -1)
{
    free(stack);
    return true;
}

free(stack);
return false;

    
}