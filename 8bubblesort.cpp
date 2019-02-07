//2019年02月07日16:25:34
//qsy
//c++
///$ g++ 8bubblesort.cpp
///$ ./a.out
#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <cstring>
#include <vector>
#include <deque>
#include <map>
#include <string>
#include <algorithm>
using namespace std;
//起泡排序。
//随机生成一组数字，使用起泡排序，从小到大。
int main(){
	vector<int>queue;
	int temp = 0;
	int qsize = 0;
	srand((unsigned)time(NULL));  
	qsize = rand()%30;
	for(int i = 0; i < qsize;i++ ) {
		temp = rand()%1000;
        cout << temp << ' ';  
        queue.push_back(temp);//生成随机序列
	}
	cout << endl;

	for (int i = 0; i < queue.size() - 1; i++){//起泡排序
		for(int j = 0; j < queue.size() - 1 - i; j++){
			if(queue[j] > queue[j + 1]){
				swap(queue[j],queue[j+1]);
			}
		}
	}

	for (int i = 0; i < qsize; i++){
		cout << queue[i] << ' ';//输出结果
	}
	cout << endl;
	return 0;
}
