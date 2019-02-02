//2019年02月02日12:08:22
//qsy
//c++
///$ g++ 7alcs.cpp
///$ ./a.out
#include <iostream>
#include <cstring>
#include <vector>
#include <deque>
#include <map>
#include <string>
#include <algorithm>
using namespace std;
//求两个字符串最长子字串，并输出。
//动态规划，递归公式。计算复杂度O(n*m)。
int main(){
	string sa,sb;
	int a,b;
	cout << "intput 2 string, will get longest common substring:"<<endl;
	cin >> sa;
	cin >> sb;
	b = sb.size();
	a = sa.size();
	int max=0,maxi=0,maxj=0;
	int z[b+1][a+1];
	for (int i = 0; i < b+1; ++i){//初始化
		z[i][0] = 0;
	}
	for (int i = 0; i < a+1; ++i){
		z[0][i] = 0;
	}
	for(int i = 1; i < b + 1; i++){//双重循环，根据递归公式求解中间答案。
		for(int j = 1; j < a + 1; j++){
			if(sb[i-1] == sa[j-1]){
				z[i][j] = z[i - 1][j - 1] + 1;//递归公式一
			} else{
				z[i][j] = 0;//递归公式二
			}
			if(z[i][j]>max){
				max = z[i][j];
				maxi = i;
				maxj = j;
			}
		}
	}
	// for(int i = 0; i < b + 1; i++){//打印动规矩阵：中间子问题答案。
	// 	for(int j = 0; j < a + 1; j++){
	// 		cout << " " << z[i][j];
	// 	}
	// 	cout << endl;
	// }

	int n = max;
	char lcs[n];
	for(int i = 0; i < max; i++){
		lcs[n-i-1] = sb[maxi - i-1];
	}
	for(int i = 0; i < max; i++){
		cout << lcs[i];
	}
	cout << endl;
	cout << "max="<< max<<endl;
	return 0;
}
