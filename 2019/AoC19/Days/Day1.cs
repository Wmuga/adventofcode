using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AoC19.Days
{
	internal class Day1 : IAoCDay
	{
		public Day1(string filename)
		{
			StreamReader sr = new(filename);
			_modules = sr.ReadToEnd().Split("\n").Select(x => int.Parse(x.Trim())).ToList();
		}
		public void SolveA(bool isTest)
		{
			Console.WriteLine(_modules.Select(x=> x / 3 - 2).Sum());
		}

		public void SolveB(bool isTest)
		{
			long count = 0;
			_modules.ForEach(x => {
				while(x > 5)
				{
					x = x / 3 - 2;
					count += x;
				}
			});
			Console.WriteLine(count);
		}

		private readonly List<int> _modules;
	}
}
