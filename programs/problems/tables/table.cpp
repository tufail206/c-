#include <iostream>
using namespace std;
int main()
{
    int x,range;
    cout<<"enter the number whose table want to generate : ";
    cin>>x;
    cout << "enter the range    : ";
    cin >> range;

    for(int i=1;i<=range;i++){
        cout<<x<<" * "<<i<<" = "<< x*i<<endl;
    }
}