#include <iostream>
#include <stack>
using namespace std;

int main()
{
    stack<int> stos;
    stos.push(2);
    stos.push(4);
    stos.push(5);
    stos.push(1);
    stos.push(8);

    for(int i=0;i<stos.size();i++)
    {
        cout<<stos.top()<<" ";
        stos.pop();
        if(stos.empty())cout<<"stos end";
    }
    return 0;
}