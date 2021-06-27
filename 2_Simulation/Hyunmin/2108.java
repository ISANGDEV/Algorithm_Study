import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

public class 2108 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        //N은 홀수
        //산술평균 : N개의 수들의 합을 N으로 나눈 값
        //중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
        //최빈값 : N개의 수들 중 가장 많이 나타나는 값
        //범위 : N개의 수들 중 최댓값과 최솟값의 차이
        int n = Integer.parseInt(br.readLine());
        double total = 0;
        int[] arr = new int[n];
        List<Integer> list = new LinkedList<>();

        int[] choi = new int[8001]; // 4000+4000

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
            total += arr[i];
            choi[arr[i] + 4000]++;
        }
        //최빈값이 없을 경우를 위해 0번째 미리 저장

        // 1. 산술평균
        // !float 으로 넣으면 틀리고! double로 넣으면 안틀림 WHY ?
        System.out.println(Math.round((total/n)));

        // 2. 중앙값
        Arrays.sort(arr);
        System.out.println(arr[n / 2]);

        // 3. 최빈 값
        int max = 0;
        for (int i = 0; i < 8001; i++) {
            if(max<=choi[i]) {
                //최대 횟수 find
                max = choi[i];
            }
        }

        //중복값이 없을 경우 max== 1 일  시 맨 앞 값 반환

        for (int i = 0; i < 8001; i++) {
            if(max==choi[i]) {
                //최대 횟수인, 값을 찾아서 list에  추가
                list.add(i-4000);
            }
        }
        // 최대 회수 4번 씩 2번
        // 2222 3333
        // 4444 3333
        // 11111 222
        // 2 3
        // 3 4
        // 5
        //최빈수가 값이 딱 1개 뿐이라면
        if(list.size()==1) {
            System.out.println(list.get(0));
        }
        //2 개 이상
        else {
            //두번째로 작은 수
            Collections.sort(list);
            System.out.println(list.get(1));
        }

        // 4. 범위
        System.out.println(arr[n - 1] - arr[0]);

        br.close();
    }
}

