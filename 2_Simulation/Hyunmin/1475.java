import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 1475 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String number = br.readLine();
        int setNumber = 1;
        int numberCnt = 0;
        int length = number.length();
        int[] numArr = new int[10];

        while (numberCnt < length) {
            int temp = number.charAt(numberCnt) - '0';
            if (temp == 6 || temp == 9) {
                //둘다 1이면 새로운 통 만든다
                if(numArr[6] != 0 && numArr[9] != 0) {
                    for (int clear = 0; clear < 10; clear++)
                        numArr[clear] = 0;
                    numArr[temp]++;
                    setNumber++;
                }
                //6에 이미 값이 있으면 9를 ++
                else if(numArr[6] != 0)
                    numArr[9]++;
                else if(numArr[9] != 0)
                    numArr[6]++;
                    //둘다 0이면?
                else
                    numArr[temp]++;
            }
            //6이랑 9가 아닐 경우
            else {
                //숫자통에 숫자가 0이라면.
                if (numArr[temp] == 0)
                    numArr[temp]++;
                    //배열 초기화 and setNumber++;
                else {
                    for (int clear = 0; clear < 10; clear++)
                        numArr[clear] = 0;
                    numArr[temp]++;
                    setNumber++;
                }
            }
            numberCnt++;
        }
        System.out.println(setNumber);
        br.close();
    }
}
//import java.io.BufferedReader;
//import java.io.IOException;
//import java.io.InputStreamReader;
//
//public class Main {
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        String number = br.readLine();
//        int length = number.length();
//
//        int[] numArr = new int[10];
//        int[] arr = new int[length];
//
//        for (int i = 0; i < length; i++)
//            arr[i] = Integer.parseInt(Character.toString(number.charAt(i)));
//
//
//        for (int i = 0; i < length; i++) {
//            int temp = arr[i]; //넘버 값 차례대로
//            if(temp==6 || temp==9) {
//                numArr[9]++;   //9에 몰아서 넣는다.
//            }
//            else {
//                numArr[temp]++;
//            }
//        }
//        //6 9 제외 가장 큰 값 구해오기
//        int biggest = 0;
//        for (int i = 0; i < length-1; i++) {
//               if(numArr[6]<=numArr[i]) { // 9999면 ? 9의 개수 arr[i] == 4
//                   numArr[6] = numArr[i];
//               }
//        }
//
//
//
//
//
//        // [4, 2]
//        // 0인 경우도 포함? , 69 6969 696969 69696 짝수라면
////        int biggest2 = 0;
//        if(numArr[9]%2==0) {
//            numArr[9] /= 2;
//        }
//        // 홀수라면
//        else {
//            numArr[9] = numArr[9]/2 + 1;
//        }
//        int real = Math.max(numArr[6], numArr[9]);
//        if(number.equals("0"))
//            real = 1;
//        System.out.println(real);
//    }
//}
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String number = br.readLine();
        int[] numArr = new int[10];
        for (char c : number.toCharArray()) {
            int num = c - '0';
            if (num == 6) {
                num = 9;
            }
            numArr[num]++;
        }
        numArr[9] = numArr[9] / 2 + numArr[9] % 2;
        for (int i = 0; i < numArr.length - 1; i++) {
            if (numArr[6] <= numArr[i]) {
                numArr[6] = numArr[i];
            }
        }
        System.out.println(Math.max(numArr[6], numArr[9]));
    }
}
