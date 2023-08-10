using AoC19.AdditionClasses;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Threading.Tasks;

namespace AoC19.Days
{
	internal class Day11 : IAoCDay
	{
		private readonly List<long> _opcodes;
		private Dictionary<Complex, bool> _coords = new();
		
		private static readonly List<Complex> _vectors = new()
		{
			Complex.ImaginaryOne,
			Complex.One,
			-Complex.ImaginaryOne,
			-Complex.One,
		};

		private bool outState = true;
		Complex robotCoord = Complex.Zero;
		int robotRotation = 0;


		public Day11(string filename)
		{
			StreamReader sr = new(filename);
			_opcodes = sr.ReadToEnd().Split(",").Select(x => long.Parse(x.Trim())).ToList();
		}

		public void SolveA(bool isTest = false)
		{
			if (isTest) return;

			robotCoord = Complex.Zero;
			_coords = new();

			var vm = SetupVM();
			vm.Eval();

			Console.WriteLine("Res A: {0}", _coords.Keys.Count);
		}

		public void SolveB(bool isTest = false)
		{
			if (isTest) return;

			robotCoord = Complex.Zero;
			_coords = new();

			_coords[robotCoord] = true;

			var vm = SetupVM();
			vm.Eval();

			int top = 0;
			int left = 0;
			int right = 0;
			int bottom = 0;
			foreach (var key in _coords.Keys)
			{
				top = Math.Max(top, (int)key.Imaginary);
				bottom = Math.Min(bottom, (int)key.Imaginary);
				left = Math.Min(left, (int)key.Real);
				right = Math.Max(right, (int)key.Real);
			}

			for (int line = top; line >= bottom; line--)
			{
				for (int startLine = left; startLine <= right; startLine++)
				{
					Complex coord = new(startLine, line);
					if (_coords.ContainsKey(coord))
					{
						Console.Write(_coords[coord] ? "■" : " ");
						continue;
					}
					Console.Write(" ");
				}
				Console.WriteLine();
			}
		}

		private long ProvideInput()
		{
			if (_coords.ContainsKey(robotCoord))
				return _coords[robotCoord] ? 1 : 0;
			return 0;

		}

		private void ReadOutput(long num)
		{
			if (outState)
			{
				_coords[robotCoord] = num == 1;
			}
			else
			{
				robotRotation = (robotRotation + (num == 1 ? 1 : -1) + 4) % 4;
				robotCoord += _vectors[robotRotation];
			}
			outState = !outState;
		}

		private VirtualMachine SetupVM()
		{
			VirtualMachine vm = new(_opcodes.Select(x=>x).ToList());
			vm.ExtendInstructions();
			vm.ExtendIntructions2();
			vm.SetInput(ProvideInput);
			vm.SetOutput(ReadOutput);
			return vm;
		}
	}
}
