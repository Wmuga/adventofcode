#include "parsed_inp.h"

std::vector<int64_t> monad0(int64_t number, int64_t x, int64_t y, int64_t z, int64_t w){
	w = number;
	x *= 0;
	x += z;
	x = x % 26;
	z /= 1;
	x += 12;
	x = x == w ? 1 : 0;
	x = x == 0 ? 1 : 0; // x = 1. y = 0 z = 0 w = any
	y *= 0;
	y += 25; 
	y *= x;
	y += 1;
	z *= y;
	y *= 0;
	y += w; 
	y += 15; 
	y *= x;
	z += y; 
	return std::vector<int64_t>({x,y,z,w}); // x = 1. y = w1 + 15 z = w1 + 15 w = w1
}

std::vector<int64_t> monad1(int64_t number, int64_t x, int64_t y, int64_t z, int64_t w){
	w = number;
	x *= 0; 
	x += z;
	x = x % 26; 
	z /= 1;
	x += 14; 
	x = x == w ? 1 : 0;
	x = x == 0 ? 1 : 0; 
	y *= 0;
	y += 25;
	y *= x;
	y += 1;
	z *= y; 
	y *= 0;
	y += w;
	y += 12;
	y *= x;
	z += y;
	return std::vector<int64_t>({x,y,z,w}); // x = 1. y = w2 + 12 z = (w1 + 15)*26 + w2 + 12. w = w2
}

std::vector<int64_t> monad2(int64_t number, int64_t x, int64_t y, int64_t z, int64_t w){
	w = number;
	x *= 0;
	x += z; 
	x = x % 26;
	z /= 1;
	x += 11;
	x = x == w ? 1 : 0;
	x = x == 0 ? 1 : 0;
	y *= 0;
	y += 25;
	y *= x;
	y += 1;
	z *= y; 
	y *= 0;
	y += w;
	y += 15;
	y *= x;
	z += y;
	return std::vector<int64_t>({x,y,z,w}); // x = 1. y = w3 + 15 z = ((w1 + 15)*26 + w2 + 12) * 26 + w3 + 15. w = w2
}

std::vector<int64_t> monad3(int64_t number, int64_t x, int64_t y, int64_t z, int64_t w){
	w = number;
	x *= 0;
	x += z; 
	x = x % 26;
	z /= 26;
	x += -9;
	x = x == w ? 1 : 0; // x = w3 + 6. y = w3 + 15 z = (w1 + 15)*26 + w2 + 12. w = w2
	x = x == 0 ? 1 : 0; // x = w4-w3 = 6 && w3 <=3 ? 0 : 1 y = w3 + 15 z = (w1 + 15)*26 + w2 + 12. w = w2
	y *= 0;
	y += 25;
	y *= x;
	y += 1;
	z *= y;
	y *= 0;
	y += w;
	y += 12;
	y *= x;
	z += y;
	return std::vector<int64_t>({x,y,z,w}); 
}

std::vector<int64_t> monad4(int64_t number, int64_t x, int64_t y, int64_t z, int64_t w){
	w = number;
	x *= 0;
	x += z;
	x = x % 26;
	z /= 26;
	x += -7;
	x = x == w ? 1 : 0;
	x = x == 0 ? 1 : 0;
	y *= 0;
	y += 25;
	y *= x;
	y += 1;
	z *= y;
	y *= 0;
	y += w;
	y += 15;
	y *= x;
	z += y;
	return std::vector<int64_t>({x,y,z,w});
}

std::vector<int64_t> monad5(int64_t number, int64_t x, int64_t y, int64_t z, int64_t w){
	w = number;
	x *= 0;
	x += z;
	x = x % 26;
	z /= 1;
	x += 11;
	x = x == w ? 1 : 0;
	x = x == 0 ? 1 : 0;
	y *= 0;
	y += 25;
	y *= x;
	y += 1;
	z *= y;
	y *= 0;
	y += w;
	y += 2;
	y *= x;
	z += y;
	return std::vector<int64_t>({x,y,z,w});
}

