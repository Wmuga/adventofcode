using AoC19.AdditionClasses;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AoC19.Days
{
	internal class Day9 : IAoCDay
	{
		private readonly List<long> _opcodes;
		public Day9(string filename)
		{
			StreamReader sr = new(filename);
			_opcodes = sr.ReadToEnd().Split(",").Select(x => long.Parse(x.Trim())).ToList();
		}

		public void SolveA(bool isTest = false)
		{
			Console.WriteLine("Res A: ");
			var vm = PrepareVm(_opcodes.Select(x=>x).ToList());
			if (!isTest )
			{
				vm.SetInput(()=>1);
			}
			vm.Eval();
		}

		public void SolveB(bool isTest = false)
		{
			if (isTest) return;
			Console.WriteLine("Res B: ");
			var vm = PrepareVm(_opcodes.Select(x => x).ToList());
			if (!isTest)
			{
				vm.SetInput(() => 2);
			}
			vm.Eval();
		}

		private static VirtualMachine PrepareVm(List<long> opcodes)
		{
			VirtualMachine vm = new(opcodes);
			vm.ExtendInstructions();
			vm.ExtendIntructions2();
			return vm;
		}
	}
}
