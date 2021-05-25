import java.util.*;
import java.io.*;

class 2193 {
//    private static int topDown(int x, int[] input) {
//        return 0;
//    }
//    private static int bottomUp(int x, int[] input) {
//        return 0;
//    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        long[] arr = new long[n+1];
        if(n <= 2)
            bw.write('1');
        else {

            arr[1] = 1;
            arr[2] = 1;

            for (int i = 3; i < n + 1; i++) {
                arr[i] = arr[i-1] + arr[i-2];
            }
            bw.write(String.valueOf(arr[n]));
        }

        bw.flush();
        bw.close();
        br.close();
    }
}

