import java.io.*;
import java.util.*;

public class NumberCard {
    public static void main(String[] args) throws IOException {

        int n, m, temp, result = 0;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        //N X M 행렬인지 입력
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        for (; n > 0; n--) {
            temp = 100001;
            StringTokenizer tempStr = new StringTokenizer(br.readLine());
            while (tempStr.hasMoreTokens()) {
                int temp2 = Integer.parseInt(tempStr.nextToken());
                if (temp > temp2)
                    temp = temp2;
            }
            if (result < temp)
                result = temp;
        }
        bw.write(String.valueOf(result));

        bw.flush();
        bw.close();
        br.close();
    }
}

