using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AoC19.AdditionClasses
{
	internal class TreeNode<T>
	{
		public T Value { get; set; }
		public TreeNode<T>? Parent { get; set; }
		public List<TreeNode<T>> Chidren { get; } = new();

		public TreeNode(T value)
		{
			Value = value;
		}

		public override string ToString()
		{
			return Value?.ToString()??base.ToString()!;
		}

	}
}
