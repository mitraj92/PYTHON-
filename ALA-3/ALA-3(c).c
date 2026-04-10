#include<stdio.h>
int main(){
 int n=121, orig, rev=0, rem;
 orig = n;
 while(n != 0){
 rem = n % 10;
 rev = rev*10 + rem;
 n = n/10;
 }
 if(orig == rev)
 printf("Palindrome\n");
 else
 printf("Not Palindrome\n");
 return 0;
}
