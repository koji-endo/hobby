#include "sei0530.hpp"
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

vector<string> sei0530::split(string& input, char delimiter)
{
    istringstream stream(input);
    string field;
    vector<string> result;
    while (getline(stream, field, delimiter)) {
        result.push_back(field);
    }
    return result;
}
vector<vector<string>> sei0530::csv_read(string filename){
    ifstream ifs(filename);
    string line;
    vector<vector<string>> returnee;
    while (getline(ifs, line)) {
        if(line[0]=='#'){
            cout<< "hit" <<endl;
        }else{
            vector<string> strvec = split(line, ' ');
            returnee.push_back(strvec);
        }
    }
    return returnee;
}
void sei0530::print_vector(vector<vector<string>> lala){
    for_each(begin(lala), end(lala), 
        [&](vector<string> la){ 
            for_each(begin(la), end(la), 
                [&](string i) {
                    cout<<i<<" ";
                }
            );
            cout<<endl;
        }
    );
}