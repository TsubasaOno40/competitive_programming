#include <string.h>

//sortされた配列を入れるとitemの位置を二分探索で探してくれる。

void binary_search(int *str, int item)
{
	int low;
	int high;
	int mid;
	int guss;

	low = 0;
	high = strlen(str) - 1;
	while (low <= high)
	{
		mid = (low + high) / 2;
		guss = str[mid];
		if (guss == item)
			return (mid);
		if (guss > item)
			high = mid - 1;
		else
			low = mid + 1;
	}
	return (NULL);
}

int main(void)
{
	return (0);
}