#include <iostream>
using namespace std;
int main()
{
   int num,result=0;
   cout<<"enter a number : ";
   cin>>num;
   for(int i=0;i<=num;i++){
    result+=i;
   }
   cout<<"result : "<<result;
   
}