let inp = ['$ cd /','$ ls','dir a','14848514 b.txt','8504156 c.dat','dir d','$ cd a','$ ls','dir e','29116 f','2557 g','62596 h.lst','$ cd e','$ ls','584 i','$ cd ..','$ cd ..','$ cd d','$ ls','4060174 j','8033020 d.log','5626152 d.ext','7214296 k']

class FileTree {
  constructor(type,size,prev){
    this.contents = {}
    this.size = size
    this.type = type
    this.prev = prev
  }
}

let main = new FileTree('dir',0, null)

function init(){
  let cur = main
  let i = 0
  while (i < inp.length){
    const com = inp[i].split(' ')
    switch(com[1]){
      case 'cd':
        switch(com[2]){
          case '/':
            cur = main
            break
          case '..':
            cur = cur.prev
            break
          default:
            cur = cur.contents[com[2]]
            break
        }
        i++
        break
      case 'ls':
        i++
        let line = inp[i].split(' ')
        while(line[0] != '$'){
          cur.contents[line[1]] = line[0] == 'dir' ? new FileTree('dir', 0, cur) : new FileTree('file', parseInt(line[0]), cur)
          i++
          if (i == inp.length) break 
          line = inp[i].split(' ')
        } 
        break
      default:
        console.log('How we got there?')
        console.log(inp[i])
        return
    }
  }
}

function calcSize(dir){
  let res = 0
  for (let content_name in dir.contents){
    const content = dir.contents[content_name]
    res += content.type == 'dir' ? calcSize(content) : content.size
  }
  dir.size = res
  return res
}

window.addEventListener('load',()=>{
  init()
  calcSize(main)
})
