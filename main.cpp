# include<iostream>

using namespace std;

int main(){
    char a[5];
    a[0] = '1';
    int ia = a[0] - '0';
/* note that the int cast is not necessary -- int ia = a would suffice */
    cout<<ia<<endl;
}