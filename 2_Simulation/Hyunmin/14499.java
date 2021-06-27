import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 14499 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        Dice d = new Dice();

        int n, m, x, y, k;
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        x = Integer.parseInt(st.nextToken());
        y = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        int[][] map = new int[n][m];
        int[] path = new int[k];

        // 동[1] 서[2] 북[3] 남[4]
        int[] xx = {0, 0, 0, -1, 1}; //index 0은 더미
        int[] yy = {0, 1, -1, 0, 0}; //index 0은 더미


        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++)
                map[i][j] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < k; i++)
            path[i] = Integer.parseInt(st.nextToken());

        for (int i = 0; i < k; i++) {

            //주사위를 놓은 곳의 좌표와 이동시키는 명령이 주어졌을 때,
            //주사위가 이동했을 때 마다 상단에 쓰여 있는 값을 구하는 프로그램을 작성하시오.
            //주사위는 지도의 바깥으로 이동시킬 수 없다.
            //만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며, 출력도 하면 안 된다.
            //안전범위 일 때
            if(x+xx[path[i]]<n && y+yy[path[i]]<m && x+xx[path[i]]>=0 && y+yy[path[i]]>=0) {
                //주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다.
                if(map[x][y]==0) {
                    map[x][y] = d.getDown();
                }
                //0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.
                else {
                    d.setDown(map[x][y]);
                    map[x][y] = 0;
                }
                //동
                if(path[i]==1) {
                    d.turnEast();
                }
                //서
                if(path[i]==2) {
                    d.turnWest();
                }
                //북
                if(path[i]==3) {
                    d.turnSouth();
                }
                //남
                if(path[i]==4) {
                    d.turnNorth();
                }
                //좌표 이동
                x += xx[path[i]];
                y += yy[path[i]];
                System.out.println(d.getUp());
            }
        }
        br.close();
    }
}

class Dice {
    //동 서 남 북
    //East West North South
    //상 하 / 좌 우 / 앞 뒤
    //필요한 좌표는 상 앞 우 / 상앞우만 알면 나머지 유추가능

    //편의를 위해 0은 더미/ 0    1 2 3 4 5 6 / size 7
    int[] diceNum;
    private final int diceMax = 7;
    //상, 앞, 우
    int up, front, right;
    int temp;
    Dice() {
        diceNum = new int[7];
        up = 1;
        front = 5;
        right = 3;
        temp = 0;
    }
    void turnEast() {
        temp = right;
        right = up;
        up = diceMax - temp;
    }
    void turnWest() {
        temp = up;
        up = right;
        right = diceMax - temp;
    }
    void turnSouth() {
        temp = up;
        up = front;
        front = diceMax - temp;
    }
    void turnNorth() {
        temp = front;
        front = up;
        up = diceMax - temp;
    }
    int getUp() {
        return diceNum[up];
    }
    //diceNum에 들어있는 바닥 "값" 구하기
    int getDown() {
        //현재, 7에서 상을 빼면 하가 나옴
        //하의 값을 리턴
        return diceNum[diceMax-up];
    }
    void setDown(int mapNum) {
        //현재, 7에서 상을 빼면 하가 나옴
        diceNum[diceMax-up] = mapNum;
    }
}
