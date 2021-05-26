
import java.util.*;
import java.io.*;

class Main {

    //Top-Down
    private static int topDown(int x, int cnt) {
        int minCnt=Integer.MAX_VALUE;

        if(x==1)
            return cnt;

        if(x%5==0)
            minCnt = Math.min(topDown(x/5, cnt+1), minCnt);
        if(x%3==0)
            minCnt = Math.min(topDown(x/3, cnt+1), minCnt);
        if(x%2==0)
            minCnt = Math.min(topDown(x/2, cnt+1), minCnt);

        minCnt = Math.min(topDown(x-1, cnt+1), minCnt);

        return minCnt;
    }
    private static int bottomUp(int x) {
    //**. 문제 풀때, x를 5로 잡고 x를 2부터 올라가면서 계산해보자. (1은 횟수가 0임)**

    //. dpTable에는 나누어지는 것들, 나누어지는 숫자라면 나누고 연산횟수를 dpTable에 +1하여 저장한뒤,  마지막에 dpTable[x]에 저장해준다.

    //. 이때 x가 0부터 늘어나기 때문에 이전에 계산한 결과 인 dpTable[x/5]에 현재 값을 만들기 위해 +1 을 더한 것과 -1한 횟수가 저장된 값을 비교하여 최종적으로 저장.

    //→메모이제이션 기법 적용 됨.

        int[] dpTable = new int[x+1];
        //숫자 1인 경우 cnt 0이여야하고 정수 배열 초기화시 0이 들어가기 때문에 2부터 시작.
        int min;
        for (int i = 2; i < x + 1; i++) {
            //i = 1, 2, 3, 4, 5로 bottom top 방식으로 생각.

            //dpTable[i] 에다가는 i가 되기 위한 최소 "횟수"를 저장하려는 것임.
            //최소 "횟수"를 저장하려면 4가지 연산 중 나머지가 0인 연산들 중에서 최소 "횟수"를 비교(min, dpTable[di/?] + 1 (i의 횟수가 되려면 여기에 횟수 + 1을 해줘야함))하여 마지막에 dpTable[i]에 횟수를 넣으면 된다.
            //min -> dpTable[i]
            dpTable[i] = dpTable[i-1] + 1; //ex) dpTable[2] 일 때 dpTable[1]은 0 이므로 2에서 1을 만들기 위해서는 2에서 1을 빼야하며, 횟수인 cnt는 1 더해줘야하기 때문에 arr[2]에는 arr[1]+1;
            if(i%2==0)
                dpTable[i] = Math.min(dpTable[i], dpTable[i/2] + 1);
            if(i%3==0)                                 //마찬가지로 나누기 연산을 했으므로 연산횟수가 늘어났다는 의미에서 cnt + 1을 해줘야 한다.
                dpTable[i] = Math.min(dpTable[i], dpTable[i/3] + 1);
            if(i%5==0)                                 //dpTable[i/5]값을 사용하므로 메모리제이션이 된다. 0부터 숫자가 올라가기 때문에 나눈 결과인 index가 이전에 이미 계산했던 값일 것이므로 비교를하고 거기에 횟수 + 1을 한다.
                dpTable[i] = Math.min(dpTable[i], dpTable[i/5] + 1) ; //위에서 1뺀 값이 초기화 된 셈이고,  1뺀값,5나눈값,3나눈값,2나눈값,끼리 값을 비교해서 가장 작은것을 dpTable[i]에 넣어야한다.


        }
        return dpTable[x];
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        int x = Integer.parseInt(br.readLine());

        bw.write(String.valueOf(bottomUp(x)));

        bw.flush();
        bw.close();
        br.close();
    }
}

