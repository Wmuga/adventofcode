using AoC19.AdditionClasses;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace AoC19.Days
{
	internal class Day12 : IAoCDay
	{
		private static readonly Regex findNumbersRegex = new(@"-?\d+", RegexOptions.Compiled);
		private readonly List<Moon> _moons = new();
		public Day12(string filename) {
			StreamReader sr = new(filename);
			while(!sr.EndOfStream)
			{
				string? line = sr.ReadLine();
				if (line == null)
					break;
				line = line.Trim();
				var matches = findNumbersRegex.Matches(line).Select(x=>int.Parse(x.Value)).ToList();
				_moons.Add(new() { Position = new(matches[0], matches[1], matches[2]) });
			}
		}

		public void SolveA(bool isTest = false)
		{
			int max_steps = isTest ? 100 : 1000;
			var moons = _moons.Select(x => new Moon()
			{
				Position = new(x.Position.X, x.Position.Y, x.Position.Z),
				Velocity = new(x.Velocity.X, x.Velocity.Y, x.Velocity.Z)
			}).ToList();
			for (int step = 0; step < max_steps; step++)
			{
				Step(moons);

				if (isTest && (step % 10 == 9 || step < 10))
				{
					Console.WriteLine("After step {0}:", step+1);
					foreach (var moon in moons)
					{
						Console.WriteLine("pos={0}, vel={1}", moon.Position, moon.Velocity);
					}
					Console.WriteLine("Energy: {0}", CalcEnergy(moons));
				}
			}

			float res = CalcEnergy(moons);

			Console.WriteLine("Res A: {0}", res);
		}

		public void SolveB(bool isTest = false)
		{
			long step = 0;
			long stepsX = 0;
			long stepsY = 0;
			long stepsZ = 0;

			var moons = _moons.Select(x => new Moon()
			{
				Position = new(x.Position.X, x.Position.Y, x.Position.Z),
				Velocity = new(x.Velocity.X, x.Velocity.Y, x.Velocity.Z)
			}).ToList();

			do
			{
				Step(moons);
				step++;

				var vels = MulVelocity(moons);

				if (AllSame(moons, SelectorX) && stepsX == 0) stepsX = step;
				if (AllSame(moons, SelectorY) && stepsY == 0) stepsY = step;
				if (AllSame(moons, SelectorZ) && stepsZ == 0) stepsZ = step;

			} while (stepsX == 0 || stepsY == 0 || stepsZ == 0);
			var lcd1 = Extensions.LCD(stepsX, stepsY);
			Console.WriteLine("Res B: {0}", Extensions.LCD(lcd1, stepsZ));
		}

		private bool AllSame(List<Moon> moons, Func<Vector3, float> selector)
		{
			for(int i = 0; i < moons.Count; i++)
			{
				if (selector(moons[i].Position) != selector(_moons[i].Position)
					|| selector(moons[i].Velocity) != selector(_moons[i].Velocity))
					return false;
			}
			return true;
		}

		private float SelectorX(Vector3 v) => v.X;
		private float SelectorY(Vector3 v) => v.Y;
		private float SelectorZ(Vector3 v) => v.Z;

		private static Vector3 MulVelocity(List<Moon> moons)
		{
			Vector3 res = Vector3.One;
			foreach(var moon in moons)
			{
				res.X *= moon.Velocity.X;
				res.Y *= moon.Velocity.Y;
				res.Z *= moon.Velocity.Z;
			}
			return res;
		}

		private static void Step(List<Moon> moons)
		{
			for (int i = 0; i < moons.Count - 1; i++)
			{
				var moon1 = moons[i];
				for (int j = i + 1; j < moons.Count; j++)
				{
					var moon2 = moons[j];
					moon1.ApplyGravity(moon2);
				}
			}

			foreach (var moon in moons)
			{
				moon.ApplyVelocity();
			}
		}

		private static float CalcEnergy(List<Moon> moons)
		{
			float res = 0;
			foreach (var moon in moons)
			{
				res += moon.Position.ManhLength() * moon.Velocity.ManhLength();
			}
			return res;
		}

		internal class Moon
		{
			public Vector3 Position { get; set; } = Vector3.Zero;
			public Vector3 Velocity { get; set; } = Vector3.Zero;

			public void ApplyGravity(Moon other)
			{
				Vector3 addVector = Vector3.Zero;
				// Calc direction	
				addVector.X = (other.Position.X - Position.X);
				addVector.Y = (other.Position.Y - Position.Y);
				addVector.Z = (other.Position.Z - Position.Z);
				// Normalize to 1
				if (addVector.X != 0) addVector.X /= Math.Abs(addVector.X);
				if (addVector.Y != 0) addVector.Y /= Math.Abs(addVector.Y);
				if (addVector.Z != 0) addVector.Z /= Math.Abs(addVector.Z);
				// Apply
				Velocity += addVector;
				other.Velocity -= addVector;
			}

			public void ApplyVelocity()
			{
				Position += Velocity;
			}
		}
	}
}
