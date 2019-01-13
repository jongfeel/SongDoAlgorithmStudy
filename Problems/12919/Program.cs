using System;

namespace _12919
{
    class Program
    {
        public static string solution(string[] seoul) {
            return $"김서방은 {Array.FindIndex(seoul, s => s == "Kim")}에 있다";
        }
        static void Main(string[] args)
        {
            Console.WriteLine(solution(new string[] { "Jane", "Kim" }));
        }
    }
}
