using AoC19.AdditionClasses;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AoC19.Days
{
	internal class Day2 : IAoCDay
	{
		public Day2(string filename)
		{
			StreamReader sr = new(filename);
			_opcodes = sr.ReadToEnd().Split(",").Select(x => int.Parse(x.Trim())).ToList();
		}

		public void SolveA(bool isTest)
		{
			var opcodesA = _opcodes.Select(x=>x).ToList();
			if (!isTest) {
				opcodesA[1] = 12;
				opcodesA[2] = 2;
			}
			VirtualMachine vm = new(opcodesA);
			Console.WriteLine($"Res A: {vm.Eval()}");
		}

		public void SolveB(bool isTest)
		{
			int res = 0;
			int par1 = 0;
			int par2 = 0;
			for (par1 = 0; par1 < 100 && res != 19690720; par1++)
			{
				for (par2 = 0; par2 < 100 && res != 19690720; par2++)
				{
					List<int> opcodesB = _opcodes.Select(x=>x).ToList();
					opcodesB[1] = par1;
					opcodesB[2] = par2;
					VirtualMachine vm = new(opcodesB);
					res = vm.Eval();
				}
			}
			if (par1 == 100 && par2 == 100)
			{
				Console.WriteLine("Noo waaayaaayaay");
				return;
			}
			Console.WriteLine($"Res B: {(par1-1) * 100 + (par2 - 1)}");
		}

		private readonly List<int> _opcodes;
	}
}
