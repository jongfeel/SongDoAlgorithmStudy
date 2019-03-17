using System;
using System.Collections.Generic;
using System.Linq;

namespace Programmers
{
    class Program
    {
        public static int[] solution(string[] genres, int[] plays) {
            List<int> answer = new List<int>();
            
            Dictionary<int, KeyValuePair<string, int>> bestDic = new Dictionary<int, KeyValuePair<string, int>>();
            
            for (int i=0; i<genres.Length; i++)
            {
                bestDic.Add(i, new KeyValuePair<string, int>(genres[i], plays[i]));
            }
            // [ {"classic", 1450}, {"pop", 3100}]
            var groupByGenresDic = bestDic.Values.GroupBy(g => g.Key).ToDictionary(k => k.Key, v => v.Sum(vv => vv.Value)).OrderByDescending(o => o.Value);
            
            foreach (var item in groupByGenresDic)
            {
                // [{4, {"pop", 2500}}, {1, {"pop", 600}}, ...]
                var generesIndexDic = bestDic.Where(w => w.Value.Key == item.Key).OrderByDescending(o => o.Value.Value).Take(2);
                foreach (var item2 in generesIndexDic)
                {
                    // Console.WriteLine(item2.Key);
                    answer.Add(item2.Key);
                }
            }
            
            return answer.ToArray();
        }
        static void Main(string[] args)
        {
            Console.WriteLine(string.Join(",", solution(new string[] { "classic", "pop", "classic", "classic", "pop" },
                                        new int[] { 500, 600, 150, 800, 2500 })));
        }
    }
}
