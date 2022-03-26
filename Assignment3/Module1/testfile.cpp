#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int a = 3;
    int b = 4;
    bool f = true;
    
    if(a<b)
    {
        if(f == false && b == 4)
        {
            if(a == 3)
            {
                cout<<"Hi\n";
            }
            else if(a == 2 || a == 1)
            {
                cout<<"Hello\n";
            }
            else
            {
                cout<<"Bye\n";
            }
        }
    }
    else if (a>b) cout<<"Bigger\n";
    // reassign a
    /* for my sake
     * and not for others sake*/
     
    a = 6;
    cin >> b;
    if (a<b) cout<<"Nooo\n";
    else cout<<"YAYY\n";
}