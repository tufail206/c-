#include <iostream>
using namespace std;
int main()
{

    // first=0 second =1 third=first+second
    int first=0, second =1,  n,sum=0,current;
    cout<<"enter number to find fibonacci : ";
    cin>>n;
    for(int i=0;i<=n;i++){
 
     current=first+second;
     second = first;
     first = current;
     sum = first + second;
    }
    cout<<sum;

}