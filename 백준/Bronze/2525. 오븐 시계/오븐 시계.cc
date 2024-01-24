#include <iostream>
using namespace std;

int main()
{
    int now_time;
    int now_minute;
    int after_time;
    int after_minute;
    int cook_time;

    cin >> now_time;
    cin >> now_minute;
    cin >> cook_time;

    after_minute = now_minute + cook_time;
    after_time = now_time + (after_minute/60);
    after_minute = after_minute % 60;
    if (after_time >= 24) { after_time %= 24; }

    cout << after_time << " " << after_minute << endl;

    return 0;
}