using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using AoC19.AdditionClasses;

namespace AoC19.Days
{
    internal class Day3 : IAoCDay
	{
		public Day3(string filename)
		{
			StreamReader sr = new(filename);
			var conv = (char a) => a switch
			{
				'R'=>0,
				'D'=>1,
				'L'=>2,
				'U'=>3,
				_=>-1,
			};
			_ropes = sr.ReadToEnd().Split('\n')
				.Select(x =>
				x.Split(',').Select(x =>
				{
					int f = conv(x[0]);
					int s = int.Parse(x[1..]);
					return (f, s);
				}
				).ToList()).ToList();
		}

		private void Solve()
		{
			uint dist = uint.MaxValue;
			uint time = uint.MaxValue;

			(int, int)[] vecs = new[] { (1, 0), (0, 1), (-1, 0), (0, -1) };
			Dictionary<(int, int), uint> coords = new();
			
			var coord = (0, 0);
			uint clock = 0;
			_ropes[0].ForEach(x =>
			{
				var vec = vecs[x.Item1];
				Enumerable.Range(1, x.Item2).Select(_ =>
				{
					clock++;
					coord = coord.Add(vec);
					if (!coords.ContainsKey(coord))
					{
						coords[coord] = clock;
					}
					return 0;
				}).ToArray();
			});

			coord = (0, 0);
			clock = 0;
			_ropes[1].ForEach(x =>
			{
				var vec = vecs[x.Item1];
				Enumerable.Range(1, x.Item2).Select(_ =>
				{
					clock++;
					coord = coord.Add(vec);
					if (coords.ContainsKey(coord))
					{
						dist = Math.Min(dist, (uint)Math.Abs(coord.Item1) + (uint)Math.Abs(coord.Item2));
						time = Math.Min(time, coords[coord] + clock);
					}
					return 0;
				}).ToArray();
			});
			_aRes = dist;
			_bRes = time;
		}

		public void SolveA(bool isTest)
		{

			if (_aRes is null) Solve();
			Console.WriteLine($"Solution A: {_aRes}");
		}

		public void SolveB(bool isTest)
		{
			if (_bRes is null) Solve();
			Console.WriteLine($"Solution B: {_bRes}");
		}

		private uint? _aRes;
		private uint? _bRes;
		private readonly List<List<(int, int)>> _ropes;
	}

}
