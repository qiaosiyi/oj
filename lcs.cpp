//2019年02月01日16:25:21
//qsy
//c++
///$ g++ lcs.cpp
///$ ./a.out
#include <iostream>
#include <cstring>
#include <vector>
#include <deque>
#include <map>
#include <string>
#include <algorithm>
using namespace std;
//求两个字符串最长公共子序列的长度，以及输出任意解。
//动态规划，递归公式。计算复杂度O(n*m),输出复杂度O(n+m)。
int main(){
	string sa,sb;
	int a,b;
	cout << "intput 2 string, will get longest common substring:"<<endl;
	cin >> sa;
	cin >> sb;

	b = sb.size();
	a = sa.size();
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
				z[i][j] = max(z[i][j-1],z[i-1][j]);//递归公式二
			}
		}
	}
	// for(int i = 0; i < b + 1; i++){//打印动规矩阵：中间子问题答案。
	// 	for(int j = 0; j < a + 1; j++){
	// 		cout << " " << z[i][j];
	// 	}
	// 	cout << endl;
	// }
	int i = b-1;
	int j = a-1;
	int n = z[b][a];
	char lcs[n];
	while(n){//根据动态规划矩阵和递归公式反推，求得一个子序列的实例。
		if(sb[i] == sa[j]){
			lcs[n - 1] = sb[i];//递归公式一
			i--;j--;n--;
			continue;
		}
		if(sb[i] != sa[j]){
			if(z[i][j+1] > z[i+1][j]){//递归公式二
				i--;
			}else{//else中包含z == z，意味着递推分支,此处默认j--，那就是当i代表行，j代表列，列减减表示向水平左方向去倒推分支。
				j--;
			}
		}
	}
	for(int i = 0; i < z[b][a]; i++){
		cout << lcs[i];
	}
	cout << endl;
	cout << z[b][a]<<endl;
	return 0;
}
