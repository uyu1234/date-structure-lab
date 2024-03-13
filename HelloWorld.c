#include <stdio.h>

int main()
{
    printf("Hello World!");
}

#define Max_ELEMENTS 100
int score[Max_ELEMENTS];

int find_max_score(int n)
{
    int i, tmp;
    tmp = score[0];
    for (i = 1; i < n; i++)
    {
        if (score[i] > tmp)
        {
            tmp = score[i];
        }
    }
    return tmp;
}