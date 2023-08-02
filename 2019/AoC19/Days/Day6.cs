using AoC19.AdditionClasses;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using PlanetNode = AoC19.AdditionClasses.TreeNode<string>;

namespace AoC19.Days
{
	internal class Day6 : IAoCDay
	{
		Dictionary<string, PlanetNode> pool = new() { { "COM", new PlanetNode("COM") } };
		public Day6(string filename)
		{
			StreamReader sr = new(filename);
			while(!sr.EndOfStream)
			{
				string? line = sr.ReadLine();
				if (line == null || line.Length == 0) continue;
				AddOrbit(line);
			}
		}

		public void SolveA(bool isTest = false)
		{
			Console.WriteLine("Res A: {0}", CheckSum(pool["COM"],0));
		}

		public void SolveB(bool isTest = false)
		{
			if (isTest)
			{
				var you = GetOrCreate("YOU");
				you.Parent = pool["K"];
				pool["K"].Chidren.Add(you);
				var san = GetOrCreate("SAN");
				san.Parent = pool["I"];
				pool["I"].Chidren.Add(san);
			}
			Console.WriteLine("Res B: {0}", BFS());
		}

		private int BFS()
		{
			int res = 0;
			PriorityQueue<(PlanetNode, int), int> toVisit = new();
			HashSet<PlanetNode> visited = new();
			toVisit.Enqueue((pool["YOU"],0), 0);
			while(toVisit.Count > 0)
			{
				var (cur, prior) = toVisit.Dequeue();

				if (visited.Contains(cur))
					continue;
				visited.Add(cur);

				if (cur.Chidren.Contains(pool["SAN"]))
				{
					res = prior; 
					break;
				}

				if (cur.Parent is not null) toVisit.Enqueue((cur.Parent, prior + 1), prior+1);
				foreach(var child in cur.Chidren)
				{
					toVisit.Enqueue((child, prior + 1), prior + 1);
				}
			}
			return res -1;
		}

		private int CheckSum(PlanetNode node, int counter)
		{
			if (node.Chidren.Count == 0) return counter;
			return counter + node.Chidren.Sum(x=>CheckSum(x, counter+1));
		}

		private void AddOrbit(string line)
		{
			var ar = line.Split(")");

			var parent = GetOrCreate(ar[0]);
			var child = GetOrCreate(ar[1]);

			parent.Chidren.Add(child);
			child.Parent = parent;
		}

		private PlanetNode GetOrCreate(string name)
		{
			if (!pool.ContainsKey(name))
			{
				pool[name] = new PlanetNode(name);
			}
			return pool[name];
		}
	}
}
