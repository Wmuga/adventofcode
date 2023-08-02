using AoC19.Days;

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
			SolveDay<Day9>(9);
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
	}
}