std::vector<int64_t> monad6(int64_t number, int64_t x, int64_t y, int64_t z, int64_t w){
	w = number;
	x *= 0;
	x += z;
	x = x % 26;
	z /= 26;
	x += -1;
	x = x == w ? 1 : 0;
	x = x == 0 ? 1 : 0;
	y *= 0;
	y += 25;
	y *= x;
	y += 1;
	z *= y;
	y *= 0;
	y += w;
	y += 11;
	y *= x;
	z += y;
	return std::vector<int64_t>({x,y,z,w});
}

std::vector<int64_t> monad7(int64_t number, int64_t x, int64_t y, int64_t z, int64_t w){
	w = number;
	x *= 0;
	x += z;
	x = x % 26;
	z /= 26;
	x += -16;
	x = x == w ? 1 : 0;
	x = x == 0 ? 1 : 0;
	y *= 0;
	y += 25;
	y *= x;
	y += 1;
	z *= y;
	y *= 0;
	y += w;
	y += 15;
	y *= x;
	z += y;
	return std::vector<int64_t>({x,y,z,w});
}

std::vector<int64_t> monad8(int64_t number, int64_t x, int64_t y, int64_t z, int64_t w){
	w = number;
	x *= 0;
	x += z;
	x = x % 26;
	z /= 1;
	x += 11;
	x = x == w ? 1 : 0;
	x = x == 0 ? 1 : 0;
	y *= 0;
	y += 25;
	y *= x;
	y += 1;
	z *= y;
	y *= 0;
	y += w;
	y += 10;
	y *= x;
	z += y;
	return std::vector<int64_t>({x,y,z,w});
}

std::vector<int64_t> monad9(int64_t number, int64_t x, int64_t y, int64_t z, int64_t w){
	w = number;
	x *= 0;
	x += z;
	x = x % 26;
	z /= 26;
	x += -15;
	x = x == w ? 1 : 0;
	x = x == 0 ? 1 : 0;
	y *= 0;
	y += 25;
	y *= x;
	y += 1;
	z *= y;
	y *= 0;
	y += w;
	y += 2;
	y *= x;
	z += y;
	return std::vector<int64_t>({x,y,z,w});
}

std::vector<int64_t> monad10(int64_t number, int64_t x, int64_t y, int64_t z, int64_t w){
	w = number;
	x *= 0;
	x += z;
	x = x % 26;
	z /= 1;
	x += 10;
	x = x == w ? 1 : 0;
	x = x == 0 ? 1 : 0;
	y *= 0;
	y += 25;
	y *= x;
	y += 1;
	z *= y;
	y *= 0;
	y += w;
	y += 0;
	y *= x;
	z += y;
	return std::vector<int64_t>({x,y,z,w});
}

std::vector<int64_t> monad11(int64_t number, int64_t x, int64_t y, int64_t z, int64_t w){
	w = number;
	x *= 0;
	x += z;
	x = x % 26;
	z /= 1;
	x += 12;
	x = x == w ? 1 : 0;
	x = x == 0 ? 1 : 0;
	y *= 0;
	y += 25;
	y *= x;
	y += 1;
	z *= y;
	y *= 0;
	y += w;
	y += 0;
	y *= x;
	z += y;
	return std::vector<int64_t>({x,y,z,w});
}

std::vector<int64_t> monad12(int64_t number, int64_t x, int64_t y, int64_t z, int64_t w){
	w = number;
	x *= 0;
	x += z;
	x = x % 26;
	z /= 26;
	x += -4;
	x = x == w ? 1 : 0;
	x = x == 0 ? 1 : 0;
	y *= 0;
	y += 25;
	y *= x;
	y += 1;
	z *= y;
	y *= 0;
	y += w;
	y += 15;
	y *= x;
	z += y;
	return std::vector<int64_t>({x,y,z,w});
}

std::vector<int64_t> monad13(int64_t number, int64_t x, int64_t y, int64_t z, int64_t w){
	w = number;
	x *= 0;
	x += z;
	x = x % 26;
	z /= 26;
	x += 0;
	x = x == w ? 1 : 0;
	x = x == 0 ? 1 : 0;
	y *= 0;
	y += 25;
	y *= x;
	y += 1;
	z *= y;
	y *= 0;
	y += w;
	y += 15;
	y *= x;
	z += y;
	return std::vector<int64_t>({x,y,z,w});
}

