impl Solution {
    pub fn kids_with_candies(candies: Vec<i32>, extra_candies: i32) -> Vec<bool> {
        

        let mut list: Vec<bool> = Vec::new();
        let max = candies.iter().max().unwrap();

        for i in 0..candies.len(){

            let result=if candies[i]+extra_candies>=*max{
                true
            }else{
                false
            };

            list.push(result);

        }

        list

    }
}