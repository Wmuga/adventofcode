using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Threading.Tasks;

namespace AoC19.AdditionClasses
{
    internal static class Extensions
    {
        public static (int, int) Mult(this (int, int) lhs, int rhs)
        {
            return (lhs.Item1 * rhs, lhs.Item2 * rhs);
        }

        public static (int, int) Add(this (int, int) lhs, (int, int) rhs)
        {
            return (lhs.Item1 + rhs.Item1, lhs.Item2 + rhs.Item2);
        }

        public static int[] Split(this int value)
        {
            int[] ints = new int[(int)Math.Ceiling(Math.Log10(value))];
            for (int i = ints.Length - 1; i >= 0; i--)
            {
                ints[i] = value % 10;
                value /= 10;
            }
            return ints;
        }

       public static void AddTo<TKey, T>(this Dictionary<TKey, List<T>> dict, TKey key, T value) where TKey: notnull
       {
            if (!dict.ContainsKey(key))
            {
                dict[key] = new();
            }
            dict[key].Add(value);
       }
    }
}
