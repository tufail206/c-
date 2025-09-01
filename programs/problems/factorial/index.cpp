#include<iostream>
using namespace std;
int main(){

    int fact=1,x;
    cout<<"enter the number to find factorial : ";
    cin>>x;
    for(int i=1;i<=x;i++){
        fact=fact*i;
    }
    cout<<"Factorial of "<<x<<" = "<<fact;
   
}



