import java.util.*;
import java.io.*;

class 2230 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine(), " ");
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[] arr = new int[n];

        for (int i = 0; i < n; i++)
            arr[i] = (Integer.parseInt(br.readLine()));

        Arrays.sort(arr);

        //투 포인터 알고리즘
        int i = 0;
        int j = 0;
        int min = Integer.MAX_VALUE;
        int temp;
        while(i < n) {
            temp = Math.abs(arr[i]-arr[j]);
            if(temp < m)
                i++;
            else {
                if(temp <= min)
                    min = temp;
                if(temp == m)
                    break;
                j++;
            }
        }
        bw.write(String.valueOf(min));
        bw.flush();
        bw.close();
        br.close();

    }
}
