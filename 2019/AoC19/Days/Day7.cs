using AoC19.AdditionClasses;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static AoC19.AdditionClasses.VirtualMachine;

namespace AoC19.Days
{
	internal class Day7 : IAoCDay
	{
		private readonly List<int> _opcodes;
		public Day7(string filename)
		{
			StreamReader sr = new(filename);
			_opcodes = sr.ReadToEnd().Split(",").Select(x => int.Parse(x.Trim())).ToList();
		}
		public void SolveA(bool isTest = false)
		{
			List<int> output = new();
			int max = int.MinValue;
			foreach(var perm in Permutation5) {
				int prev = 0;
				for (int i = 0; i < 5; i++)
				{
					List<int> opcodesA = _opcodes.Select(x => x).ToList();
					List<int> inp = new() { perm[i]-1, prev };
					VirtualMachine vm = new(opcodesA);
					vm.ExtendInstructions();
					vm.SetOutput(SetupOutput(output));
					vm.SetInput(SetupInput(inp));
					vm.Eval();
					prev = output[^1];
					output.Clear();
				}
				max = Math.Max(max, prev);
			}

			Console.WriteLine("Res A: {0}", max);
		}

		public void SolveB(bool isTest = false)
		{
			if (isTest) return;

			List<List<int>> inputs = Enumerable.Range(0,5).Select<int, List<int>>(_ => new List<int>(){0}).ToList();
			int max = int.MinValue;
			foreach (var perm in Permutation5)
			{
				Task[] machines = new Task[5];
				inputs[0] = new() { 0, 0 };

				for (int i = 0; i < 5; i++)
				{
					inputs[i][0] = perm[i] + 4;
				}

				for (int i = 0; i < 5; i++)
				{
					machines[i] = Task.Factory.StartNew(new Action<object?>((object? index) =>
					{
						int ind = (int)index!;
						List<int> opcodesA = _opcodes.Select(x => x).ToList();
						VirtualMachine vm = new(opcodesA);
						vm.ExtendInstructions();
						vm.SetOutput(SetupOutput(inputs[(ind + 1) % 5]));
						vm.SetInput(SetupInput(inputs[ind]));
						vm.Eval();
					}), i);
				}
				Task.WaitAll(machines);
				max = Math.Max(max, inputs[0][1]);
			}

			Console.WriteLine("Res A: {0}", max);
		}

		private static GetNext SetupInput(List<int> inp)
		{
			int ind = 0;
			return () => {
				while (ind >= inp.Count)
				{
					Task.Delay(100).Wait();
				}

				int ret = 0;
				ret = inp[ind];
				ind++;

				return ret;
			};
		}

		private static Output SetupOutput(List<int> outp)
		{
			return (long num) => {
				outp.Add((int)num);
			};
		}

		// Lazy AF
		private static readonly List<List<int>> Permutation5 = new()
		{	new(){1,2,3,4,5},
			new(){1,2,3,5,4},
			new(){1,2,4,3,5},
			new(){1,2,4,5,3},
			new(){1,2,5,3,4},
			new(){1,2,5,4,3},
			new(){1,3,2,4,5},
			new(){1,3,2,5,4},
			new(){1,3,4,2,5},
			new(){1,3,4,5,2},
			new(){1,3,5,2,4},
			new(){1,3,5,4,2},
			new(){1,4,2,3,5},
			new(){1,4,2,5,3},
			new(){1,4,3,2,5},
			new(){1,4,3,5,2},
			new(){1,4,5,2,3},
			new(){1,4,5,3,2},
			new(){1,5,2,3,4},
			new(){1,5,2,4,3},
			new(){1,5,3,2,4},
			new(){1,5,3,4,2},
			new(){1,5,4,2,3},
			new(){1,5,4,3,2},
			new(){2,1,3,4,5},
			new(){2,1,3,5,4},
			new(){2,1,4,3,5},
			new(){2,1,4,5,3},
			new(){2,1,5,3,4},
			new(){2,1,5,4,3},
			new(){2,3,1,4,5},
			new(){2,3,1,5,4},
			new(){2,3,4,1,5},
			new(){2,3,4,5,1},
			new(){2,3,5,1,4},
			new(){2,3,5,4,1},
			new(){2,4,1,3,5},
			new(){2,4,1,5,3},
			new(){2,4,3,1,5},
			new(){2,4,3,5,1},
			new(){2,4,5,1,3},
			new(){2,4,5,3,1},
			new(){2,5,1,3,4},
			new(){2,5,1,4,3},
			new(){2,5,3,1,4},
			new(){2,5,3,4,1},
			new(){2,5,4,1,3},
			new(){2,5,4,3,1},
			new(){3,1,2,4,5},
			new(){3,1,2,5,4},
			new(){3,1,4,2,5},
			new(){3,1,4,5,2},
			new(){3,1,5,2,4},
			new(){3,1,5,4,2},
			new(){3,2,1,4,5},
			new(){3,2,1,5,4},
			new(){3,2,4,1,5},
			new(){3,2,4,5,1},
			new(){3,2,5,1,4},
			new(){3,2,5,4,1},
			new(){3,4,1,2,5},
			new(){3,4,1,5,2},
			new(){3,4,2,1,5},
			new(){3,4,2,5,1},
			new(){3,4,5,1,2},
			new(){3,4,5,2,1},
			new(){3,5,1,2,4},
			new(){3,5,1,4,2},
			new(){3,5,2,1,4},
			new(){3,5,2,4,1},
			new(){3,5,4,1,2},
			new(){3,5,4,2,1},
			new(){4,1,2,3,5},
			new(){4,1,2,5,3},
			new(){4,1,3,2,5},
			new(){4,1,3,5,2},
			new(){4,1,5,2,3},
			new(){4,1,5,3,2},
			new(){4,2,1,3,5},
			new(){4,2,1,5,3},
			new(){4,2,3,1,5},
			new(){4,2,3,5,1},
			new(){4,2,5,1,3},
			new(){4,2,5,3,1},
			new(){4,3,1,2,5},
			new(){4,3,1,5,2},
			new(){4,3,2,1,5},
			new(){4,3,2,5,1},
			new(){4,3,5,1,2},
			new(){4,3,5,2,1},
			new(){4,5,1,2,3},
			new(){4,5,1,3,2},
			new(){4,5,2,1,3},
			new(){4,5,2,3,1},
			new(){4,5,3,1,2},
			new(){4,5,3,2,1},
			new(){5,1,2,3,4},
			new(){5,1,2,4,3},
			new(){5,1,3,2,4},
			new(){5,1,3,4,2},
			new(){5,1,4,2,3},
			new(){5,1,4,3,2},
			new(){5,2,1,3,4},
			new(){5,2,1,4,3},
			new(){5,2,3,1,4},
			new(){5,2,3,4,1},
			new(){5,2,4,1,3},
			new(){5,2,4,3,1},
			new(){5,3,1,2,4},
			new(){5,3,1,4,2},
			new(){5,3,2,1,4},
			new(){5,3,2,4,1},
			new(){5,3,4,1,2},
			new(){5,3,4,2,1},
			new(){5,4,1,2,3},
			new(){5,4,1,3,2},
			new(){5,4,2,1,3},
			new(){5,4,2,3,1},
			new(){5,4,3,1,2},
			new(){5,4,3,2,1}
		};
	}
}
