import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        Solution sol = new Solution();
        int n, result;
        List<Integer> lost = new LinkedList<>();
        List<Integer> reserve = new LinkedList<>();

        n = Integer.parseInt(br.readLine());

        StringTokenizer strTemp = new StringTokenizer(br.readLine());
        while (strTemp.hasMoreTokens())
            lost.add(Integer.parseInt(strTemp.nextToken()));

        strTemp = new StringTokenizer(br.readLine());
        while (strTemp.hasMoreTokens())
            reserve.add(Integer.parseInt(strTemp.nextToken()));


        //List-> int[] 로 변환 (Stream 이해 더 필요)
        result = sol.solution(n, lost.stream().mapToInt(Integer::intValue).toArray(), reserve.stream().mapToInt(Integer::intValue).toArray());

        System.out.println(result);

        bw.flush();
        bw.close();
        br.close();
    }
}

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int i, answer = 0;
        answer = n;

        int[] total = new int[n + 2]; //앞 뒤에 더미 생성
        //전체학생 만들어 초기화
        for (i = 0; i < n + 2; i++)
            total[i] = 1;

        //체육복 2개 = 2
        for (i = 0; i < reserve.length; i++)
            total[reserve[i]] = 2;

        for (i = 0; i < lost.length; i++)
            total[lost[i]]--;

        //reserve 계산
        for (i = 0; i < reserve.length; i++) {
            //지자리 -1
            if (total[reserve[i] - 1]==0 && total[reserve[i]]==2)
                total[reserve[i] - 1] = 1; // 값 삽입
            //지자리 +1
            else if (total[reserve[i] + 1] == 0&& total[reserve[i]]==2)
                total[reserve[i] + 1] = 1; // 값 삽입
        }

        for (i = 0; i < n + 2; i++)
            if(total[i]==0)
                answer--;

        return answer;
    }
}

