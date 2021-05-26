import java.util.*;
import java.io.*;

class 5582 {
//    String a = br.readLine();
//    int aLen = a.length();
//    String b = br.readLine();
//    int bLen = b.length();
//    int result = 0;
//    StringBuilder sb;
//        for (int i = 0; i < aLen; i++) {
//        sb = new StringBuilder();
//        for (int k = i; k < aLen; k++) {
//            sb.append(a.charAt(k));
//            if(b.contains(sb)) {
//                if(result < sb.toString().length())
//                    result = sb.toString().length();
//            }
//        }
//    }
//        System.out.println(result);
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        String a = br.readLine();
        int aLen = a.length();
        String b = br.readLine();
        int bLen = b.length();
        int[][] dp = new int[aLen][bLen]; //dp인가 ?

        int max = 0;
        for (int i = 0; i < bLen; i++) {
            for (int j = 0; j < aLen; j++) {
                if(b.charAt(i)==a.charAt(j)) {
                    if(j-1>=0&&i-1>=0&&dp[j-1][i-1]!=0)
                        dp[j][i] = dp[j-1][i-1]+1;
                    else
                        dp[j][i] = 1;
                    max = Math.max(dp[j][i], max);
                }
            }
        }

        bw.write(String.valueOf(max));

        bw.flush();
        bw.close();
        br.close();
    }
}

