using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AoC19.Days
{
	internal class Day8 : IAoCDay
	{
		List<int> _data = new();
		public Day8(string filename)
		{
			StreamReader sr = new(filename);
			var data = sr.ReadToEnd();
			foreach (var item in data)
			{
				_data.Add(item - '0');
			}
		}

		public void SolveA(bool isTest = false)
		{
			var (width, height) = isTest ? (3, 2) : (25,6);
			var layer_size = width * height;
			List<int[]> layers = _data.Chunk(layer_size).ToList();
			var zeros = layers.Select(x=>x.Count(x=>x==0)).ToList();
			int zerosMin = zeros.Min();
			int index = zeros.FindIndex(x=>x==zerosMin);
			int res = layers[index].Count(x => x == 1) * layers[index].Count(x => x == 2);
			Console.WriteLine("Res A: {0}",res);
		}

		public void SolveB(bool isTest = false)
		{
			// black, white, transparent
			var (width, height) = isTest ? (2, 2) : (25, 6);
			var layer_size = width * height;
			int[] image = new int[layer_size];
			Array.Fill(image, 2);

			List<int[]> layers = _data.Chunk(layer_size).ToList();
			for(int i = 0; i < layer_size; i++)
			{
				foreach(var layer in layers)
				{
					if (layer[i] == 2)
						continue;
					image[i] = layer[i];
					break;
				}
			}
			Console.WriteLine("Res B:");
			foreach(var line in image.Chunk(width))
			{
				var strLine = string.Join(string.Empty,line.Select(x => x == 1 ? '■' : ' ').ToList());
				Console.WriteLine(strLine);
			}
		}
	}
}
