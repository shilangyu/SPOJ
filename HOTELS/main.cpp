#include <iostream>

using namespace std;

int solve(int arr[], int n, int sum)
{
	int curr_sum = arr[0], max_sum = 0, start = 0, i;
	for (i = 1; i <= n; i++)
	{
		while (curr_sum > sum && start < i - 1)
		{
			curr_sum = curr_sum - arr[start];
			start++;
		}
		if (max_sum < curr_sum)
			max_sum = curr_sum;

		curr_sum = curr_sum + arr[i];
	}

	return max_sum;
}

int main()
{
	int n, m;
	cin >> n >> m;
	int a[n];
	for (int i = 0; i < n; i++)
	{
		cin >> a[i];
	}
	cout << solve(a, n, m) << endl;
}
