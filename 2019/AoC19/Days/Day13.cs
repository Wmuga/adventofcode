using AoC19.AdditionClasses;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Threading.Tasks;

namespace AoC19.Days
{
	internal class Day13 : IAoCDay
	{
		private List<long> _opcodes;
		private OutputType _state = OutputType.X;
		private readonly Dictionary<Vector2, Tile> _field = new();
		private Vector2 _coord = new();
		private Vector2 _paddle = new();
		private Vector2 _ball = new();

		public Day13(string filename)
		{
			StreamReader sr = new(filename);
			_opcodes = sr.ReadToEnd().Split(",").Select(x => long.Parse(x.Trim())).ToList();
		}

		public void SolveA(bool isTest = false)
		{
			if (isTest) return;
			var vm = SetupVM();
			vm.Eval();

			int res = _field.Where((x)=>x.Value==Tile.Block).Count();
			Console.WriteLine("Res A: {0}", res);
		}

		public void SolveB(bool isTest = false)
		{
			if (isTest) return;
			Console.WriteLine("Res B:");
			_opcodes[0] = 2;
			var vm = SetupVM();
			vm.SetOutput(OutputScore);
			vm.Eval();
		}

		private long ProvideInput()
		{
			if (_ball.X < _paddle.X)
			{
				_paddle.X -= 1;
				return -1;
			}

			if (_ball.X > _paddle.X)
			{
				_paddle.X += 1;
				return 1;
			}

			return 0;
		}

		private void OutputScore(long num)
		{
			if (_state == OutputType.X)
			{
				_ball.X = num;
				_state = OutputType.Y;
				return;
			}

			if (_state == OutputType.Y)
			{
				_ball.Y = num;
				_state = OutputType.Tile;
				return;
			}
			_state = OutputType.X;

			Console.Write("\r{0,-16}", num);
		}


		private void OutputField(long num)
		{
			if (_state == OutputType.X)
			{
				_coord.X = num;
				_state = OutputType.Y;
				return;
			}

			if (_state == OutputType.Y)
			{
				_coord.Y = num;
				_state = OutputType.Tile;
				return;
			}

			_state = OutputType.X;
			Tile tile = Extensions.FromInt<Tile>((int)num);
			_field[new(_coord.X, _coord.Y)] = tile;

			if (tile == Tile.Horizontal)
			{
				_paddle = new(_coord.X, _coord.Y);
			}

			if (tile == Tile.Ball)
			{
				_ball = new(_coord.X, _coord.Y);
			}
		}

		private VirtualMachine SetupVM()
		{
			VirtualMachine vm = new(_opcodes.Select(x => x).ToList());
			vm.ExtendInstructions();
			vm.ExtendIntructions2();
			vm.SetInput(ProvideInput);
			vm.SetOutput(OutputField);
			return vm;
		}

		internal enum OutputType
		{
			X,
			Y,
			Tile,
		}

		internal enum Tile
		{
			Empty = 0,
			Wall,
			Block,
			Horizontal,
			Ball
		}
	}
}
