import java.util.*;
import java.io.*;

class dp4 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        //숫자를 일일이 조합하여 계산함
        int n = Integer.parseInt(br.readLine());
        int[] dp = new int[1000];

        dp[0] = 0;
        dp[1] = 1;
        dp[2] = 3;
        //4 = 11

        for (int i = 3; i < n + 1; i++)
            dp[i] = dp[i-2] * 2 + dp[i-1];

        bw.write(String.valueOf(dp[n]%796796));

        bw.flush();
        bw.close();
        br.close();
    }
}
