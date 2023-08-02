using AoC19.AdditionClasses;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AoC19.Days
{
	internal class Day5 : IAoCDay
	{
		private readonly List<int> _opcodes;

		public Day5(string filename)
		{
			StreamReader sr = new(filename);
			_opcodes = sr.ReadToEnd().Split(",").Select(x => int.Parse(x.Trim())).ToList();
		}

		public void SolveA(bool isTest = false)
		{
			if (isTest) { return; }
			Console.WriteLine($"Res A:");
			List<int> opcodesA = _opcodes.Select(x=>x).ToList();
			VirtualMachine vm = SetUpMachine(opcodesA);
			vm.Eval();
		}

		public void SolveB(bool isTest = false)
		{
			Console.WriteLine($"Res B:");
			List<int> opcodesB = _opcodes.Select(x => x).ToList();
			VirtualMachine vm = SetUpMachine(opcodesB);
			vm.Eval();
		}

		private static VirtualMachine SetUpMachine(List<int> opcodes) {
			VirtualMachine vm = new(opcodes);
			vm.ExtendInstructions();
			return vm;
		}




	}
}
