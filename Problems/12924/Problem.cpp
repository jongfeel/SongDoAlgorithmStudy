#include <iostream>
using namespace std;

int solution(int n) {
    int answer = 0;
    
    int sum = 0;
    for (int i=1; i<=n; i++)
    {
        for (int j=i; j<=n; j++)
        {
            //std::cout << j;
            sum += j;
            if (sum == n)
            {
                answer++;
                break;
            }
            else if (sum > n)
            {
                break;
            }
        }
        sum = 0;
    }
    return answer;
}

int main() 
{
    cout << solution(15) << endl;
    
    return 0;
}