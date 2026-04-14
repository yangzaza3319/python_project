#include <stdio.h>

int main()
{
    int a = 10;           // 整数类型
    printf("%d\n", a);   // 输出：10

    char *str = "Hello"; // 字符串类型
    printf("%s\n", str); // 正确的输出：Hello

    float b = 3.14;       // 浮点数类型
    printf("%f\n", b);   // 输出：3.140000

    char c = 'A';        // 字符类型
    printf("%c\n", c);   // 输出：A

    return 0;
}