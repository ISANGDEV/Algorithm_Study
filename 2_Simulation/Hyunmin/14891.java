import java.io.*;
import java.util.StringTokenizer;

public class 14891 {
    public static void main(String[] args) throws IOException {
        //톱니바퀴를 회전시키려면, 회전시킬 톱니바퀴와 회전시킬 방향을 결정해야 한다.
        //톱니바퀴가 회전할 때, 서로 맞닿은 극에 따라서 옆에 있는 톱니바퀴를 회전시킬 수도 있고, 회전시키지 않을 수도 있다.
        //톱니바퀴 A를 회전할 때, 그 옆에 있는 톱니바퀴 B와 서로 맞닿은 톱니의 극이 다르다면,
        // 돌리기 전 맞닿 극 다르면 돌림
        //B는 A가 회전한 방향과 반대방향으로 회전하게 된다.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        Gear g = new Gear();
        int[][] gears = new int[4][8];
        for (int i = 0; i < 4; i++) {
            String temp = br.readLine();
            for (int j = 0; j < 8; j++)
                gears[i][j] = temp.charAt(j) - '0';
        }

        int k = Integer.parseInt(br.readLine());

        int[][] orderArr = new int[k][2];

        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < 2; j++) {
                orderArr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i < k; i++) {
            g.cycle(gears, orderArr[i][0] - 1, orderArr[i][1]);
        }
//        System.out.println(g.getScore(gears));


        br.close();
    }
}

class Gear {

    int[][] arr = new int[4][2];

    Gear() {
        for (int i = 0; i < 4; i++) {
            //왼쪽 바라보는 방향 idx = 6 초기화
            arr[i][0] = 6;
            //오른 바라보는 방향 idx = 2 초기화
            arr[i][1] = 2;
        }
    }

    //특정 톱니의 좌우 값
    int getGearLeft(int gearNum) {
        return arr[gearNum - 1][0];
    }

    int getGearRight(int gearNum) {
        return arr[gearNum - 1][1];
    }

    void left(int[][] gears, int left, int turnNum) {
        //left = 1
        if(left<0)
            return;
        System.out.println("left");
        System.out.println(gears[left][getGearRight(left+1)]);
        System.out.println(gears[left+1][getGearLeft(left+1+1)]);
        if (gears[left][getGearRight(left+1)] != gears[left+1][getGearLeft(left+1+1)]) {
            if (turnNum == 1) {
                turnRight(left + 1);
            } else {
                turnLeft(left + 1);
            }
        }
        left(gears, left - 1, -turnNum);
    }
    void right(int[][] gears, int right, int turnNum) {
        //현재의 오른쪽과 오른쪽의 왼쪽
        //3 , 2
        if(right>3)
            return;

        System.out.println("righ");
        System.out.println(gears[right][getGearRight(right + 1)]);
        System.out.println(gears[right-1][getGearLeft(right)]);

//
        if (gears[right][getGearRight(right + 1)] != gears[right-1][getGearLeft(right)]) {
            if (turnNum == 1) {
                turnRight(right + 1);
            } else {
                turnLeft(right + 1);
            }
        }
        right(gears, right + 1, -turnNum);

    }

    void cycle(int[][] gears, int gearNum, int turnNum) {
        // 0 1 2 3
        // 2
        int left = gearNum - 1;
        // 1
        left(gears, left, -turnNum);
        int right = gearNum + 1;
        right(gears, right, -turnNum);

        if(turnNum==1)
            turnLeft(gearNum);
        else
            turnRight(gearNum);

    }

    int getScore(int[][] gears) {
        int total = 0;
        int sNum = 1;
        for (int i = 0; i < 4; i++, sNum*=2) {
            //s극
            if(gears[i][0] == 1) {
                total += sNum;
            }

        }
        return total;

    }


    void turnRight(int gearNum) {
        if (arr[gearNum - 1][0] - 1 < 0)
            arr[gearNum - 1][0] = 7;
        else
            arr[gearNum - 1][0] -= 1;

        if (arr[gearNum - 1][1] - 1 < 0)
            arr[gearNum - 1][1] = 7;
        else
            arr[gearNum - 1][1] -= 1;
    }

    void turnLeft(int gearNum) {
        if (arr[gearNum - 1][0] + 1 > 7)
            arr[gearNum - 1][0] = 0;
        else
            arr[gearNum - 1][0] += 1;

        if (arr[gearNum - 1][1] + 1 > 7)
            arr[gearNum - 1][1] = 0;
        else
            arr[gearNum - 1][1] += 1;
    }
}


