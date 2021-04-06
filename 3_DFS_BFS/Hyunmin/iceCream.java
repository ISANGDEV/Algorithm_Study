import java.util.*;
import java.io.*;

class iceCream {
    //그래프 저장 공간  NXM
    public static int[][] g;
    // ArrayList<ArrayList<Integer>> g = new ArrayList<>();

    //x++ y++하면서 계산, return true => 아이스크림 1개
    public static boolean dfs(int x, int y) {
        if ((x >= g.length) || (y >= g[x].length) || (x < 1) || (y < 1))
            return false;

        if (g[x][y] == 0) {
            g[x][y] = 1;
            //오른
            dfs(x, y+1);
            //왼쪽
            dfs(x, y-1);
            //아래
            dfs(x+1, y);
            //위쪽
            dfs(x-1, y);

            return true;
        }
        return false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int i = Integer.parseInt(st.nextToken());
        int j = Integer.parseInt(st.nextToken());
        g = new int[i + 1][j + 1]; //4 5 => 5 6

        for (int x = 1; x < i + 1; x++) {
            int y = 1;
            for (char temp : br.readLine().toCharArray()) {
                g[x][y++] = temp - '0';
            }
        }

        int iceCream = 0;
        for (int x = 1; x < i + 1; x++) {
            for (int y = 1; y < j + 1; y++) {
                //아이디어 1,1에서 처음 호출을 시작하니 스택프레임에 함수가 쌓이기 시작하면
                //1,2,3,4,5 순으로 쌓이고 5,4,3,2,1순으로 리턴되니 마지막엔 제일 처음 넣은 함수의 결과가 리턴 될 것
                if(dfs(x,y))
                    iceCream++;
            }
        }
        System.out.println(iceCream);
    }
}
