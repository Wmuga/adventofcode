using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AoC19.AdditionClasses
{
	internal class VirtualMachine
	{
		public delegate int Instruction(int modes, int pos);
		public delegate long GetNext();
		public delegate void Output(long num);

		private GetNext getNext = StdIn;
		private Output output = StdOut;
		private List<long> opcodes;
		private Dictionary<int, Instruction> _evaluators = new();
		private Dictionary<long, long> _memory = new();

		private long relativeBase = 0;
		private bool useExtendedMemory = false;

		public VirtualMachine(List<int> opcodes)
		{
			this.opcodes = opcodes.Select(x => (long)x).ToList();
			SetStandartIntructions();
		}
		public VirtualMachine(List<long> opcodes)
		{
			this.opcodes = opcodes;
			SetStandartIntructions();
		}

		public int Eval()
		{
			int pos = 0;
			while (pos != -1)
			{
				long opcode = opcodes[pos];
				int testOpcode = (int)(opcode % 100);
				if (!_evaluators.ContainsKey(testOpcode)) {
					Console.WriteLine("No opcode {0}", testOpcode);
					pos = -1;
					continue;
				}

				pos = _evaluators[testOpcode]((int)(opcode/100), pos);
			}
			return (int)opcodes[0];
		}

		public void SetAction(int opcode, Instruction instruction)
		{
			_evaluators[opcode] = instruction;
		}
		private void SetStandartIntructions()
		{
			SetAction(1, OpCode1);
			SetAction(2, OpCode2);
			SetAction(99, (_, _) => -1);
		}

		public void ExtendInstructions()
		{
			SetAction(3, OpCode3);
			SetAction(4, OpCode4);
			SetAction(5, OpCode5);
			SetAction(6, OpCode6);
			SetAction(7, OpCode7);
			SetAction(8, OpCode8);
		}

		public void ExtendIntructions2()
		{
			useExtendedMemory = true;
			SetAction(9, OpCode9);
		}

		public void SetInput(GetNext next)
		{
			getNext = next;
		}

		public void SetOutput(Output outp)
		{
			output = outp;
		}

		private static long StdIn()
		{
			string res = Console.ReadLine() ?? "";
			long inp = long.Parse(res);
			return inp;
		}

		private static void StdOut(long num)
		{
			Console.WriteLine(num);
		}

		private long TryGetMem(long addr)
		{
			if (addr < 0)
				return -1;
			
			if (_memory.ContainsKey(addr))
				return _memory[addr];
			
			_memory[addr] = 0;
			return 0;
		}

		private int WriteMem(long addr, long param, int mode)
		{
			mode %= 10;

			if (mode == 1)
			{
				Console.WriteLine("TO in immediate mode");
				return -1;
			}

			addr = mode == 0 ? addr : addr+relativeBase;

			if (addr >= opcodes.Count)
			{
				if (useExtendedMemory)
				{
					_memory[addr] = param;
					return 0;
				}
				return -1;
			}

			opcodes[(int)addr] = param;
			return 0;
		}

		private long GetParam(long opcode, int mode)
		{
			mode %= 10;
			
			if (mode == 0)
			{
				if (opcode < opcodes.Count)
					return opcodes[(int)opcode];
				if (!useExtendedMemory)
					return -1;
				return TryGetMem(opcode);
			}

			if (mode == 1)
				return opcode;

			long addr = relativeBase + opcode;

			if (addr < opcodes.Count)
				return opcodes[(int)addr];
			if (!useExtendedMemory)
				return -1;
			return TryGetMem(addr);
		}

		private int OpCode1(int modes,int pos)
		{
			long from1 = opcodes[pos + 1];
			long from2 = opcodes[pos + 2];
			long to = opcodes[pos + 3];
			long p1 = GetParam(from1, modes);
			long p2 = GetParam(from2, modes/10);

			if(WriteMem(to, p1 + p2, modes / 100) == -1)
				return -1;

			return pos + 4;
		}

		private int OpCode2(int modes, int pos)
		{
			long from1 = opcodes[pos + 1];
			long from2 = opcodes[pos + 2];
			long to = opcodes[pos + 3];
			long p1 = GetParam(from1, modes);
			long p2 = GetParam(from2, modes / 10);

			if (WriteMem(to, p1 * p2, modes / 100) == -1)
				return -1;

			return pos + 4;
		}

		
		private int OpCode3(int modes, int pos)
		{
			long to = opcodes[pos + 1];
			WriteMem(to,getNext(),modes);
			
			return pos + 2;
		}

		private int OpCode4(int modes, int pos)
		{
			long from1 = opcodes[pos + 1];
			long p1 = GetParam(from1, modes);
			output(p1);
			return pos + 2;
		}

		private int OpCode5(int modes, int pos)
		{
			long from1 = opcodes[pos + 1];
			long from2 = opcodes[pos + 2];
			long p1 = GetParam(from1, modes);
			long p2 = GetParam(from2, modes / 10);
			pos += 3;
			if (p1 != 0) pos = (int)p2;
			return pos;
		}

		private int OpCode6(int modes, int pos)
		{
			long from1 = opcodes[pos + 1];
			long from2 = opcodes[pos + 2];
			long p1 = GetParam(from1, modes);
			long p2 = GetParam(from2, modes / 10);
			pos += 3;
			if (p1 == 0) pos = (int)p2;
			return pos;
		}

		private int OpCode7(int modes, int pos)
		{
			long from1 = opcodes[pos + 1];
			long from2 = opcodes[pos + 2];
			long to = opcodes[pos + 3];
			long p1 = GetParam(from1, modes);
			long p2 = GetParam(from2, modes / 10);

			if (WriteMem(to, p1 < p2 ? 1 : 0, modes / 100) == -1)
				return -1;

			return pos + 4;
		}

		private int OpCode8(int modes, int pos)
		{
			long from1 = opcodes[pos + 1];
			long from2 = opcodes[pos + 2];
			long to = opcodes[pos + 3];
			long p1 = GetParam(from1, modes);
			long p2 = GetParam(from2, modes / 10);

			if (WriteMem(to, p1 == p2 ? 1 : 0, modes / 100) == -1)
				return -1;

			return pos + 4;
		}

		private int OpCode9(int modes, int pos)
		{
			long from1 = opcodes[pos + 1];
			int p1 = (int)GetParam(from1, modes);
			relativeBase += p1;
			return pos + 2;
		}
	}
}
