using AoC19.Days;
using System.Reflection.Emit;
using System.Xml.Schema;

namespace AoC19
{
	internal class Program
	{
		private static readonly string InputFolder = "D:\\Desktop\\Side Goods\\AdventOfCode\\2019\\AoC19\\Inputs\\";
		
		public static string DayInput(int day, bool test)
		{
			if (day == 4)
			{
				return test ? "" : "165432-707912"; 
			}
			return $"{InputFolder}Day{day}{(test ? "Test" : "")}.txt";
		}
		
		static void Main(string[] args)
		{
			//SolveDay<Day15>(15);
			ParseIntCode(15);
		}

		public static void SolveDay<T>(int day) where T : IAoCDay
		{
			string inTest = DayInput(day, true);
			string inAct = DayInput(day, false);

			Console.WriteLine("Test input:");
			IAoCDay curDay = (T)Activator.CreateInstance(typeof(T), new[] {inTest})!;
			curDay.SolveA(true);
			curDay.SolveB(true);

			Console.WriteLine("Actual input:");
			curDay = (T)Activator.CreateInstance(typeof(T), new[] { inAct })!;
			curDay.SolveA();
			curDay.SolveB();

		}

		public static void ParseIntCode(int day)
		{
			string inAct = DayInput(day, false);
			List<long> opcodes = new StreamReader(inAct).ReadToEnd().Split(",").Select(x => long.Parse(x.Trim())).ToList();
			int i = 0;
			while(i < opcodes.Count)
			{
				switch (opcodes[i] % 100)
				{
					case 1:
						Console.Write("ADD ");
						ParseParams(opcodes, i, 3);
						i += 4;
						break;
					case 2:
						Console.Write("MUL ");
						ParseParams(opcodes, i, 3);
						i += 4;
						break;
					case 3:
						Console.Write("INP ");
						ParseParams(opcodes, i, 1);
						i += 2;
						break;
					case 4:
						Console.Write("OUT ");
						ParseParams(opcodes, i, 1);
						i += 2;
						break;
					case 5:
						Console.Write("JNZ ");
						ParseParams(opcodes, i, 2);
						i += 3;
						break;
					case 6:
						Console.Write("JEZ ");
						ParseParams(opcodes, i, 2);
						i += 3;
						break;
					case 7:
						Console.Write("LES ");
						ParseParams(opcodes, i, 3);
						i += 4;
						break;
					case 8:
						Console.Write("EQS ");
						ParseParams(opcodes, i, 3);
						i += 4;
						break;
					case 9:
						Console.Write("ADB ");
						ParseParams(opcodes, i, 2);
						i += 3;
						break;
					case 99:
						Console.Write("END");
						i++;
						break;
					default:
						Console.Write(opcodes[i]);
						i++;
						break;
				}
				Console.WriteLine();
			}
		}
		private static void ParseParams(List<long> opcodes, int pos, int count)
		{
			int modes = (int)(opcodes[pos] / 100);

			for(int i  = 1; i <= count; i++)
			{
				ParseParam(modes%10, opcodes[pos + i]);
				if (i != count)
				{
					Console.Write(", ");
				}
				modes /= 10;
			}
		}
		private static void ParseParam(int mode, long param)
		{
			if (mode == 0)
			{
				Console.Write("[{0}]", param);
				return;
			}

			if (mode == 1)
			{
				Console.Write("{0}", param);
				return;
			}

			Console.Write("[base + {0}]", param);
		}
	}
}