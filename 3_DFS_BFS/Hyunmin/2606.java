import java.util.*;
import java.io.*;

class 2606 {
    public static ArrayList<ArrayList<Integer>> arr;
    public static int count = 0 ;
    public static boolean[] visited;

    //dfs
    public static boolean dfs(int x) {

        //재귀함수 사용
        if (x < 1 && x >= arr.size())
            return false;

        if (!visited[x]) {
            count++;
            visited[x] = true;
        }

        for (int j = 0; j < arr.get(x).size(); j++) {
            int y = arr.get(x).get(j);
            if(!visited[y])
                dfs(y);
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        arr = new ArrayList<>();
        visited = new boolean[n + 1];

        for (int i = 0; i < n + 1; i++)
            arr.add(new ArrayList<>());

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int front = Integer.parseInt(st.nextToken());
            int back = Integer.parseInt(st.nextToken());

            arr.get(front).add(back);
            arr.get(back).add(front);
        }

        for (int i = 1; i < n + 1; i++)
            Collections.sort(arr.get(i));

        //1번째 컴퓨터 제외 하고 Count
        visited[1] = true;

        dfs(1);
        System.out.println(count);

        br.close();
    }
}



