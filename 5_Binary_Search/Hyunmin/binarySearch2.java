import java.util.*;
import java.io.*;

class binarySearch2 {
    private static boolean binarySearch (int[] arr, int key) {
        int start = 0;
        int end = arr.length - 1;
        int mid;
        while(start<=end) {
            mid = (start + end) / 2;
            if(arr[mid] == key)
                return true;
            if(arr[mid] < key)
                start = mid + 1;
            else
                end = mid - 1;
        }
        return false;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine(), " ");
        int[] nArr = new int[n];
        for (int i = 0; st.hasMoreTokens(); i++)
            nArr[i] = Integer.parseInt(st.nextToken());
        Arrays.sort(nArr);

        br.readLine();
        st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; st.hasMoreTokens(); i++) {
            if(binarySearch(nArr, Integer.parseInt(st.nextToken())))
                bw.write("yes");
            else
                bw.write("no");
            bw.write(' ');
        }

        bw.flush();
        bw.close();
        br.close();
    }
}
