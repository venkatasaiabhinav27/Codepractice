class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0, lastPrice;
        if (prices.length > 0) {
            lastPrice = prices[0];
        } else {
            return 0;
        }

        for (int price:prices) {
            if (price < lastPrice) {
                lastPrice = price;
            } else {
                maxProfit = Math.max(maxProfit, price - lastPrice);
            }
        }

        return maxProfit;
    }
}