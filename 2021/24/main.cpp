#include "parsed_inp.h"
#include <ctime>
#include <unordered_map>
#include <string>
#include <cstdio>
#include <cmath>

std::vector<monad_func> funky = { monad1, monad2, monad3, monad4, monad5, monad6, monad7, monad8, monad9, monad10, monad11, monad12, monad13 };

std::string tokey(std::vector<int64_t> states) {
	return std::to_string(states[1])+ " " + std::to_string(states[2]);
}


void max() {
	std::unordered_map<std::string, std::vector<int64_t>> cache_cur = {};
	std::unordered_map<std::string, std::vector<int64_t>> cache_buf = {};

	int64_t start = clock();

	for (int i = 9; i > 0; i--) {
		auto vec = monad0(i, 0, 0, 0, 0);
		auto key = tokey(vec);
		if (cache_buf.find(key) == cache_buf.end())
			cache_buf.insert({ key, {vec[1],vec[2],i} });
	}

	cache_cur = cache_buf;
	cache_buf = {};

	for (auto& f : funky) {
		printf("New funky\n");
		for (auto& states : cache_cur) {
			for (int i = 9; i > 0; i--) {
				auto vec = f(i, 0, states.second[0], states.second[1], 0);
				auto key = tokey(vec);
				int64_t num = states.second[2] * 10 + i;
				if (cache_buf.find(key) == cache_buf.end())
				{
					cache_buf.insert({ key, {vec[1],vec[2], num} });
				}
				else if (cache_buf[key][2] < num) {
					cache_buf[key][2] = num;
				}
			}
		}
		cache_cur = cache_buf;
		cache_buf = {};
	}

	int64_t res = 0;

	for (auto& states : cache_cur) {
		if (states.second[1] == 0) res = std::max(res, states.second[2]);
	}

	printf("Res: %llu. Elapsed: %llu s. States: %llu\n", res, (clock() - start) / CLOCKS_PER_SEC, cache_cur.size());
}

void min() {
	std::unordered_map<std::string, std::vector<int64_t>> cache_cur = {};
	std::unordered_map<std::string, std::vector<int64_t>> cache_buf = {};

	int64_t start = clock();

	for (int i = 1; i < 10; i++) {
		auto vec = monad0(i, 0, 0, 0, 0);
		auto key = tokey(vec);
		if (cache_buf.find(key) == cache_buf.end())
			cache_buf.insert({ key, {vec[1],vec[2],i} });
	}

	cache_cur = cache_buf;
	cache_buf = {};

	for (auto& f : funky) {
		printf("Next funky\n");
		for (auto& states : cache_cur) {
			for (int i = 1; i < 10; i++) {
				auto vec = f(i, 0, states.second[0], states.second[1], 0);
				auto key = tokey(vec);
				int64_t num = states.second[2] * 10 + i;
				if (cache_buf.find(key) == cache_buf.end())
				{
					cache_buf.insert({ key, {vec[1],vec[2], num} });
				}
				else if (cache_buf[key][2] > num) {
					cache_buf[key][2] = num;
				}
			}
		}
		cache_cur = cache_buf;
		cache_buf = {};
	}

	int64_t res = 99999999999999;

	for (auto& states : cache_cur) {
		if (states.second[1] == 0) res = std::min(res, states.second[2]);
	}


	printf("Res: %llu. Elapsed: %llu s. States: %llu\n", res, (clock() - start) / CLOCKS_PER_SEC, cache_cur.size());
}


int main() {
	max();
	min();

	getc(stdin);

	return 0;
}