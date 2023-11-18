using AoC19.AdditionClasses;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Runtime.ExceptionServices;
using System.Text;
using System.Threading.Tasks;

namespace AoC19.Days
{
	internal class Day15 : IAoCDay
	{
		private List<long> _opcodes;
		private Dictionary<Vector2, long> _map = new() { { Vector2.Zero, 0} };
		private Vector2 position = Vector2.Zero;

		public Day15(string filename)
		{
			StreamReader sr = new(filename);
			_opcodes = sr.ReadToEnd().Split(",").Select(x => long.Parse(x.Trim())).ToList();
		}

		public void SolveA(bool isTest = false)
		{
			if (isTest) return;
			var vm = SetupVM();
			vm.Eval(true);
			//MakeMap();
		}

		public void SolveB(bool isTest = false)
		{
			if (isTest) return;
		}

		private void MakeMap()
		{
			var vm = SetupVM();
			position = Vector2.Zero;
			var queue = new Queue<Vector2>();
			queue.Enqueue(Vector2.UnitX);
			while (queue.Count > 0)
			{
				var pos = queue.Dequeue();
			}
		}

		private void VisitNeighbours()
		{

		}

		private VirtualMachine SetupVM()
		{
			VirtualMachine vm = new(_opcodes.Select(x => x).ToList());
			vm.ExtendInstructions();
			vm.ExtendIntructions2();
			vm.SetInput(() => 3);
			vm.SetOutput((x)=>Console.WriteLine(x));
			return vm;
		}
	}
}
