import java.util.*;
import java.io.*;

class 17271 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine(), " ");
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        double[] dp = new double[10005];

        //dp가 하나 씩 올라가는데 올라가는 값을 M으로 생각하지 않고, N으로 생각!
        //dN 0 = ?
        //dN 1 = 1
        //dN 2 = 1
        //dN 3 = 2
        //dN 4 = 3
        //dN 5 = 4

        //= > dN = dN-1 + dN-3 ( 3==m)

        //dN 0 = ?
        //dN 1 = 1
        //dN 2 = 1
        //dN 3 = 2 //여기서 식 적용시 dN 0 = 1이 되어야함
        //dN 4 = 3
        //dN 5 = 4

        dp[0] = 1;
        dp[1] = 1;

        for (int i = 2; i < n + 1 ; i++) {
            dp[i] = (dp[i-1] + (i-m >= 0 ? dp[i-m] : 0))%1000000007; //나머지를 저장해야함
        }
        bw.write(String.format("%.0f\n",dp[n] ));
        

        bw.flush();
        bw.close();
        br.close();
    }
}

