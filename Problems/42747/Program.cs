using System;
using System.Linq;

namespace Programmers
{
    class Program
    {
        public static int solution(int[] citations)
        {
            for (int i=0; i<=10000; i++)
            {
                if (citations.Where(c => c > i).Count() <= i)
                {
                    return i;
                }
            }
            return 0;
        }
        static void Main(string[] args)
        {
            Console.WriteLine(solution(new int[] { 3, 0, 6, 1, 5 }));
        }
    }
}
