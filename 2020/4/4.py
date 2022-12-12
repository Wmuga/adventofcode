import re

def parse_passports(lines:list):
  passports = list()
  passport = dict()
  for line in lines:
    if len(line)==0:
      passports.append(passport)
      passport = dict()
      continue

    for data in line.split(' '):
      pair = data.split(':')
      passport[pair[0]] = pair[1]
  passports.append(passport)
  return passports    

def check_passport(passport:list,checkValues:bool = False):
  valid_lines = ['byr','eyr','iyr','hgt','hcl','ecl','pid']
  for line in valid_lines:
    if (line not in passport):
      return False
  if checkValues and not(1920<=int(passport['byr'])<=2002 and 2010<=int(passport['iyr'])<=2020 and 2020<=int(passport['eyr'])<=2030 
    and (('cm' in passport['hgt'] and 150<=int(passport['hgt'][:-2])<=193) or ('in' in passport['hgt'] and 59<=int(passport['hgt'][:-2])<=76))
    and re.match(r'\#[0-9a-f]{6}\b',passport['hcl']) and passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and re.match(r'[0-9]{9}\b',passport['pid'])):
    return False
  return True         

def solve1(passports:list):
  valid_count = 0
  for passport in passports:
    valid_count += int(check_passport(passport))
  print(valid_count)

def solve2(passports:list):
  valid_count = 0
  for passport in passports:
    valid_count += int(check_passport(passport,True))
  print(valid_count)

passports = parse_passports([i.strip() for i in open('input.txt','r').readlines()])

solve1(passports)
solve2(passports)