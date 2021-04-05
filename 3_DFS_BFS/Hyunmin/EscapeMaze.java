import java.util.*;
import java.io.*;

class EscapeMaze {
    public static int[][] g;
//    public static int[][] gVisited;
    public static int i, j; // 5, 6 => 6 7

    //bfs
    //그래프를 단순화 시켜서 생각 3X3
    //아이디어 다음꺼에 이전숫자+1 삽입
    public static int bfs(int x, int y) {

        Queue<Pos> q = new LinkedList<>();
        q.offer(new Pos(x, y));

        //상하좌우 다음 좌표
        int[] xX = {-1, 1, 0, 0};
        int[] yY = {0, 0, -1, 1};

//        int moved = 1;
        while (!q.isEmpty()) {
//            moved++;
            //현재 좌표
            Pos temp = q.poll();
            if(temp.getX()==i-1 && temp.getY()==j-1) {
                return g[temp.getX()][temp.getY()];
            }

            for (int k = 0; k < 4; k++) {
                //상하좌우
                int nX = temp.getX() + xX[k];
                int nY = temp.getY() + yY[k];

                //범위 조건 만족할 때
                if (nX >= 1 && nY >= 1 && nX < i & nY < j) {
                    //1이면 0이면
                    if (g[nX][nY] == 1 ) {
                        //다음거 큐에 넣는다
                        q.offer(new Pos(nX, nY));
                        //다음 위치에 moved + 1 대신 이전꺼 + 1 을 넣는다
                        g[nX][nY] = g[temp.getX()][temp.getY()] + 1;
                    }
                }
            }
        }
        return 0;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        Pos pos = new Pos();

        i = Integer.parseInt(st.nextToken()) + 1;
        j = Integer.parseInt(st.nextToken()) + 1;

        g = new int[i][j];
//        gVisited = new int[i][j];

        for (int x = 1; x < i; x++) {
            StringBuilder temp = new StringBuilder(br.readLine());
            for (int y = 1; y < j; y++) {
                g[x][y] = temp.charAt(y - 1) - '0';
            }
        }



        System.out.println(bfs(1, 1));

        for (int x = 1; x < i; x++) {
            for (int y = 1; y < j; y++) {
                System.out.print(g[x][y]+ " ");
            }
            System.out.println();
        }
//
//        for (int x = 1; x < i; x++) {
//            for (int y = 1; y < j; y++) {
//                System.out.print(gVisited[x][y]+ " ");
//            }
//            System.out.println();
//        }




        /*
5 6
101010
111111
000001
111111
111111
         */
        br.close();

    }
}

class Pos {

    private int x;
    private int y;

    Pos() {
        x = 0;
        y = 0;
    }

    Pos(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

}

