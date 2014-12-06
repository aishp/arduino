//displays system time on terminal with a delay of 2 seconds 

#include <stdio.h>
#include <time.h>
#include<unistd.h>

int main()
{
    time_t timer;
    char buffer[25];
    struct tm* tm_info;
    int i,j;
    
    
    
    while(1)
    {
       // NSThread sleepForTimeInterval:5.0;
        time(&timer);
        tm_info = localtime(&timer);
    strftime(buffer, 25, "%Y:%m:%d %H:%M:%S", tm_info);
    puts(buffer);
       /* for(i=0;i<20000;i++)
        {
            for(j=0;j<10000;j++);
        }*/
       // sleepForTimeInterval(2);
        sleep(2);
        
    }
    
    return 0;
}
