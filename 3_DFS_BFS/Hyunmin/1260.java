import java.util.*;
import java.io.*;

class 1260 {
    public static ArrayList<ArrayList<Integer>> arr;
    public static boolean[] visitedD;
    public static boolean[] visitedB;

    //dfs
    public static boolean dfs(int x) {

        //재귀함수 사용
        if (x < 1 && x >= arr.size())
            return false;

        if (!visitedD[x]) {
            System.out.print(x+" ");
            visitedD[x] = true;
        }

        for (int j = 0; j < arr.get(x).size(); j++) {
            int y = arr.get(x).get(j);

            if(!visitedD[y])
                dfs(y);
        }
        return true;
    }

    //bfs
    public static void bfs(int x) {
        Queue<Integer> q = new LinkedList<>();

        q.offer(x);

        while(!q.isEmpty()) {

            int xX = q.poll();

            if(!visitedB[xX]) {
                visitedB[xX] = true;
                System.out.print(xX + " ");
            }
            for (int j = 0; j < arr.get(xX).size(); j++) {
                int y = arr.get(xX).get(j);

                if(!visitedB[y])
                    q.offer(y);

            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        //간선 정보를 저장 어디 / Arraylist LinkedList ?


        int n = Integer.parseInt(st.nextToken()); //4
        int m = Integer.parseInt(st.nextToken()); //5
        int v = Integer.parseInt(st.nextToken()); //1

        arr = new ArrayList<>();
        visitedD = new boolean[n + 1]; // 0 1 2 3 4
        visitedB = new boolean[n + 1]; // 0 1 2 3 4

        //더미 0만큼 추가한 정점의 개수만큼 생성
        for (int i = 0; i < n + 1; i++) {
            arr.add(new ArrayList<>());
        }

        // 0 1 2 3 4
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int front = Integer.parseInt(st.nextToken());
            int back = Integer.parseInt(st.nextToken());

            //양 방향으로 넣어준다
            arr.get(front).add(back);
            arr.get(back).add(front);
        }

        //인접 중에서 작은 순으로 검색하기 위해 행들 정렬
        for (int i = 1; i < n + 1; i++) {
            Collections.sort(arr.get(i));
        }

        dfs(v);
        System.out.println();
        bfs(v);



        br.close();
    }
}
