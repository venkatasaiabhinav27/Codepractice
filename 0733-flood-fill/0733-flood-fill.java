class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        Stack<int[]> pixels = new Stack<>();
        Set<String> track = new HashSet<>();
        int orgColor = image[sr][sc];
        System.out.println(sr + "  " + sc);
        pixels.push(new int[]{sr, sc});
        while (pixels.size() > 0) {
            int[] pixel = pixels.pop();
            System.out.println(pixel[0] + "  " + pixel[1]);

            image[pixel[0]][pixel[1]] = color;
            track.add(pixel[0]+","+pixel[1]);

            if (pixel[0]-1 > -1 && image[pixel[0]-1][pixel[1]] == orgColor && !track.contains(pixel[0]-1+","+pixel[1])) {
                pixels.push(new int[]{pixel[0]-1, pixel[1]});
            }

            if (pixel[0]+1 < image.length && image[pixel[0]+1][pixel[1]] == orgColor && !track.contains(pixel[0]+1+","+pixel[1])) {
                pixels.push(new int[]{pixel[0]+1, pixel[1]});
            }

            if (pixel[1]-1 > -1 && image[pixel[0]][pixel[1]-1] == orgColor && !track.contains(pixel[0]+","+(pixel[1]-1))) {
                pixels.push(new int[]{pixel[0], pixel[1]-1});
            }

            if (pixel[1]+1 < image[pixel[0]].length && image[pixel[0]][pixel[1]+1] == orgColor && !track.contains(pixel[0]+","+pixel[1]+1)) {
                pixels.push(new int[]{pixel[0], pixel[1]+1});
            }
        }

        return image;
    }
}