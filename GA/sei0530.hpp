#pragma once 
#include <vector>
#include <string>
using namespace std;

class sei0530{
public:
	vector<vector<string>> csv_read(string filename);
	void print_vector(vector<vector<string>> lala);
	vector<string> split(string& input, char delimiter);
};