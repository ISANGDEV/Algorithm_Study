import java.util.*;
import java.io.*;

class 1012 {
    public static int[][] g;     //graph
    public static int n, m;

    public static boolean dfs(int x, int y) {

        if (x < 0 || y < 0 || x >= n || y >= m)
            return false;

        if (g[x][y]==1) {
            g[x][y] = 0;
            //동서남북으로 보내고
            dfs(x, y + 1);
            dfs(x, y - 1);
            dfs(x + 1, y);
            dfs(x - 1, y);

            return true;
        }
        return false;
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;


        int testCase = Integer.parseInt(br.readLine());
        int[] testCaseArr = new int[testCase];

        //dfs가 배추가 심어져 있는 땅인 1을 찾게하기 위해 상하좌우로 위치를 보내고 있으면 true, 없거나 갔었다면 visited후 false
        //리턴 시 main 반복문에서 true라면 지렁이 ++
        while (testCase-- > 0) {

            st = new StringTokenizer(br.readLine(), " ");
            m = Integer.parseInt(st.nextToken());           //M가로
            n = Integer.parseInt(st.nextToken());           //N세로
            int k = Integer.parseInt(st.nextToken());           //K배추 위치 개수

            g = new int[n][m];

            while (k-- > 0) {
                st = new StringTokenizer(br.readLine(), " ");
                //배추 위치 입력시  X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1) 이므로
                //편의를 위해 반대로 삽입
                int y = Integer.parseInt(st.nextToken());
                int x = Integer.parseInt(st.nextToken());
                g[x][y] = 1;
            }

            int wormCnt = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (dfs(i, j))
                        wormCnt++;
                }
            }
            //배열의 뒤에서 부터 저장
            testCaseArr[testCase] = wormCnt;
        }
        for (int i = testCaseArr.length - 1; i >= 0; i--)
            System.out.println(testCaseArr[i]);

        br.close();
    }
}



