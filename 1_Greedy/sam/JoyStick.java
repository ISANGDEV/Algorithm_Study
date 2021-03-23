public class JoyStick {
    public static void main(String[] args) {

        Solution sol = new Solution();
        System.out.println("\n" + sol.solution("BBBAAAB") + "\n");
        System.out.println("\n" + sol.solution("ABABAAAAABA") + "\n");
        System.out.println("\n" + sol.solution("BAAABA") + "\n");
        System.out.println("\n" + sol.solution("BABAA") + "\n");
        System.out.println("\n" + sol.solution("JAZ") + "\n");
        System.out.println("\n" + sol.solution("JEROEN") + "\n");
        System.out.println("\n" + sol.solution("JAN") + "\n");
        System.out.println("\n" + sol.solution("H") + "\n");

    }
}
class Solution {
    public int solution(String name) {
        int answer = 0;
        int move = 0;
        int max = name.length();
        boolean PATH;
        boolean ISA = false;
        int i;
        int j;

        int[] arr = new int[max]; // 마지막 비교 시 StringIndexOutOfBoundsException 방지용 더미
        PATH = false;
        for (i = 0; i < max - 1; i++) {
            if (name.charAt(i) == 'A' && name.charAt(i + 1) == 'A') {
                arr[i] = -1;
                arr[i + 1] = -1;
                PATH = true;
                ISA = true;
            } else {
                if (!PATH) {
                    if ((int) name.charAt(i) - 65 <= 13)
                        arr[i] = (int) name.charAt(i) - 65;
                    else
                        arr[i] = 90 - ((int) name.charAt(i) - 1);
                } else {
                    PATH = false;
                }
            }
        }
        if (!PATH) {
            if ((int) name.charAt(i) - 65 <= 13)
                arr[max - 1] = (int) name.charAt(i) - 65;
            else
                arr[max - 1] = 90 - ((int) name.charAt(i) - 1);
        }
        //배열 비교를 해야하는데 문자가 1개일 경우
        if (max == 1) {
            answer += arr[0];
            return answer;
        }
        //-1 대칭일 경우 AABAA
        //앞 >= 뒤  방향 =>
        if (arr[1] >= arr[max - 1]) {
            if(ISA) {

                PATH = false;
                i = 0;
                j = 0;
                for (; i < max; i++) {
                    //-1이 아닌 값인 경우
                    if (arr[i] != -1) {
                        if (PATH) {
                            move += j;
                            j = 0;
                            PATH = false;
                            answer += arr[i];
                            continue;


                        }
                        if (arr[i] == 0 && i == max - 1)
                            continue;
                        answer += arr[i];
                        move++;

                    }
                    //-1값인 경우
                    else {
                        PATH = true;
                        j++;
                    }

                }
                answer += move - 1;

            }
            else {
                i = 0;
                for (; i < max; i++) {
                    if (arr[i] != -1) {
                        if (arr[i] == 0&&i==max-1)
                            continue;
                        answer += arr[i];
                        move++;
                    }
                }
                answer += move-1;
            }

        }
        //앞 <= 뒤  방향 <=
        else {
            if(ISA) {
                //JAJAAAJ
                //AABAA
                //BBCBB
                PATH = false;
                if (arr[0] != -1)
                    answer += arr[0];
                i = max - 1;
                j = 0;
                for (; i > 0; i--) {
                    //-1이 아닌 값인 경우
                    if (arr[i] != -1) {
                        if (PATH) {
                            move += j;
                            j = 0;
                            PATH = false;
                            answer += arr[i];
                            continue;

                        }
                        if (arr[i] == 0 && i == 1)
                            continue;
                        answer += arr[i];
                        move++;

                    }
                    //-1값인 경우
                    else {
                        PATH = true;
                        j++;
                    }

                }

                answer += move;
            }
            else {
                if (arr[0] != -1)
                    answer += arr[0];
                i = max - 1;
                for (; i > 0; i--) {
                    if (arr[i] != -1) {
                        if (arr[i] == 0 && i == 1)
                            continue;
                        answer += arr[i];
                        move++;
                    }
                }
                answer += move;
            }

        }
        //같을경우 ? 같을 경우는 뒤로 하나 앞으로 하나 같은 결과로 예상
        return answer;
    }
}

