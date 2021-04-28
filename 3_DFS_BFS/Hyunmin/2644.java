import java.util.*;
import java.io.*;

class 2644 {
    public static ArrayList<ArrayList<Integer>> arr;
    public static int[] visited;
    public static int number = 1;
    public static int bfs(int start, int end) {
        Queue<Integer> q = new LinkedList<>();
        q.offer(start);
        while (!q.isEmpty()) {
            int poll = q.poll();
            if(visited[poll]==0) {
                visited[poll] = number;
                if(poll==end)
                    return visited[poll]-1;
            }
            boolean check = false;
            for (int i : arr.get(poll)) {
                if(visited[i] == 0) {       //다음게 있으면
                    check = true;
                    bfs(i, end);
                }
            }
            if(check)
                number++;
        }
        return visited[end];
    }

    public static int dfs(int start, int end, int prev) {
        if(visited[start] == -1) {
            visited[start] = prev;
            for (int i : arr.get(start)) {
                if(visited[i] == -1)     //다음게 있으면
                    dfs(i, end, prev + 1);
            }
        }
        //visited[end]에 값이 저장이 되지 않고 0이라면 start가 end까지 도달하지 못한 것임
        //도달했다면 결과값이 visited[end]에 저장되어 있을 것.
        return visited[end];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        arr = new ArrayList<>();

        int n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine(), " ");
        int start = Integer.parseInt(st.nextToken());
        int end = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(br.readLine());
        visited = new int[n+1];
        Arrays.fill(visited, -1); //초기값 -1로 설정 해주면 dfs결과 값을 재 확인할 필요 없어짐

        while (n-- >= 0)
            arr.add(new ArrayList<>());

        while (m-- > 0) {
            st = new StringTokenizer(br.readLine(), " ");
            int i = Integer.parseInt(st.nextToken());
            int j = Integer.parseInt(st.nextToken());

            arr.get(i).add(j);
            arr.get(j).add(i);
        }

        System.out.println(dfs(start, end, 0));

        br.close();
    }
}




