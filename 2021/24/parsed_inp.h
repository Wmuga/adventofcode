#pragma once
#include <vector>
#include <inttypes.h>
#include <functional>

std::vector<int64_t> monad0(int64_t number, int64_t x, int64_t y, int64_t z, int64_t w);
std::vector<int64_t> monad1(int64_t number, int64_t x, int64_t y, int64_t z, int64_t w);
std::vector<int64_t> monad2(int64_t number, int64_t x, int64_t y, int64_t z, int64_t w);
std::vector<int64_t> monad3(int64_t number, int64_t x, int64_t y, int64_t z, int64_t w);
std::vector<int64_t> monad4(int64_t number, int64_t x, int64_t y, int64_t z, int64_t w);
std::vector<int64_t> monad5(int64_t number, int64_t x, int64_t y, int64_t z, int64_t w);
std::vector<int64_t> monad6(int64_t number, int64_t x, int64_t y, int64_t z, int64_t w);
std::vector<int64_t> monad7(int64_t number, int64_t x, int64_t y, int64_t z, int64_t w);
std::vector<int64_t> monad8(int64_t number, int64_t x, int64_t y, int64_t z, int64_t w);
std::vector<int64_t> monad9(int64_t number, int64_t x, int64_t y, int64_t z, int64_t w);
std::vector<int64_t> monad10(int64_t number, int64_t x, int64_t y, int64_t z, int64_t w);
std::vector<int64_t> monad11(int64_t number, int64_t x, int64_t y, int64_t z, int64_t w);
std::vector<int64_t> monad12(int64_t number, int64_t x, int64_t y, int64_t z, int64_t w);
std::vector<int64_t> monad13(int64_t number, int64_t x, int64_t y, int64_t z, int64_t w);

typedef std::function<std::vector<int64_t>(int64_t, int64_t, int64_t, int64_t, int64_t)> monad_func;
