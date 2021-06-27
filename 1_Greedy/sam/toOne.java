import java.io.*;
import java.util.*;

public class toOne {
    public static void main(String[] args) throws IOException {

        int n, k, result = 0;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        //N X M 행렬인지 입력
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        while(n>1) {
            if (n % k == 0) {
                n /= k;
            }
            else {
                n -= 1;
            }
            result++;
        }


        bw.write(String.valueOf(result));

        bw.flush();
        bw.close();
        br.close();
    }
}

