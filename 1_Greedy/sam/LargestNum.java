import java.util.*;

public class LargestNum {
    public static void main(String[] args) {
        /*
        // LinkedList version
        LinkedList<String> list = new LinkedList<>(Arrays.asList(number.split("")));
        max = number.length();
        //전체 중복 시 앞에서부터 k만큼 삭제
        boolean allEqual = new HashSet<>(Arrays.asList(number.split(""))).size() == 1;
        if (allEqual) {
            while (k > 0) {
                list.removeFirst();
                k--;
            }
        }
        while (k > 0) {
            //i를 처음으로가 아닌 위치를 찾아서 줘보자.
            for (i = 1; i < max; i++) {
                //제외 시킬 것들
                //뒤에꺼 보다만 작으면 지워도 되는지 생각
                if (Integer.parseInt(list.get(i)) < Integer.parseInt(list.get(i + 1))) {
                    list.remove(i);
                    k--;
                    break;
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        for (String s : list)
            sb.append(s);

         */
        //ArrayList Version
        /*

        // 속도 비교 결과 => ArrayList > LinkedList why ?? => 둘다 런타임에러
        //배열에 넣지 않는다 ? 큰수를 몇번 찾아서 새로운 문자열에 넣는다
        ArrayList<String> al = new ArrayList<>(Arrays.asList(number.split("")));
        max = al.size();

        //1. 반복문을 이용해 전부 중복인지 검사 o
        //2. Set 이용해 전부 중복인지 검사 X => 새로운 배열을 만들고 hash에 넣는 것이므로 이방식 역시 느릴 가능성 o
        boolean allEqual = new HashSet<>(Arrays.asList(number.split(""))).size() == 1;
        if (allEqual) {
            while (k > 0) {
                al.remove(0);
                k--;
            }
        }

        while (k > 0) {
            //i를 처음으로가 아닌 위치를 찾아서 줘보자.
            for (i = 0; i < max - 1; i++) {
                //같은건 마지막 if 에서 검사.
                //제외 시킬 것들
                //뒤에꺼 보다만 작으면 지워도 되는지 생각
                if (al.get(i).compareTo(al.get(i + 1)) < 0) {
                    al.remove(i);
                    k--;
                    break;
                }
            }
        }

         */

        Solution sol = new Solution();
        System.out.println(sol.solution("1924", 3));
        System.out.println(sol.solution("1111", 2));
        System.out.println(sol.solution("1231234", 3));
        System.out.println(sol.solution("4177252841", 4));


    }
}

class Solution {
    public String solution(String number, int k) {
        StringBuilder sb = new StringBuilder(number);
        sb.append(9);
        int i, max = sb.length()-1;
        boolean tf = true;
        while (k > 0) {
            for (i = 0; i < max; i++) {
                String cur = Character.toString(sb.charAt(i));
                String next = Character.toString(sb.charAt(i + 1));
                if(tf)
                    if(!(cur.equals(next)))
                        tf = false;
                if (cur.compareTo(next) < 0) {
                    sb.deleteCharAt(i);
                    k--;
                    break;
                }
            }
            //다 같은 경우
            if(tf) {
                while(k>0) {
                    sb.deleteCharAt(0);
                    k--;
                }
                break;
            }
        }
        sb.deleteCharAt(sb.length()-1);
        return sb.toString();
    }
}
