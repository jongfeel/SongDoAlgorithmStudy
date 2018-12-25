#include <iostream>
#include <string>

using namespace std;

bool solution(string s)
{
    int checkPair = 0;
    for (int i=0; i<s.length(); i++)
    {
        if (s[i] == '(')
            checkPair++;
        else if (s[i] == ')')
            checkPair--;
        
        if (checkPair < 0)
            return false;
    }

    return checkPair == 0 ? true : false;
}

int main() 
{
    int input;

    cout << boolalpha << solution("()()") << endl;
    
    cout << "To end of program, input any character and enter...";
    cin >> input;
    return 0;
}