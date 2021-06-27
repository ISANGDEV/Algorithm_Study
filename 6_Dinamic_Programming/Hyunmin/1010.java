import java.util.*;
import java.io.*;

class Main {
    private static void factorial(double[] arr) {
        arr[0] = 1;
        for (int i = 1; i < 30; i++)
            arr[i] = i * arr[i-1];
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int t = Integer.parseInt(br.readLine());
        double[] answer = new double[t];
        double[] facNum = new double[30];

        factorial(facNum);

        int idx = 0;
        while(t-- > 0) {
            st = new StringTokenizer(br.readLine(), " ");
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            answer[idx++] = facNum[m] / (facNum[n] * facNum[m - n]);
        }
        for(double temp: answer)
            bw.write(String.format("%.0f", temp)+'\n');

        bw.flush();
        bw.close();
        br.close();
    }
}

