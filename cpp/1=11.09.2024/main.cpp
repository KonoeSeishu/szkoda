#include <iostream>
using namespace std;

int silnia(int n)
{
    if(n<2)
    {
        return 1;
    }
    return silnia(n-1)*n;
}

int dw(int x)
{
    if(x>0)
    {
        dw(x/2);
        cout << x%2;
    }
}

int main() 
{
    int n;
    cout << "n = ";
    cin >> n;
    cout << silnia(n) << endl;
    return 0;
}