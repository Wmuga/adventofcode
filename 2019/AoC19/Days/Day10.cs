using AoC19.AdditionClasses;
using System;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.Linq;
using System.Numerics;
using System.Text;
using System.Threading.Tasks;

namespace AoC19.Days
{
	internal class Day10 : IAoCDay
	{
		private readonly Dictionary<Complex, List<bool?>> _asteroids = new();
		private int height = 0;
		private int width = 0;
		private Complex point = Complex.Zero;
		private static readonly Complex upVector = new(0, -1);
		public Day10(string filename)
		{
			using (StreamReader sr = new(filename))
			{
				while (!sr.EndOfStream)
				{
					height++;
					string? line = sr.ReadLine();
					if (line == null) break;
					line = line.Trim();
					for(width = 0; width < line.Length; width++)
					{
						if (line[width] == '.')
							continue;
						_asteroids[new Complex(width, height - 1)] = new();
					}
				}
			}

			foreach(var (_,visibles) in _asteroids)
			{
				visibles.InsertRange(0, Enumerable.Range(0, width * height).Select<int, bool?>(x => null));
			}
		}

		public void SolveA(bool isTest = false)
		{
			foreach(var (keyA, visiblesA) in _asteroids)
			{
				foreach (var (keyB, visiblesB) in _asteroids)
				{
					if (keyA == keyB)
						continue;
					
					if (visiblesA[GetNumber(keyB)] is not null)
						continue;

					bool visible = CanSee(keyA, keyB, visiblesA, visiblesB);

					visiblesA[GetNumber(keyB)] = visible;
					visiblesB[GetNumber(keyA)] = visible;
				}
			}

			int maxAsters = int.MinValue;

			foreach (var (key, vis) in _asteroids)
			{
				int asters = vis.Where(x => x is not null && x == true).Count();
				if (false)
				//if (isTest)
				{
					Console.WriteLine("{0},{1} : {2}", key.Real, key.Imaginary, asters);
				}

				if (asters > maxAsters)
				{
					maxAsters = asters;
					point = key;
				}
			}
			Console.WriteLine("Res A: {0}, point:{1}", maxAsters, point);
		}

		public void SolveB(bool isTest = false)
		{
			Dictionary<double, List<Complex>> angles = new();

			foreach (var (key, _) in _asteroids)
			{
				if (key == point)
					continue;


				Complex vector = key - point;
				double angle = (Math.PI*2 -GetAngle(vector, upVector)) % (Math.PI * 2);


				angles.AddTo(angle, key);
			}

			foreach (var (_, list) in angles)
			{
				list.Sort((x1,x2) =>
				{
					var mag1 = (x1 - point).Magnitude;
					var mag2 = (x2 - point).Magnitude;
					if (mag1 < mag2)
						return -1;
					if (mag1 == mag2)
						return 0;
					return 1;
				});
			}

			int counter = 0;
			Complex lastPoint = Complex.Zero;
			
			var keys = new List<double>(angles.Keys);
			keys.Sort();
			
			while(counter < 200)
			{
				foreach(var key in keys)
				{
					if (angles.ContainsKey(key))
					{
						counter++;
						lastPoint = angles[key][0];
						angles[key].RemoveAt(0);

						if (angles[key].Count == 0)
						{
							angles.Remove(key);
						}
					}

					if (isTest && (counter <= 3 || counter == 10 || counter == 20 || counter == 50 || counter > 197 ))
					{
						Console.WriteLine("Point: {0}, counter: {1}", lastPoint, counter);
					}

					if (counter == 200)
						break;
				}
			}

			Console.WriteLine("Res B: {0}, point:{1}", lastPoint.Real*100+lastPoint.Imaginary, lastPoint);
		}

		private static double GetAngle(Complex vectorA, Complex vectorB)
		{
			double dot = vectorA.Real * vectorB.Real + vectorA.Imaginary * vectorB.Imaginary;
			double det = vectorA.Real * vectorB.Imaginary - vectorA.Imaginary * vectorB.Real;
			return Math.Atan2(det,dot);
		}

		private bool CanSee(Complex keyA, Complex keyB, List<bool?> visiblesA, List<bool?> visiblesB)
		{
			bool visible = true;
			var vector = GetVector(keyB - keyA);
			var point = keyA + vector;

			while (point != keyB)
			{
				if (_asteroids.ContainsKey(point))
				{
					visible = false;
					_asteroids[point][GetNumber(keyA)] = true;
					visiblesA[GetNumber(point)] = true;
					break;
				}
				point += vector;
			}
			return visible;
		}

		private int GetNumber(Complex coord)
		{
			return (int)(coord.Real + coord.Imaginary * width);
		}

		private static int GCD(int l, int r)
		{
			while(l != 0 && r != 0)
			{
				if (l > r)
				{
					l %= r;
					continue;
				}
				r %= l;
			}
			return l + r;
		}

		private static Complex GetVector(Complex value)
		{
			if (value == 0)
				return value;
			double gcd = GCD(Math.Abs((int)value.Real), Math.Abs((int)value.Imaginary));

			return new Complex(value.Real/gcd, value.Imaginary/gcd);
		}


		private static Complex RoundWithEps(Complex value)
		{
			double e = 0.001;
			double roundReal = Math.Round(value.Real);
			double roundIm = Math.Round(value.Imaginary);
			return new Complex(
				Math.Abs(value.Real - roundReal) <= e ? roundReal : value.Real,
				Math.Abs(value.Imaginary - roundIm) <= e ? roundIm : value.Imaginary
				);
		}
	}
}
