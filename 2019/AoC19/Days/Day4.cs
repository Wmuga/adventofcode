using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using AoC19.AdditionClasses;

namespace AoC19.Days
{
    internal class Day4 : IAoCDay
	{
		public Day4(string input)
		{
			if (input.Length == 0) return;
			var ar = input.Split('-').Select(x => int.Parse(x)).ToArray();
			_range = Enumerable.Range(ar[0], ar[1] - ar[0]);
			_pa = (x =>
			{
				bool isDouble = false;
				var digs = x.Split();
				for (int i = 1; i < digs.Length; i++)
				{
					if (digs[i] < digs[i - 1]) return false;
					if (digs[i] == digs[i - 1]) isDouble = true;
				}
				return isDouble;
			});
		}

		private int Solve(Predicate<int> func)
		{
			return _range.Where(x => func(x)).Count();
		}

		public void SolveA(bool isTest = false)
		{
			if (isTest) { return; }
			
			int res = Solve(_pa);
			Console.WriteLine($"Part A: {res}");
		}

		public void SolveB(bool isTest = false)
		{
			if (isTest) { return; }
			int res = Solve((x =>
			{
				if (!_pa(x)) return false;
				var digs = x.Split();
				int prev = digs[0];
				bool isDouble = false;
				bool curDouble = false;
				bool curMult = false;

				for (int i = 1; i < digs.Length; i++)
				{
					if (digs[i] == prev)
					{
						if (curMult) continue;
						if (curDouble)
						{
							curDouble = false;
							curMult = true;
							continue;
						}
						curDouble = true;
						continue;
					}
					prev = digs[i];
					curMult = false;
					isDouble |= curDouble;
				}
				return isDouble | curDouble;
			}));

			Console.WriteLine($"Solve B: {res}");
		}

		private Predicate<int> _pa;
		private IEnumerable<int> _range;
	}
}
