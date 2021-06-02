import java.util.*;
import java.io.*;

class dp5 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine(), " ");
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] d = new int[n]; //N개 종류의 화폐들 저장
        for (int i = 0; i < n; i++)
            d[i] = Integer.parseInt(br.readLine());

        int[] dp = new int[m+1];
        Arrays.fill(dp, Integer.MAX_VALUE);

        //d = {2, 3, 5}

        //       0   1   2   3   4   5   6   7
        //dp = {-1, -1, -1, -1, -1, -1, -1, -1}

        //       0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15
        //dp = {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1}

        //초기 값 -1 X => 크게 잡아야 대소 비교가 가능
        // 2, 3, 5 순서로 최소값 넣어줌
        for(int k = 0; k < n; k++) {  //3개의 화폐 2, 3, 5
            for (int i = 1; i < m + 1; i++) { //  1 - 7까지
                if(i%d[k]==0&&(i/d[k]<dp[m]))
                    dp[i] = i/d[k];          //cnt
            }
        }

        //투 포인터 ? => dp[i-d[k]] + dp[d[k]]
        for (int i = 1; i < m + 1; i++) { // 1- 7까지
            for(int k = 0; k < n; k++) {  //3개의 화폐 2, 3, 5
                //지금 숫자가 화폐중 최소 숫자보다 작으면 연산 X
                // 계산 진행 가능 조건
                if(i-d[k] >= 0 && dp[i-d[k]]!=Integer.MAX_VALUE) {
                    if(dp[i-d[k]] + dp[d[k]] < dp[i])
                        dp[i] = dp[i-d[k]] + dp[d[k]];
                }
                //추가 고려사항 ?
            }
        }

        if(dp[m]==Integer.MAX_VALUE)
            bw.write("-1");
        else
            bw.write(String.valueOf(dp[m]));

        bw.flush();
        bw.close();
        br.close();
    }
}

