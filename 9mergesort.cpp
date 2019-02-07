//2019年02月07日16:25:34
//qsy
//c++
///$ g++ 9mergesort.cpp
///$ ./a.out
#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <cstring>
#include <cstdio>
#include <vector>
#include <deque>
#include <map>
#include <string>
#include <algorithm>
using namespace std;
//归并排序。
//分治，递归，归并操作。

void merge(int *a, int *l, int lcount, int *r, int rcount){//以下几步，总和称为归并操作
	int i = 0, j = 0, k = 0;
	while(j < lcount && k < rcount){//两个分支都没有归并操作结束
		if(l[j] < r[k]){
			a[i++] = l[j++];
		}else{
			a[i++] = r[k++];
		}
	}
	while(j < lcount){//其中一个分支已经归并操作结束
		a[i++] = l[j++];
	}
	while(k < rcount){//其中一个分支已经归并操作结束
		a[i++] = r[k++];
	}
}

void mergesort(int *a, int number){
	int mid, i, *l, *r;
	if(number < 2) return;//不需要对a数组进行排序，直接退出。否则需要分治，并且排序。

	mid = number/2;

	l = new int[mid];
	r = new int[number - mid];

	for(i = 0; i < mid; i++) l[i] = a[i];//新建两个子分支的实质内容。
	for(i = mid; i < number; i++) r[i - mid] = a[i];

	mergesort(l, mid); //递归
	mergesort(r, number - mid);
	merge(a, l, mid, r, number - mid);

	delete [] r;
	delete [] l;
}

int main(){
	int temp = 0;
	int qsize = 0;
	srand((unsigned)time(NULL));  
	qsize = rand()%30;
	int a[qsize];

	for(int i = 0; i < qsize;i++ ) {
		temp = rand()%1000;
        cout << temp << ' ';  
        a[i] = temp;
	}
	cout << endl;

	mergesort(a, qsize);

	for (int i = 0; i < qsize; i++){
		cout << a[i] << ' ';//输出结果
	}
	cout << endl;
	
	return 0;
}
