#include <iostream>
using namespace std;
int main(){

    int number, factor=0;
    cout<<"enter number to check prime or not : ";
    cin>>number;

    for(int i=2;i<=(number/2);i++){
        if(number==1){
            cout<<number<<" is not prime ";
        }
        if(number%i==0){
            factor++;
        }
    }
    if(factor>0){
        cout<<number << " is number is not a prime";
    }else{
        cout<<number << " is number is  a prime";
    }

}