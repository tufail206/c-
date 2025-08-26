#include<iostream>
#include<string>
using namespace std;

class Teacher {
   string name;
   string dep;
   string course;
   int age;
   int id;
   public:
   void setTeacherData(string n,string d,string c, int a,int i){
    name=n;
     dep=d;
     course=c;
     age=a;
     id=i;
   }

   string displayData(){
  cout<< name;
   }

};


int main(){
// Teacher t1;
// t1.setTeacherData("zain","computer","DSA",30,1234);
// cout<<t1.displayData();

Teacher *t=new Teacher;
t->setTeacherData("zain","dh","course",23,5);
t->displayData();


}