using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Intrinsics.Arm;
using System.Text;
using System.Threading.Tasks;

namespace AoC19.Days
{
	internal class Day14 : IAoCDay
	{
		internal struct Recipe
		{
			public ulong Count;
			public List<(string, ulong)> Ingrs;
			public Recipe()
			{
				Count = 0;
				Ingrs = new();
			}
		}

		private ulong oreCounter = 0;
		private Dictionary<string, Recipe> _recipes = new();
		private Dictionary<string, ulong> _bag = new();
		public Day14(string filename)
		{
			StreamReader sr = new(filename);
			while(!sr.EndOfStream) { 
				string? line = sr.ReadLine();
				if (line == null)
				{
					break;
				}

				var recipe_array = line.Split(" => ");
				Recipe recipe = new();

				var ingr_array = recipe_array[0].Split(", ");
				foreach(var ingr in ingr_array)
				{
					var ingr_list = ingr.Split(' ');
					uint count = uint.Parse(ingr_list[0]);
					recipe.Ingrs.Add((ingr_list[1], count));
				}
				
				var product_array = recipe_array[1].Split(' ');
				recipe.Count = uint.Parse(product_array[0]);
				_recipes[product_array[1]] = recipe;
			}
		}

		// bag of elements. If not enough - craft.

		public void SolveA(bool isTest = false)
		{
			oreCounter = 0;
			_bag = new();
			Craft("FUEL", 1);
			Console.WriteLine("Res A {0}", oreCounter);
		}

		public void SolveB(bool isTest = false)
		{
			ulong ORE_COUNT = 1_000_000_000_000;
			ulong oreCounterA = oreCounter;
			oreCounter = 0;
			_bag = new();

			while(ORE_COUNT >= oreCounterA)
			{
				ulong rem = ORE_COUNT / oreCounterA;
				Craft("FUEL", rem);
				ORE_COUNT -= oreCounter;
				oreCounter = 0;
			}

			Craft("FUEL", 1);
			if (ORE_COUNT < oreCounter)
			{
				_bag["FUEL"] -= 1;
			}

			Console.WriteLine("Res B {0}", _bag["FUEL"]);
		}


		private void Craft(string element, ulong quantity)
		{
			var recipe = _recipes[element];

			uint multiplier = (uint)Math.Ceiling((double)quantity / recipe.Count);

			foreach(var (ingr, ingr_count) in recipe.Ingrs)
			{
				Use(ingr, ingr_count * multiplier);
			}

			var count = _bag.TryGetValue(element, out ulong value) ? value : 0;
			_bag[element] = count + multiplier * recipe.Count;
		}

		private void Use(string element, ulong quantity)
		{
			if (element == "ORE")
			{
				oreCounter += quantity;
				return;
			}

			if (!_bag.ContainsKey(element) || _bag[element] < quantity)
			{
				var count = _bag.TryGetValue(element, out ulong value) ? value : 0;
				Craft(element, quantity - count);	
			}

			_bag[element] -= quantity;

			if (_bag[element] == 0)
			{
				_bag.Remove(element);
			}
		}
	}
}
