import java.util.*;
import java.io.*;

class 2110 {
    private static int binarySearch (int[] arr, int c) {
        int result = 0;

        int start = 0;
        int end = arr[arr.length-1] - arr[0];

        int mid = 0;
        while(start<=end) {
            mid = (start + end) / 2;
            //mid가 거리라고 가정하고 거리에 따른 횟수가 c이상 인지
            //ex) 거리 3 => ok 3저장 , 거리 1 => ok 1 저장 ???
            //있으면, dis가 올라가야 됨, 따라서 start = mid + 1;
            if(check(arr, mid, c)) {
                result = mid;
                start = mid + 1;
            }
            else
                end = mid - 1;
        }
        return result;
    }
    private static boolean check(int[] arr, int dis, int c) {
        int cnt = 1;
        int temp = arr[0];
        for (int i = 1; i < arr.length; i++) {
            //차를 통한 거리 구해야 됨
            if(dis <= arr[i] - temp) {
                cnt++;
                temp = arr[i];
            }
        }
        return (cnt >= c);
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine(), " ");
        int n = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int[] arr = new int[n];

        for (int i = 0; i < n; i++)
            arr[i] = Integer.parseInt(br.readLine());
        Arrays.sort(arr);

        bw.write(String.valueOf(binarySearch(arr, c)));
        bw.flush();
        bw.close();
        br.close();
    }
}
