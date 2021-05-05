import java.util.*;
import java.io.*;

class 10815 {
    public static boolean binarySearch(int[] arr, int target) {
        int mid;
        int left = 0;
        int right = arr.length - 1;

        while (right >= left) {
            mid = (right + left) / 2;
            if (target == arr[mid])
                return true;
            if (target < arr[mid])
                right = mid - 1;
            else
                left = mid + 1;
        }
        return false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        int[] nArr = new int[n];

        st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < n; i++)
            nArr[i] = Integer.parseInt(st.nextToken());
        Arrays.sort(nArr);

        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < m; i++) {
            if(binarySearch(nArr, Integer.parseInt(st.nextToken())))
                bw.write('1');
            else
                bw.write('0');
            bw.write(' ');
        }

        bw.flush();
        bw.close();
        br.close();

    }
}
