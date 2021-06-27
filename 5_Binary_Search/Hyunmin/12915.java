import java.util.*;
import java.io.*;

class 12915 {
    private static int binarySearch (int[] arr, int max) {
        int result = 0;
        int start = 0;
        int end = max;
        int mid = 0;
        while(start<=end) {
            mid = (start + end) / 2;
            if(calculate(arr, mid)) {
                result = mid;
                start = mid + 1;
            }
            else
                end = mid - 1;
        }
        return result;
    }
    private static boolean calculate(int[] arr, int mid) {
        int[] temp = arr.clone();
        for (int i = 0; i < mid; i++) {
            //E경우
            if(temp[0] > 0)
                temp[0]--;
            else if(temp[1] > 0)
                temp[1]--;
            else
                return false;
            //M경우
            if(temp[2] > 0)
                temp[2]--;
            //더 큰 것을 줄여야 함
            else if ((temp[1] > 0) || (temp[3] > 0)) {
                if(temp[1] >= temp[3])
                    temp[1]--;
                else
                    temp[3]--;
            }
            else
                return false;
            //H경우
            if(temp[4] > 0)
                temp[4]--;
            else if(temp[3] > 0)
                temp[3]--;
            else
                return false;
        }
        return true;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int[] arr = new int[5];
        st = new StringTokenizer(br.readLine(), " ");

        int max = 0;
        for (int i = 0; st.hasMoreTokens(); i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            max += arr[i];
        }
        //E, EM, M, MH, H가 주어진다. (0 ≤ E, EM, M, MH, H ≤ 100,000)
        //1부터 100,000까지 탐색하는 것이 시간이 더 빨랐다.
        bw.write(String.valueOf(binarySearch(arr, max)));

        bw.flush();
        bw.close();
        br.close();
    }
}
