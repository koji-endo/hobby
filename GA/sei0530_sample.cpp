#include "sei0530.hpp"
#include <vector>
#include <string>

int main(){
    vector<vector<string>> lala;
    sei0530 sei;
    lala=sei.csv_read("connect_sei0530.txt");
    sei.print_vector(lala);
}