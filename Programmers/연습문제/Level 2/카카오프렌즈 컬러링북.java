class Solution {
    public int[] solution(int m, int n, int[][] picture) {
        static int numberOfArea = 0;
        static int maxSizeOfOneArea = 0;

        static picture;
        static int[] dx = {-1, 1, 0, 0};
        static int[] dy = {0, 0, -1, 1};
        static boolean[][] isChecked = new boolean[m][n];
        static int sizeOfOneArea = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (picture[i][j] != 0 && !isChecked[i][j]) {
                    numberOfArea++;
                    sizeOfOneArea = dfs(i, j, picture, isChecked);
                }
                if (sizeOfOneArea > maxSizeOfOneArea) {
                    maxSizeOfOneArea = sizeOfOneArea;
                    sizeOfOneArea = 0;
                }
            }
        }

        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }

    private int dfs(int x, int y) {
        if (isChecked[x][y]) {
            return;
        }

        isChecked[x][y] = true;
        numberOfArea++;

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || nx >= m || ny < 0 || ny >= n) {
                continue;
            }

            if (picture[x][y] = picture[nx][ny] && !check[nx][ny]) {
                dfs(nx, ny);
            }
        }
    }
}