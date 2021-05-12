import java.util.*;
import java.io.*;

class binarySearch3 {
    private static int binarySearch (int[] arr, int key) {
        int start = 0;
        int end = arr[arr.length - 1];
        int mid = 0;
        int total = 0;
        int result = 0;

        while(start<=end) {
            mid = (start + end) / 2;
            total = getTotal(arr, mid);

            if (total < key)
                end = mid - 1;
                //더 클 때 저장 해 놓는다.
            else {
                result = mid;
                start = mid + 1;
            }
//            System.out.println(mid + " " + total + " "  + result);
        }
        return result;
    }
    private static int getTotal(int[] arr, int h) {
        int total = 0;
        for (int i : arr) {
            if (i > h)
                total += i - h;
        }
        return total;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine(), " ");
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine(), " ");
        int[] nArr = new int[n];
        for (int i = 0; st.hasMoreTokens(); i++)
            nArr[i] = Integer.parseInt(st.nextToken());

        Arrays.sort(nArr);
        bw.write(String.valueOf(binarySearch(nArr, m)));
        bw.flush();
        bw.close();
        br.close();
    }
}
