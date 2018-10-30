#include<stdio.h>

int main(){
    int x, y, z, j, a, o;
    scanf("%d",&a);
    while(a--){
        int count = 0;
        scanf("%d",&x);
        scanf("%d",&y);
        for(j=0; j<x; j++){
            scanf("%d",&z);
            if(z == 1)
                count++;
        }
        o = x - count;
        if(o <= y)
           printf("YES\n");
        else
           printf("NO\n");
    }
    return 0;
}
