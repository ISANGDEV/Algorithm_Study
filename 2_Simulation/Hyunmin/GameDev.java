import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class GameDev {
    public static void main(String[] args) {
        Solution sol = new Solution();

        try {
            System.out.println("answer: "  + sol.solution());

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

class Solution {
    public int solution() throws IOException {
        int answer = 0;
        int i, j, d;

        List<InsideData> al = new ArrayList<>();
        al.add(new InsideData(-1, 0, 0)); //북
        al.add(new InsideData(0, 1, 1)); //동
        al.add(new InsideData(1, 0, 2)); //남
        al.add(new InsideData(0, -1, 3)); //서

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        i = Integer.parseInt(st.nextToken());
        j = Integer.parseInt(st.nextToken());
        int[][] map = new int[i][j]; // 4 4

        st = new StringTokenizer(br.readLine(), " ");


        InsideData myPos = new InsideData(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));

        for (int x = 0; x < i; x++) {
            st = new StringTokenizer(br.readLine(), " ");
            for (int y = 0; y < j; y++) {
                map[x][y] = Integer.parseInt(st.nextToken());
            }
        }
        br.close();

        InsideData temp = new InsideData(0, 0, 0);
        int cycleCnt = 0;
        // [0] [1] [2] [3]
        // 북  서  남  동
        // 회전 4번을 안에서 구현하는 것이 아니라 회전은 1번만.


        while (true) {
            //회전
            temp.change(myPos.getD()); // 3
            cycleCnt++;

            //초기화
            //다음 좌표의 x,y
            temp.setTemp(al.get(temp.getD()).getX() + myPos.getX(), al.get(temp.getD()).getY() + myPos.getY(), temp.getD()); //서 3
            //북 -> 서 -> 남 -> 동

            //정상 범위 안에 존재 할 때
            if ((temp.getX() < i && temp.getX() >= 0) && (temp.getY() < j && temp.getY() >= 0)) {
                if (map[temp.getX()][temp.getY()] == 0) {

                    answer++;
                    map[myPos.getX()][myPos.getY()] = -1;
                    myPos.setX(temp.getX());
                    myPos.setY(temp.getY());

                    cycleCnt = 0;
                }
                //
                if (cycleCnt >= 4) {
                    //이전 방향
                    int back = (temp.getD() >= 2) ? temp.getD() - 2 : temp.getD() + 2;
                    //이전 방향의 좌표가 바다면
                    if (map[al.get(back).getX() + myPos.getX()][al.get(back).getY() + myPos.getY()] == 1) {
                        break;
                    }
                    //이전 방향의 좌표가 가봤던 곳 이라면
                    if (map[al.get(back).getX() + myPos.getX()][al.get(back).getY() + myPos.getY()] == -1) {
                        answer++;
                        map[myPos.getX()][myPos.getY()] = -1;
                        myPos.setX(al.get(back).getX() + myPos.getX());
                        myPos.setY(al.get(back).getY() + myPos.getY());
                        cycleCnt = 0;
                    }
                }
            }
            //방향 저장
            myPos.setD(temp.getD());
        }
        return answer;
    }
}

class InsideData {
    int x;
    int y;
    int d;

    InsideData(int x, int y, int d) {
        this.x = x;
        this.y = y;
        this.d = d;
    }

    void setTemp(int x, int y, int d) {
        this.x = x;
        this.y = y;
        this.d = d;
    }

    void change(int d) {
        this.d = d - 1;
        if(this.d<0)
            this.d = 3;
    }

    int getX() {
        return x;
    }

    int getY() {
        return y;
    }

    int getD() {
        return d;
    }

    void setX(int x) {
        this.x = x;
    }

    void setY(int y) {
        this.y = y;
    }

    void setD(int d) {
        this.d = d;
    }

    @Override
    public String toString() {
        return "InsideData{" +
                "x=" + x +
                ", y=" + y +
                ", d=" + d +
                '}';
    }
}
