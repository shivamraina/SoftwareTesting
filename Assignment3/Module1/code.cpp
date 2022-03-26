#include <iostream>
#include <vector>
#include <fstream>
#include <cstdlib>

using namespace std;

int countop(string text)
{
    int c = 1;
    for(int i=0;i<text.length()-1;i++)
    {
        if((text[i]=='&' && text[i+1]=='&') || (text[i]=='|' && text[i+1]=='|'))
        {
            c++;
        }
    }
    return c;
}

int main()
{
    ifstream indata;
    indata.open("C:\\Users\\srain\\Desktop\\Software Testing\\Assignment3\\Module1\\testfile.cpp");
    
    if(!indata)
    {
        cerr<<"Error: file could not be opened\n"<<endl;
        exit(1);
    }
    
    string text;
    int ans = 0;
    
    while(getline(indata, text))
    {
        int loc = text.find("if");
        if(loc == string::npos) continue;
        
        ans+=countop(text.substr(loc));
    }

    cout<<ans+1<<endl;
    indata.close();
    return 0;
}